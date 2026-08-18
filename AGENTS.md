# HeX-Control Agent Instructions

This repository is currently a small scaffold, but future work must use the same state-first execution rule as the rest of the FormatX66 project stack.

Before meaningful action, determine proportionally:

`intent -> observed current state -> required state -> delta -> constraints -> minimum useful action -> verification`

Only perform work that can change a required state or produce genuinely new evidence. Prefer deterministic/local work, deduplicate retries, distinguish waiting/refused/blocked/no-change from true failure, verify consequential results, and fix recurring problems at the earliest shared invariant rather than repeating the same action.
