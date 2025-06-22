import json
from unittest.mock import patch, MagicMock
import pytest


# Mock response for OpenAI API
MOCK_RESPONSE_CONTENT = {
    "risk_level": "Medium",
    "key_factors": ["elevated glucose", "family history"],
    "recommendations": ["consult doctor", "monitor blood sugar"]
}

@pytest.fixture(scope="function", autouse=True)
def mock_openai():
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