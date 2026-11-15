# Lab 7 — Fuzz Testing for Input Validation Bugs

Run commands from this folder after installing requirements from the repository root:

```bash
python -m pip install -r ../requirements.txt
```

## Reproduce the original failures

The original program is preserved as `mobile_data_plan_before.py`. To see the example run:

```bash
python mobile_data_plan_before.py
```

Use `standard:5`, `300,450,800`, and `399|50` when prompted. For the failing fuzz-test evidence, run:

```bash
python -m pytest -q fuzz_before_demo.py
```

The examples pass `None` to all three original functions. They crash with unexpected `AttributeError` or `TypeError` instead of rejecting malformed input cleanly.

## Run the hardened version

```bash
python mobile_data_plan.py
python -m pytest -q test_mobile_data_plan.py
```

The updated tests use Hypothesis to generate arbitrary text and `None`, check result invariants, and retain valid examples. Save screenshots of the original app output, failing fuzz tests, fixed app output, and passing tests into `../evidence/` for the Lab 7 PDF deliverable.
