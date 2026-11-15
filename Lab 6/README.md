# Lab 6 — Code and Branch Coverage

Run the commands from this folder after installing the project requirements from the repository root (`python -m pip install -r requirements.txt`).

## Line coverage

```bash
python -m coverage erase
python -m coverage run --source=mobile_data_plan -m pytest CodeCoverageTest_PES2UG24AM205_application.py
python -m coverage report -m
```

Save a screenshot of the final passing test output and coverage report as `../evidence/Lab6_CodeCoverage.png`.

## Branch coverage

```bash
python -m coverage erase
python -m coverage run --branch --source=mobile_data_plan -m pytest BranchCoverageTest_PES2UG24AM205_application.py
python -m coverage report --branch -m
```

Save a screenshot of the final passing test output and branch coverage report as `../evidence/Lab6_BranchCoverage.png`. The handout asks for screenshots only after the relevant coverage result reaches at least 90%.
