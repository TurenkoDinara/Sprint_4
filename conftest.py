import pytest
from main import BooksCollector

@pytest.fixture
def collection():
    collection = BooksCollector()
    return collection