'''
grouping tests:
--------------
test_LoginByEmail -> sanity , regression
test_LoginByFacebook -> sanity
test_LoginByPhone -> regression
test_signupByEmail -> sanity, regression
test_signupByFacebook -> regression
test_signupbyphone -> sanity
test_paymentindollor -> sanity, regression
test_paymentinrupees -> regression

'''

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_loginupbyEmail():
    print("This is test login by Email")
    assert True == True


@pytest.mark.sanity
def test_loginbyFacebook():
    print("This is test login by Facebook")
    assert True == True


@pytest.mark.regression
def test_loginbyPhone():
    print("This is test login by Phone")
    assert True == True


@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyEmail():
    print("This is test signup by Email")
    assert True == True


@pytest.mark.regression
def test_signupbyFacebook():
    print("This is test signup by Facebook")
    assert True == True


@pytest.mark.sanity
def test_signupbyPhone():
    print("This is test signup by Phone")
    assert True == True


@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindollor():
    print("This is test payment in Doller")
    assert True == True


@pytest.mark.regression
def test_paymentinrupees():
    print("This is test payment in Rupees")
    assert True == True
