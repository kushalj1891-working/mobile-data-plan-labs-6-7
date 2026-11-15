"""Hypothesis fuzz tests for mobile plan input validation (Lab 7)."""

import math

from hypothesis import example, given, settings, strategies as st

from mobile_data_plan import parse_plan, payable_bill, usage_average


FUZZ_SETTINGS = settings(max_examples=300, deadline=None)
INPUTS = st.text() | st.none()


@FUZZ_SETTINGS
@given(INPUTS)
@example(None)
@example("")
@example("standard:nan")
@example("standard:inf")
@example("standard:-1")
def test_parse_plan_accepts_valid_values_or_rejects_cleanly(value):
    try:
        result = parse_plan(value)
    except ValueError:
        return

    assert isinstance(result, tuple)
    assert len(result) == 2
    plan, data_gb = result
    assert plan in {"Basic", "Standard", "Premium"}
    assert math.isfinite(data_gb)
    assert data_gb >= 0


@FUZZ_SETTINGS
@given(INPUTS)
@example(None)
@example("")
@example("1,,3")
@example("-1,2")
def test_usage_average_accepts_valid_values_or_rejects_cleanly(value):
    try:
        result = usage_average(value)
    except ValueError:
        return

    assert isinstance(result, int)
    assert result >= 0


@FUZZ_SETTINGS
@given(INPUTS)
@example(None)
@example("")
@example("399|nan")
@example("-1|0")
@example("1|-1")
def test_payable_bill_accepts_valid_values_or_rejects_cleanly(value):
    try:
        result = payable_bill(value)
    except ValueError:
        return

    assert math.isfinite(result)
    assert result >= 0


def test_valid_examples_keep_expected_behavior():
    assert parse_plan("standard:5") == ("Standard", 5.0)
    assert usage_average("300,450,800") == 516
    assert payable_bill("399|50") == 420.82


def test_negative_bill_and_discount_are_rejected():
    for value in ("-1|0", "1|-1"):
        try:
            payable_bill(value)
        except ValueError:
            continue
        raise AssertionError(f"negative value was accepted: {value}")
