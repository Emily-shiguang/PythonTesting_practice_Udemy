import pytest

@pytest.fixture(scope="class")
def setup():  # any name
    print("I will be executed first")
    yield # whatever you write after yield, it will be executed last
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Emily", "Du", "I am happy"]

@pytest.fixture(params=[("chrome", "emily1", "du"), ("Firefox", "emily2"), ("IE", "emily3")])
def crossBrower(request):
    return request.param