#Fixture : Reusable function

import pytest

@pytest.fixture
def setup():
    print("Setup Browser")
    return "Chrome"

def test_demo(setup):
    print("This is test one")
    print("Browser is", setup)

def test_demo2(setup):
    print("This is test two")
    print("Browser is", setup)

def test_demo3(setup):
    print("This is test Three")
    print("Browser is", setup)

