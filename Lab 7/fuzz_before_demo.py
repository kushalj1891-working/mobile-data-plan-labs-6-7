"""Run this file explicitly to reproduce Lab 7's pre-fix fuzz failures."""

from hypothesis import example, given, settings, strategies as st
import pytest

from mobile_data_plan_before import parse_plan, payable_bill, usage_average


FUZZ_SETTINGS = settings(max_examples=100, deadline=None)
INPUTS = st.text() | st.none()


@FUZZ_SETTINGS
@given(INPUTS)
@example(None)
def test_original_parse_plan_does_not_crash(value):
    try:
        parse_plan(value)
    except ValueError:
        return


@FUZZ_SETTINGS
@given(INPUTS)
@example(None)
def test_original_usage_average_does_not_crash(value):
    try:
        usage_average(value)
    except ValueError:
        return


@FUZZ_SETTINGS
@given(INPUTS)
@example(None)
def test_original_payable_bill_does_not_crash(value):
    try:
        payable_bill(value)
    except ValueError:
        return


def test_original_payable_bill_rejects_negative_amount():
    with pytest.raises(ValueError):
        payable_bill("-1|0")
