#Fixture : Reusable function

# scope="function"  fixture will be called before every test function executes
# scope="module"   fixture will be called only once before test functions executes
# scope="class"   fixture will be called only once before the class
# scope="session"  fixture will be called only once for session

# module --> class --> methods
# module --> function


import pytest

@pytest.fixture
def setup(scope="module" ):
    print("Setup Browser")

def test_demo(setup):
    print("This is test one")

def test_demo2(setup):
    print("This is test two")

def test_demo3(setup):
    print("This is test Three")

