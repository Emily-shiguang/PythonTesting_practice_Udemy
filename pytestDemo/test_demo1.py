# Any pytest file should start with test_
# pytest method names should start with test
# Any code should be wrapped in method body
# Every method is a test case
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_secondGreetCreditCard():
    print("Good Morning")

def test_crossBroswer(crossBrower):
    print(crossBrower)
    # print(crossBrower[1])