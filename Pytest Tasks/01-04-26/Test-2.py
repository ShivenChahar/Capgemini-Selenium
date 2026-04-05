import pytest

@pytest.mark.regression
def test_reg1():
    assert 99>=29,"Not Greater Than"
@pytest.mark.regression
def test_reg2():
    assert True==True,"Not True"
@pytest.mark.smoke
def test_smoketest1():
    assert "Hello"=="Hello","Error Occurred"
@pytest.mark.smoke
def test_smoketest2():
    assert 55>=45,"not Greater Than"