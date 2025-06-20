import os, json
from typing import Literal
from pydantic import BaseModel, Field, field_validator
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Assessment(BaseModel):
    """Structured diabetes risk assessment from LLM output."""
    risk_level: Literal['Low', 'Medium', 'High'] = Field(
        ...,
        description="Risk level must be one of: 'Low', 'Medium', or 'High'"
    )
    key_factors: list[str] = Field(
        ...,
        min_length=1,
        description="At least one key factor must be provided"
    )
    recommendations: list[str] = Field(
        ...,
        min_length=1,
        description="At least one recommendation must be provided"
    )

    @field_validator('key_factors', 'recommendations')
    @classmethod
    def check_non_empty_strings(cls, v):
        """Ensure all strings in the list are non-empty."""
        if not all(isinstance(item, str) and item.strip() for item in v):
            raise ValueError("All items must be non-empty strings")
        return v

def validate(text):
    """Validate the LLM output against the Assessment model."""
    try:
        data = json.loads(text)
        assessment = Assessment.model_validate(data)
        return {"valid": True, "data": assessment.model_dump()}
    except json.JSONDecodeError as e:
        return {"valid": False, "error": f"Invalid JSON: {str(e)}"}
    except Exception as e:
        return {"valid": False, "error": f"Validation error: {str(e)}"}

def get_risk(patient):
    """Get diabetes risk assessment from LLM."""
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    prompt = f"""Analyze this patient data and return a JSON object with these exact fields:
    - risk_level: Must be one of 'Low', 'Medium', or 'High'
    - key_factors: List of at least one string describing risk factors
    - recommendations: List of at least one recommended action

    Example valid response:
    {{
        "risk_level": "Medium",
        "key_factors": ["elevated glucose", "family history"],
        "recommendations": ["consult doctor", "monitor blood sugar"]
    }}

    Patient Data: {json.dumps(patient, indent=2)}
    
    Return ONLY the JSON object with no additional text."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a medical assistant providing structured diabetes risk assessments in JSON format"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        response_format={"type": "json_object"}
    )
    
    result = response.choices[0].message.content
    return {"raw": result, "validation": validate(result)}

if __name__ == "__main__":
    patient = {
        "age": 45, "bmi": 28.5, "glucose_level": 110,
        "family_history": "Father had type 2 diabetes",
        "symptoms": ["increased thirst", "frequent urination"],
        "blood_pressure": "130/85",
        "cholesterol": {"total": 210, "hdl": 45, "ldl": 130},
        "physical_activity": "sedentary"
    }
    
    result = get_risk(patient)
    print("\nValidation Result:")
    print("=" * 40)
    if result["validation"]["valid"]:
        print(" Valid assessment:")
        print(json.dumps(result["validation"]["data"], indent=2))
    else:
        print(" Invalid assessment:")
        print(result["validation"]["error"])
        print("\nRaw LLM response:")
        print("-" * 40)
        print(result["raw"])
