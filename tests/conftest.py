import pytest

@pytest.fixture
def db():
    from phonygres import Database
    return Database()
