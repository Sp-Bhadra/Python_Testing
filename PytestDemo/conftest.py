import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed 1st")
    yield
    print("I will be executed last")


@pytest.fixture()
def loadData():
    print("retun Data")
    return ["Rahul", "Shetty", "Rahul.com"]
@pytest.fixture(params=[("Chrome","Rahul"), ("Firefox", "Shetty"), ("IE","SS")])
def crossBrowser(request):
    return request.param
