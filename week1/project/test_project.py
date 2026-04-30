import pytest
import project
from unittest.mock import patch


def test_validate():
    assert project.validate("abc") == "Invalid input"
    with pytest.raises(SystemExit):
        project.validate("x")
    with patch('project.get_news') as mock_news:
        project.validate("news")
        mock_news.assert_called_once()
    with patch('project.get_sports') as mock_sports:
        project.validate("sports")
        mock_sports.assert_called_once()
    with patch('project.get_quote') as mock_quote:
        project.validate("quote") 
        mock_quote.assert_called_once()

def test_get_news():
    ...


def test_get_sports():
    ...


def test_get_quote():
    ...