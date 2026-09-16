#Fixture : Reusable function

import pytest

@pytest.fixture
def setup():
    print("Setup Browser")
    yield
    print("close browser")

def test_demo(setup):
    print("This is test one")

def test_demo2(setup):
    print("This is test two")

def test_demo3(setup):
    print("This is test Three")

