#!/usr/bin/env python3
import hashlib
import json
import os
import platform
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path


def utcnow():
    return datetime.now(timezone.utc).isoformat()


def main():
    request_id = os.environ.get("REQUEST_ID") or str(uuid.uuid4())
    intent = os.environ.get("HUMAN_INTENT", "harmless proof request")
    transport = os.environ.get("TRANSPORT", "unknown")
    started = utcnow()

    result = {
        "request_id": request_id,
        "original_human_intent": intent,
        "interpreted_task": "safe-proof-echo",
        "selected_execution_path": transport,
        "current_state": "running",
        "actions_attempted": ["normalize intent", "collect runtime evidence", "hash evidence"],
        "successful_actions": [],
        "failed_actions": [],
        "evidence": {},
        "artifacts": [],
        "predicted_future_branches": [
            {"branch": "verify feedback retrieval from GPT", "confidence": "high", "safe": True},
            {"branch": "add adapter registry", "confidence": "high", "safe": True},
            {"branch": "connect self-hosted Aurum runner capability report", "confidence": "medium", "safe": True}
        ],
        "checkpoints": [{"state": "running", "at": started}],
        "recommended_next_action": "Have GPT retrieve and verify this execution result.",
        "completion_status": "running",
        "timestamps": {"created": started, "started": started, "completed": None, "verified": None}
    }

    proof = {
        "intent": intent,
        "transport": transport,
        "platform": platform.platform(),
        "python": sys.version.split()[0],
        "runner": os.environ.get("RUNNER_NAME", "unknown"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID", "unknown"),
        "epoch": int(time.time())
    }
    digest = hashlib.sha256(json.dumps(proof, sort_keys=True).encode()).hexdigest()
    result["evidence"] = {"proof": proof, "sha256": digest}
    result["successful_actions"] = result["actions_attempted"].copy()
    result["current_state"] = "completed"
    result["completion_status"] = "completed_pending_external_verification"
    result["timestamps"]["completed"] = utcnow()
    result["checkpoints"].append({"state": "completed", "at": result["timestamps"]["completed"]})

    out_dir = Path(os.environ.get("OUTPUT_DIR", "state/runs"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{request_id}.json"
    out_path.write_text(json.dumps(result, indent=2) + "\n")
    Path("state/current.json").parent.mkdir(parents=True, exist_ok=True)
    Path("state/current.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
