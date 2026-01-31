import pytest

@pytest.fixture(scope="module")
def setup():
    print("hello...this is a setup fixture")
    yield
    print("hello.. this is tear down")