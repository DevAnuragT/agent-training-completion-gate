# Training Completion Gate

Checks required training courses for completion and explicit expiry dates against a caller-supplied date. It returns a gate result without enrolling or changing records.

## Architecture

```text
JSON payload → domain algorithm → evidence-backed findings → human review
                              └→ OpenAI / CrewAI / Claude Code / Lyzr export surfaces
```

The core implementation is `agent.py` and exposes `analyze(payload)`. Tests include valid, malformed, boundary, and domain-specific cases.

## Run

```bash
python3 agent.py examples/good-input.json
python3 -m unittest discover -s tests -v
python3 tools/audit-training-completion-gate.py examples/good-input.json
```

## Limitations

This core cannot verify course identity, attendance, assessment scores, equivalence, or whether an expiry policy is appropriate. It does not notify learners, update a learning system, grant access, or provide employment or legal advice.
