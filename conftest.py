"""Test configuration with mock OpenAI API scenarios."""
import json
from unittest.mock import patch, MagicMock
import pytest

# Mock response templates
MOCK_RESPONSES = {
    "success": {
        "risk_level": "Medium",
        "key_factors": ["elevated glucose", "family history"],
        "recommendations": ["consult doctor", "monitor blood sugar"]
    },
    "partial": {
        "incomplete": True,
        "risk_level": "Medium",
        "key_factors": ["elevated glucose"],
        "recommendations": ["consult doctor"]
    }
}

def create_mock_response(content, is_raw_string=False):
    """Helper to create a mock response with the given content."""
    mock_response = MagicMock()
    mock_choice = MagicMock()
    mock_message = MagicMock()
    
    if is_raw_string:
        mock_message.content = content
    else:
        mock_message.content = json.dumps(content, indent=2)
    mock_choice.message = mock_message
    mock_response.choices = [mock_choice]
    return mock_response

@pytest.fixture
def mock_openai():
    """Base fixture to mock the OpenAI client."""
    with patch('diabetes_diagnosis.OpenAI') as mock_client:
        yield mock_client

@pytest.fixture
def success_mock(mock_openai):
    content = MOCK_RESPONSES["success"]
    mock_response = create_mock_response(content)
    mock_openai.return_value.chat.completions.create.return_value = mock_response
    return mock_openai

@pytest.fixture
def rate_limit_mock(mock_openai):
    """Mock for rate limit error."""
    mock_openai.return_value.chat.completions.create.side_effect = Exception(
        "OpenAI API Error: Rate limit exceeded (type: rate_limit_error)"
    )
    return mock_openai

@pytest.fixture
def partial_mock(mock_openai):
    """Mock for partial response."""
    content = MOCK_RESPONSES["partial"]
    mock_response = create_mock_response(content)
    mock_openai.return_value.chat.completions.create.return_value = mock_response
    return mock_openai

@pytest.fixture
def invalid_json_mock(mock_openai):
    """Mock for invalid JSON response."""
    mock_response = create_mock_response(
        "This is not valid JSON", 
        is_raw_string=True
    )
    mock_openai.return_value.chat.completions.create.return_value = mock_response
    return mock_openai