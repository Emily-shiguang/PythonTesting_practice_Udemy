# Any pytest file should start with test_
# pytest method names should start with test
# Any code should be wrapped in method body
# Every method is a test case
# You can mark (tag) tests @pytest.mark.smoke and then run with -m
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_secondCreditCard():
    a = 4
    b = 6
    assert a + 2 == b, "Addition do not match"

@pytest.fixture()
def setup():  # any name
    print("I will be executed first")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")

