# Chat-to-Git Pipeline

Staged bootstrap for the dedicated `FormatX66/Chat-to-Git-Pipeline` repository.

## Human interface

Natural-language execution phrase: **Computer, make it so.**

The human should not need workflow names, API payloads, or webhook syntax.

## Transport order

1. **Direct GitHub transport (primary):** GPT creates a GitHub issue whose title starts with `[make-it-so]`. The `direct.yml` workflow turns that issue into an execution request, runs the safe executor, uploads evidence, and comments machine-readable completion status back on the issue.
2. **Webhook/API transport (fallback):** an external bridge sends a `repository_dispatch` event of type `make-it-so`; `fallback.yml` executes the same runner and records evidence.
3. Additional adapters should call the same runner contract rather than reimplement task logic.

## State model

Every request uses: `proposed -> queued -> running -> completed -> verified` or a terminal `failed` state. A request is never called complete merely because it was accepted.

Each result records request ID, original intent, interpreted task, transport, attempts, successes, failures, evidence, artifacts, Future Branch predictions, checkpoints, recommended next action, timestamps, and verification state.

## Future Branch

Future Branch is a first-class policy: anticipate likely next work; precompute only safe, reversible, high-confidence branches; preserve alternatives; checkpoint long work; score useful versus wasted branches; keep speculation distinct from verified state.

## Codelation resource model

Resources are described by capabilities rather than human labels: latency, bandwidth, compute traits, capacity, speed, persistence, locality, parallelism, cost, and utilization. GitHub runners provide a limited first implementation; later self-hosted Aurum runners can expose richer CPU/GPU/RAM/cache/storage/network capability maps.

## Security

Security is consequence-driven rather than ceremonial. Secrets, destructive authority, privileged infrastructure, personal/financial data, and signing authority are protected. Harmless execution metadata is kept simple and observable. Never commit secrets.

## Initial proof

The safe proof action echoes normalized intent, records platform/runtime metadata, produces a SHA-256 evidence digest, writes a JSON result, and returns it through GitHub. No destructive action is allowed by the bootstrap executor.

## Migration

This directory is intentionally isolated on `chat-to-git-bootstrap` so the work can be moved into its dedicated repository without altering HeX-Control main.