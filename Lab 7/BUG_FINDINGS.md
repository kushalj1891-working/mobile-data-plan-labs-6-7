# Lab 7 Input Validation Findings

The following cases are represented in the fuzz suite. The original implementation is preserved in `mobile_data_plan_before.py` so the failures can be reproduced with Hypothesis after installing the requirements. These are source-level expectations; the Hypothesis run has not yet been executed in this environment.

| Function | Input | Original behavior | Hardened behavior |
|---|---|---|---|
| `parse_plan` | `None` | Calls `.split` on `None`, raising `AttributeError`. | Raises a clear `ValueError`. |
| `parse_plan` | `standard:nan` or `standard:-1` | Accepts non-finite or negative data usage. | Rejects values that are not finite and non-negative. |
| `usage_average` | `None` | Calls `.split` on `None`, raising `AttributeError`. | Raises a clear `ValueError`. |
| `usage_average` | `1,,3` or `-1,2` | Empty fields fail indirectly; negative usage can be accepted. | Rejects empty fields and negative values. |
| `payable_bill` | `None` | Calls `.split` on `None`, raising `AttributeError`. | Raises a clear `ValueError`. |
| `payable_bill` | `399|nan` | Can return `NaN`. | Rejects non-finite values. |
| `payable_bill` | `-1|0` or `1|-1` | Accepts negative monetary input. | Rejects negative bill and discount values. |
