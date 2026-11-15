"""Branch coverage tests for mobile_data_plan.py (SRN PES2UG24AM205)."""

import pytest

from mobile_data_plan import (
    overage_charge,
    recharge_allowed,
    validity_status,
)


@pytest.mark.parametrize(
    ("plan", "data_gb", "roaming", "loyal", "expected"),
    [
        ("basic", 2, False, False, 0),
        ("basic", 3, False, True, 0),
        ("premium", 10, False, True, 0),
        ("standard", 6, False, False, 15),
        ("basic", 3, True, False, 40),
        ("basic", 13, False, False, 275),
        ("basic", 13, True, False, 605),
    ],
)
def test_overage_charge_branches(plan, data_gb, roaming, loyal, expected):
    assert overage_charge(plan, data_gb, roaming, loyal) == expected


@pytest.mark.parametrize(
    ("plan", "data_gb"),
    [("unknown", 1), ("basic", -1)],
)
def test_overage_charge_validation_branches(plan, data_gb):
    with pytest.raises(ValueError):
        overage_charge(plan, data_gb, False, False)


@pytest.mark.parametrize(
    ("amount", "pending", "kyc", "expected"),
    [
        (200, 5, True, True),
        (201, 0, True, False),
        (2001, 0, False, False),
        (2000, 2, False, True),
        (2000, 3, False, False),
    ],
)
def test_recharge_allowed_branches(amount, pending, kyc, expected):
    assert recharge_allowed(amount, pending, kyc) is expected


@pytest.mark.parametrize(
    ("days", "prepaid", "addon", "expected"),
    [
        (0, True, False, "active"),
        (-1, True, False, "grace"),
        (-16, True, False, "expired"),
        (3, False, False, "active"),
        (2, False, False, "grace"),
        (-13, False, False, "expired"),
        (5, False, True, "active"),
        (4, False, True, "grace"),
    ],
)
def test_validity_status_branches(days, prepaid, addon, expected):
    assert validity_status(days, prepaid, addon) == expected
