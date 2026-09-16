import pytest

@pytest.fixture
def setup():
    print("Setup environment...")
    yield
    print("close browser")