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

3. Set up your OpenAI API key:
   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

## Testing

### Mock vs Real API

The test suite includes a mock for the OpenAI API to avoid making real API calls during testing. This is the default behavior.

#### Running Tests with Mocks (Default)

```bash
# Using the test script (recommended)
bash scripts/run_tests.sh

# Or directly with pytest
pytest tests/
```

#### Running Tests with Real API

If you want to run tests against the real OpenAI API (not recommended for normal testing):

```bash
# Using environment variable
USE_MOCK=false pytest tests/

# Or using command line flag
pytest tests/ --use-mock=false
```

## Requirements

- Python 3.6+
- OpenAI API key