import os, json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_diabetes_risk(patient_data):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    prompt = f"""Analyze this patient data and provide a diabetes risk assessment:
    {json.dumps(patient_data, indent=2)}
    
    Provide: 1) Risk level (Low/Medium/High) 2) Key risk factors 3) Recommendations"""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a medical assistant providing diabetes risk assessments"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    patient = {
        "age": 45, "bmi": 28.5, "glucose_level": 110,
        "family_history": "Father had type 2 diabetes",
        "symptoms": ["increased thirst", "frequent urination"],
        "blood_pressure": "130/85",
        "cholesterol": {"total": 210, "hdl": 45, "ldl": 130},
        "physical_activity": "sedentary"
    }
    
    print("\nDiabetes Risk Assessment:")
    print("=" * 40)
    print(get_diabetes_risk(patient))
