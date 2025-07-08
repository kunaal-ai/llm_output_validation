# Diabetes Diagnosis with LLM - Technical Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Core Components](#core-components)
   - [Diabetes Diagnosis Module](#diabetes-diagnosis-module)
   - [Validation System](#validation-system)
   - [Testing Framework](#testing-framework)
4. [Tools and Dependencies](#tools-and-dependencies)
5. [Workflow](#workflow)
6. [Error Handling](#error-handling)
7. [Extending the Project](#extending-the-project)

## Project Overview

This project provides a structured approach to diabetes risk assessment using OpenAI's language models. It processes patient data, generates risk assessments, and validates the output to ensure reliability and consistency.

## System Architecture

```
├── diabetes_diagnosis.py   # Main module with core functionality
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py         # Test configuration
│   ├── test_edge_cases.py  # Edge case tests
│   └── test_validation.py  # Validation tests
├── scripts/
│   └── run_tests.sh       # Test runner script
├── requirements.txt        # Python dependencies
└── .env.example           # Environment template
```

## Core Components

### Diabetes Diagnosis Module

Located in `diabetes_diagnosis.py`, this module contains:

1. **Assessment Model** (`Assessment` class):
   - Defines the structure for risk assessments
   - Uses Pydantic for data validation
   - Enforces required fields and data types

2. **Risk Assessment Function** (`get_risk`):
   - Takes patient data as input
   - Communicates with OpenAI's API
   - Returns structured risk assessment

### Validation System

1. **Response Validation** (`validate_response`):
   - Validates JSON structure
   - Ensures all required fields are present
   - Validates data types and constraints

2. **Error Handling**:
   - Catches and reports JSON parsing errors
   - Validates against the Assessment model
   - Provides clear error messages

### Testing Framework

1. **Test Types**:
   - Unit tests for individual components
   - Integration tests for API interactions
   - Edge case testing

2. **Mocking**:
   - Uses `pytest-mock` for API call mocking
   - Prevents unnecessary API calls during testing
   - Ensures consistent test results

## Tools and Dependencies

### Core Dependencies

- **Python 3.8+**: Core programming language
- **Pydantic**: Data validation and settings management
- **OpenAI Python Client**: Interface with OpenAI's API
- **python-dotenv**: Environment variable management
- **pytest**: Testing framework

### Development Tools

- **pytest-mock**: Mocking for tests
- **pytest-html**: HTML test reporting
- **black**: Code formatting
- **flake8**: Linting
- **mypy**: Static type checking

## Workflow

1. **Input Processing**:
   - Patient data is collected and formatted
   - Data is validated for required fields

2. **API Interaction**:
   - Request is sent to OpenAI's API
   - Response is captured and parsed

3. **Response Validation**:
   - JSON structure is validated
   - Data types and constraints are checked
   - Results are formatted for output

4. **Result Handling**:
   - Valid results are processed
   - Errors are caught and reported
   - Logs are generated for debugging

## Error Handling

The system implements robust error handling:

1. **Input Validation**:
   - Checks for required fields
   - Validates data types and formats
   - Provides clear error messages

2. **API Error Handling**:
   - Handles network issues
   - Manages API rate limits
   - Processes API-specific errors

3. **Response Validation**:
   - Validates JSON structure
   - Checks for required fields
   - Ensures data consistency

## Extending the Project

### Adding New Fields

To add new fields to the assessment model:

1. Update the `Assessment` class in `diabetes_diagnosis.py`
2. Add validation rules as needed
3. Update the test suite to cover new fields

### Customizing Validation

To modify validation rules:

1. Edit the `validate_response` function
2. Add new validation rules to the `Assessment` class
3. Update tests to verify new validation rules

### Adding Tests

To add new tests:

1. Create test cases in the `tests/` directory
2. Use the existing test fixtures
3. Follow the pattern of existing tests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `bash scripts/run_tests.sh`
5. Submit a pull request

## License

[Specify your license here]

---

For setup and installation instructions, please refer to [README.md](README.md).
