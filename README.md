# Diabetes Risk Assessment with LLM

A Python application that provides structured diabetes risk assessments using OpenAI's language models. The application processes patient data, generates risk assessments, and validates the output to ensure reliability and consistency.

## Features

- Structured diabetes risk assessment using OpenAI's GPT models
- Input validation using Pydantic models
- Comprehensive test suite with unit and integration tests
- Mock-based testing to avoid real API calls during development
- Type hints and static type checking with mypy
- Code formatting with Black and isort

## Prerequisites

- Python 3.10 or higher
- OpenAI API key
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/llm_output_validation.git
   cd llm_output_validation
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

## Usage

```python
from diabetes_diagnosis import get_risk

patient_data = {
    "age": 45,
    "bmi": 28.5,
    "glucose_level": 110,
    "family_history": "Father had type 2 diabetes",
    "symptoms": ["increased thirst", "frequent urination"],
    "blood_pressure": "130/85",
    "cholesterol": {"total": 210, "hdl": 45, "ldl": 130},
    "physical_activity": "sedentary"
}

result = get_risk(patient_data)
print(result)
```

## Testing

The test suite includes unit tests and integration tests with mocked API responses.

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=diabetes_diagnosis tests/

# Generate HTML coverage report
pytest --cov=diabetes_diagnosis --cov-report=html tests/
```

### Test Structure

- `tests/test_diabetes.py`: Core functionality tests
- `tests/test_edge_cases.py`: Edge case validation tests
- `tests/test_mock_scenarios.py`: Mocked API response tests

## Development

### Code Style

The project uses:
- Black for code formatting
- isort for import sorting
- mypy for static type checking

### Development Workflow

1. Create a feature branch
2. Make your changes
3. Run tests and checks:
   ```bash
   black .
   isort .
   mypy .
   pytest
   ```
4. Commit your changes with a descriptive message
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Requirements

- Python 3.6+
- OpenAI API key