"""Line coverage tests for mobile_data_plan.py (SRN PES2UG24AM205)."""

import pytest

from mobile_data_plan import (
    overage_charge,
    recharge_allowed,
    validity_status,
)


def test_overage_rejects_unknown_plan():
    with pytest.raises(ValueError, match="unknown plan"):
        overage_charge("ultra", 1, False, False)


def test_overage_rejects_negative_usage():
    with pytest.raises(ValueError, match="invalid data usage"):
        overage_charge("basic", -1, False, False)


def test_included_usage_and_loyalty_bonus_do_not_cost_extra():
    assert overage_charge("standard", 5, False, False) == 0
    assert overage_charge("basic", 3, False, True) == 0


def test_standard_non_roaming_overage():
    assert overage_charge("standard", 6, False, False) == 15


def test_roaming_overage():
    assert overage_charge("basic", 3, True, False) == 40


def test_large_non_roaming_overage_uses_high_usage_rate():
    assert overage_charge("basic", 13, False, False) == 275


def test_large_roaming_overage_uses_high_usage_rate():
    assert overage_charge("basic", 13, True, False) == 605


def test_kyc_recharge_limit():
    assert recharge_allowed(200, 9, True) is True
    assert recharge_allowed(201, 0, True) is False


def test_non_kyc_recharge_amount_and_pending_limits():
    assert recharge_allowed(2000, 2, False) is True
    assert recharge_allowed(2001, 0, False) is False
    assert recharge_allowed(2000, 3, False) is False


def test_validity_statuses():
    assert validity_status(0, True, False) == "active"
    assert validity_status(2, False, False) == "grace"
    assert validity_status(-13, False, False) == "expired"
    assert validity_status(5, False, True) == "active"
    assert validity_status(2, False, True) == "grace"
