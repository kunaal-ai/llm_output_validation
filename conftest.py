import os
import json
from unittest.mock import patch, MagicMock
import pytest


# Mock response for OpenAI API
MOCK_RESPONSE_CONTENT = {
    "risk_level": "Medium",
    "key_factors": ["elevated glucose", "family history"],
    "recommendations": ["consult doctor", "monitor blood sugar"]
}

def pytest_addoption(parser):
    parser.addoption(
        "--use-mock",
        action="store_true",
        default=False,
        help="use mock not real API"
    )

@pytest.fixture(scope="function", autouse=True)
def mock_openai(request):
    # get terminal input
    mock_terminal_cmd = request.config.getoption("--use-mock")
    # get env value
    mock_env_value = os.getenv("USE_MOCK", "true").lower() == 'true'
    # use which ever available
    use_mock = mock_terminal_cmd or mock_env_value

    if use_mock:
        with patch('diabetes_diagnosis.OpenAI') as mock_client:
            # mock for the response object
            mock_response = MagicMock()
            
            # mock for the message object
            mock_message = MagicMock()
            mock_message.content = json.dumps(MOCK_RESPONSE_CONTENT)
            
            # mock for the choice object
            mock_choice = MagicMock()
            mock_choice.message = mock_message
            
            # Set up the response structure
            mock_response.choices = [mock_choice]
            
            # Configure the mock client to return our mock response
            mock_instance = MagicMock()
            mock_instance.chat.completions.create.return_value = mock_response
            mock_client.return_value = mock_instance
            
            yield mock_instance
    else:
        yield