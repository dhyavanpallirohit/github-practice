import pytest
import os
import sys
import subprocess

from risk_check import check_risk


def test_high_risk():
    assert check_risk(85) == "High Risk"


def test_low_risk():
    assert check_risk(50) == "Low Risk"


def test_invalid_high_score():
    with pytest.raises(ValueError):
        check_risk(150)


def test_invalid_negative_score():
    with pytest.raises(ValueError):
        check_risk(-10)

def test_default_risk_threshold():
    env = os.environ.copy()
    env.pop("RISK_THRESHOLD", None)

    result = subprocess.check_output(
        [
            sys.executable,
            "-c",
            "from risk_check import check_risk; "
            "print(check_risk(85))"
        ],
        env=env,
        text=True
    ).strip()

    assert result == "High Risk"


def test_custom_risk_threshold():
    env = os.environ.copy()
    env["RISK_THRESHOLD"] = "90"

    result = subprocess.check_output(
        [
            sys.executable,
            "-c",
            "from risk_check import check_risk; "
            "print(check_risk(85))"
        ],
        env=env,
        text=True
    ).strip()

    assert result == "Low Risk"