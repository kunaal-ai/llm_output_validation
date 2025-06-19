# Diabetes Diagnosis with LLM

A simple Python script that uses OpenAI's GPT-3.5 model to provide diabetes risk assessments based on patient data.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Edit the `example_patient` dictionary in `diabetes_diagnosis.py` with the patient's data.
2. Run the script:
   ```bash
   python diabetes_diagnosis.py
   ```

## Example Output

The script will output a diabetes risk assessment based on the provided patient data, including:
- Risk level (Low/Medium/High)
- Key factors contributing to the risk
- Recommended next steps

## Requirements

- Python 3.6+
- OpenAI API key