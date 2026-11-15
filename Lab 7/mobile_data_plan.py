"""Parse mobile plan inputs and calculate daily use and payable bills."""

import math


VALID_PLANS = {"basic", "standard", "premium"}


def parse_plan(text):
    """Parse and validate a plan string formatted as ``plan:data_gb``."""
    if not isinstance(text, str) or text.count(":") != 1:
        raise ValueError("plan must use the format plan:data_gb")

    plan_text, data_text = text.split(":")
    plan = plan_text.strip().lower()
    if plan not in VALID_PLANS:
        raise ValueError("plan must be basic, standard, or premium")
    if not data_text.strip():
        raise ValueError("data usage is required")

    try:
        data_gb = float(data_text)
    except ValueError as error:
        raise ValueError("data usage must be numeric") from error

    if not math.isfinite(data_gb) or data_gb < 0:
        raise ValueError("data usage must be a finite non-negative number")
    return plan.title(), data_gb


def usage_average(usage_csv):
    """Return the integer average of non-negative comma-separated MB values."""
    if not isinstance(usage_csv, str) or not usage_csv.strip():
        raise ValueError("usage must be a non-empty CSV string")

    fields = usage_csv.split(",")
    if any(not field.strip() for field in fields):
        raise ValueError("usage CSV cannot contain empty values")

    try:
        values = [int(field.strip()) for field in fields]
    except ValueError as error:
        raise ValueError("usage values must be integers") from error

    if any(value < 0 for value in values):
        raise ValueError("usage values must be non-negative")
    return sum(values) // len(values)


def payable_bill(text):
    """Calculate a bill with tax and a fixed discount, never below zero."""
    if not isinstance(text, str) or text.count("|") != 1:
        raise ValueError("bill must use the format bill|discount")

    bill_text, discount_text = text.split("|")
    if not bill_text.strip() or not discount_text.strip():
        raise ValueError("bill and discount are both required")

    try:
        bill = float(bill_text)
        discount = float(discount_text)
    except ValueError as error:
        raise ValueError("bill and discount must be numeric") from error

    if not math.isfinite(bill) or not math.isfinite(discount):
        raise ValueError("bill and discount must be finite numbers")
    if bill < 0 or discount < 0:
        raise ValueError("bill and discount must be non-negative")
    return max(bill * 1.18 - discount, 0)


def _run_prompt(title, prompt, processor):
    """Read one input and display either its result or a clear validation error."""
    print(f"==== {title} ====")
    try:
        result = processor(input(prompt))
    except ValueError as error:
        print(f"Invalid input: {error}")
    else:
        print("Result:", result)


def main():
    """Run the interactive examples for all three input processors."""
    _run_prompt(
        "Running parse_plan",
        "Enter plan:data in GB (e.g. standard:5): ",
        parse_plan,
    )
    _run_prompt(
        "Running usage_average",
        "Enter daily usage in MB as CSV (e.g. 300,450,800): ",
        usage_average,
    )
    _run_prompt(
        "Running payable_bill",
        "Enter bill|discount (e.g. 399|50): ",
        payable_bill,
    )


if __name__ == "__main__":
    main()
