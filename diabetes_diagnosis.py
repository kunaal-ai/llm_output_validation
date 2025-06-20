import os, json
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Assessment(BaseModel):
    risk_level: str
    key_factors: list
    recommendations: list

def validate(text):
    data = json.loads(text)
    return {"valid": True, "data": Assessment(**data).model_dump()}

def get_risk(patient):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    prompt = f"""Analyze this patient data and return a JSON object with:
    - risk_level: 'Low', 'Medium', or 'High'
    - key_factors: list of strings
    - recommendations: list of strings

    Patient Data: {json.dumps(patient, indent=2)}
    
    Return only the JSON object."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Provide diabetes risk assessment in JSON format"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        response_format={"type": "json_object"}
    )
    print(response.choices[0])
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
    print("\nAssessment:")
    print("=" * 40)
    print(json.dumps(result["validation"]["data"], indent=2))
