import pytest

@pytest.mark.xfail
def test_first():
    print("Hello")

@pytest.mark.smoke
@pytest.mark.skip
def test_world():
    print("World")
