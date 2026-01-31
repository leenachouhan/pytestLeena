import pytest

def test_Firstcase(setup):
    print("this is a first test case")
    assert setup == "pass"

def test_Secondcase(setup):
    print("this is a second test case")
    assert setup == "fail"

