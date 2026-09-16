import pytest


def test_loginupbyEmail():
    print("This is test login by Email")
    assert True == True

@pytest.mark.skip(reason="skipping it")
def test_loginbyFacebook():
    print("This is test login by Facebook")
    assert True == True

@pytest.mark.skip(reason="skipping it")
def test_loginbyPhone():
    print("This is test login by Phone")
    assert True == True


def test_signupbyEmail():
    print("This is test signup by Email")
    assert True == True

@pytest.mark.skip(reason="skipping it")
def test_signupbyFacebook():
    print("This is test signup by Facebook")
    assert True == True

@pytest.mark.skip(reason="skipping it")
def test_signupbyPhone():
    print("This is test signup by Phone")
    assert True == True
