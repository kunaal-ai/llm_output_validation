"""Tests for diabetes diagnosis validation."""
import json
import pytest
from diabetes_diagnosis import validate, validate_llm_output

# Test data
VALID_LLM_OUTPUT = {
    "risk_level": "Medium",
    "key_factors": ["elevated glucose", "family history"],
    "recommendations": ["consult doctor", "monitor blood sugar"]
}

def test_validate_with_valid_data():
    """Test validation with correct data format."""
    result = validate(json.dumps(VALID_LLM_OUTPUT))
    assert result["valid"] is True
    assert result["data"]["risk_level"] == "Medium"

def test_validate_missing_fields():
    """Test validation with missing required fields."""
    invalid = VALID_LLM_OUTPUT.copy()
    invalid.pop("risk_level")
    result = validate(json.dumps(invalid))
    assert result["valid"] is False
    assert "missing" in result["error"].lower()

def test_validate_invalid_risk_level():
    """Test validation with invalid risk level."""
    invalid = VALID_LLM_OUTPUT.copy()
    invalid["risk_level"] = "Very High"
    result = validate(json.dumps(invalid))
    assert result["valid"] is False
    assert "risk_level" in result["error"]

def test_validate_empty_lists():
    """Test validation with empty lists."""
    invalid = VALID_LLM_OUTPUT.copy()
    invalid["key_factors"] = []
    result = validate(json.dumps(invalid))
    assert result["valid"] is False
    assert "key_factors" in result["error"]