import pytest
from unittest.mock import patch, MagicMock
from src.metadata_crawler import fetch_arxiv_data

@pytest.fixture
def mock_requests_get():
    with patch('metadata_crawler.requests.get') as mock_get:
        yield mock_get

def test_fetch_arxiv_data_success(mock_requests_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = 'Mocked XML response'
    mock_requests_get.return_value = mock_response

    result = fetch_arxiv_data(0, 10)

    assert result is not None

def test_fetch_arxiv_data_failure(mock_requests_get):
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_requests_get.return_value = mock_response

    result = fetch_arxiv_data(0, 10)

    assert result is None

