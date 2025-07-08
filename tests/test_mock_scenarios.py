"""Tests for the mock OpenAI API scenarios."""
import json
import pytest
from diabetes_diagnosis import get_risk

# Test data
TEST_PATIENT = {
    "age": 45,
    "bmi": 28,
    "glucose_level": 110,
    "blood_pressure": "130/85",
    "cholesterol": "220",
    "family_history": True,
    "symptoms": ["increased thirst", "frequent urination"]
}

@pytest.fixture
def test_patient():
    return TEST_PATIENT.copy()

@pytest.fixture
def get_risk_fix(test_patient):
    return get_risk(test_patient)

def test_success_scenario(success_mock, get_risk_fix):
    result = get_risk_fix    
    assert "raw" in result
    assert "validation" in result
    
    # Parse the raw response
    data = json.loads(result["raw"])
    assert "risk_level" in data
    assert "key_factors" in data
    assert "recommendations" in data

def test_rate_limit_scenario(rate_limit_mock, test_patient):
    # The function now returns a structured error response instead of raising an exception
    result = get_risk(test_patient)
    assert not result["validation"]["valid"]
    assert "Rate limit exceeded" in result["validation"].get("error", "")

def test_partial_response_scenario(partial_mock, get_risk_fix):
    result = get_risk_fix
    assert "raw" in result
    assert "validation" in result
    data = json.loads(result["raw"])
    assert data.get("incomplete") is True

def test_invalid_json_scenario(invalid_json_mock, get_risk_fix):
    result = get_risk_fix   
    assert "raw" in result
    assert "validation" in result
    # Should contain the raw string since it's not valid JSON
    assert result["raw"] == "This is not valid JSON"
