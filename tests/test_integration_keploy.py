"""Integration tests using VCR for API testing."""
from pprint import pprint
from textwrap import indent
import pytest
import vcr
import json

@my_vcr.use_cassette('tests/cassettes/test_diabetes_risk_assessment.yaml')
def test_diabetes_risk_assessment():
    from diabetes_diagnosis import get_risk
    
    test_patient = {
        "age": 45,
        "bmi": 28,
        "glucose_level": 110,
        "blood_pressure": "130/85",
        "cholesterol": "220",
        "family_history": True,
        "symptoms": ["increased thirst", "frequent urination"]
    }
    
    result = get_risk(test_patient)

    pprint(result, indent=2, width=80)

    response_data = json.loads(result["raw"])
    pprint(response_data, indent=2, width=80)

    assert "raw" in result
    assert "validation" in result
    assert "risk_level" in response_data
    assert "key_factors" in response_data
    assert "recommendations" in response_data
    assert result["validation"]["valid"] is True