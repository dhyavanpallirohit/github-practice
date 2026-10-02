import pytest

from risk_check import check_risk


def test_high_risk():
    assert check_risk(85) == "High Risk"


def test_low_risk():
    assert check_risk(50) == "High Risk"


def test_invalid_high_score():
    with pytest.raises(ValueError):
        check_risk(150)


def test_invalid_negative_score():
    with pytest.raises(ValueError):
        check_risk(-10)