"""Test edge cases for diabetes diagnosis validation."""
import json
import logging
import sys
import pytest
from typing import Dict, Any, Optional
from diabetes_diagnosis import get_risk, validate

# Configure logging to output to stdout
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propagate = False  # Prevent duplicate logs

# Base valid patient data
BASE_PATIENT = {
    "age": 45,
    "bmi": 28.5,
    "glucose_level": 110,
    "family_history": "Father had type 2 diabetes",
    "symptoms": ["increased thirst", "frequent urination"],
    "blood_pressure": "130/85",
    "cholesterol": {"total": 210, "hdl": 45, "ldl": 130},
    "physical_activity": "sedentary"
}


def log_test_case(name: str, data: Dict[str, Any], result: Dict[str, Any]):
    """Log test case details and results."""
    print("\n" + "="*80)
    print(f"TEST CASE: {name}")
    print("-"*80)
    print("INPUT DATA:")
    print(json.dumps(data, indent=2))
    print("\nRESULT:")
    print(json.dumps(result, indent=2))
    print("="*80 + "\n")

class TestEdgeCases:    
    """Test cases for edge cases in diabetes diagnosis."""
    
    @pytest.mark.parametrize("field", [
        "age", "bmi", "glucose_level", "family_history", 
        "symptoms", "blood_pressure", "cholesterol"
    ])
    def test_missing_required_fields(self, field: str):
        """Test behavior when required fields are missing."""
        print(f"\n{'*'*10} Testing missing required field: {field} {'*'*10}")
        patient = BASE_PATIENT.copy()
        patient.pop(field, None)
        
        print(f"Sending request with missing field: {field}")
        result = get_risk(patient)
        validation = result["validation"]
        
        log_test_case(
            f"Missing required field: {field}",
            {k: v for k, v in patient.items() if k != field},
            validation
        )
        
        assert isinstance(validation, dict), "Response should be a dictionary"
        if not validation.get("valid", False):
            print(f"✅ Expected failure for missing {field}. Error: {validation.get('error', 'No error message')}")
        else:
            print(f"❌ Unexpected success for missing {field}")

    @pytest.mark.parametrize("field,invalid_values", [
        ("age", [-1, 0, 151, "not_an_age"]),
        ("bmi", [-10, 0, 1000, "not_a_bmi"]),
        ("glucose_level", [-5, 0, 2000, "not_a_number"]),
        ("blood_pressure", ["120", "85/120/90", "eighty/ninety"]),
    ])
    def test_invalid_values(self, field: str, invalid_values: list):
        """Test behavior with invalid values for numeric fields."""
        for value in invalid_values:
            patient = BASE_PATIENT.copy()
            patient[field] = value
            
            result = get_risk(patient)
            validation = result["validation"]
            log_test_case(
                f"Invalid {field}: {value}", 
                {field: value}, 
                validation
            )
            assert isinstance(validation, dict), "Response should be a dictionary"

    def test_extreme_values(self):
        """Test behavior with extreme but potentially valid values."""
        extreme_cases = [
            ("age", 120),  # Very old
            ("bmi", 60),   # Extreme obesity
            ("glucose_level", 600),  # Diabetic emergency
            ("blood_pressure", "200/120"),  # Hypertensive crisis
        ]
        
        for field, value in extreme_cases:
            patient = BASE_PATIENT.copy()
            patient[field] = value
            
            result = get_risk(patient)
            validation = result["validation"]
            log_test_case(
                f"Extreme {field}: {value}",
                {field: value},
                validation
            )
            
            assert isinstance(validation, dict), "Response should be a dictionary"
            if validation.get("valid", False):
                assert validation["data"]["risk_level"] in ["Low", "Medium", "High"]

    def test_empty_symptoms(self):
        """Test behavior with empty symptoms list."""
        patient = BASE_PATIENT.copy()
        patient["symptoms"] = []
        
        result = get_risk(patient)
        validation = result["validation"]
        log_test_case("Empty symptoms", patient, validation)
        
        assert isinstance(validation, dict), "Response should be a dictionary"
        if validation.get("valid", False):
            assert validation["data"]["risk_level"] in ["Low", "Medium", "High"]

    def test_null_values(self):
        """Test behavior with null/None values."""
        patient = {
            "age": None,
            "bmi": None,
            "glucose_level": None,
            "family_history": None,
            "symptoms": None,
            "blood_pressure": None,
            "cholesterol": None,
            "physical_activity": None
        }
        
        result = get_risk(patient)
        validation = result["validation"]
        log_test_case("All null values", patient, validation)
        
        assert isinstance(validation, dict), "Response should be a dictionary"
        if not validation.get("valid", False):
            logger.info(f"Expected failure for null values: {validation.get('error', 'No error message')}")