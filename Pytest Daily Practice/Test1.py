'''
Pytest Markers => Markers in pytest are used to categorize, control, and selectively run tests.
@pytest.mark.skip => Used to unconditionally skip a test, The test will never execute. (@pytest.mark.skip(reason="Feature not implemented"))
@pytest.mark.skipif => Used to conditionally skip a test based on a condition, Test is skipped only if the condition is True...
...,Useful for OS, Python version, or environment-based conditions.(@pytest.mark.skipif(condition, reason="Explain why")).
Parametrize → runs the same test with multiple input combinations automatically
'''
import pytest
def test_change():
    assert "hello" == "hello", 'Not Equal'
    assert 6 == 6 , "Not Equal"

@pytest.mark.smoke                            # To Run Smoke Marker : pytest Test1.py -vs -m "smoke"
def test_comparison():
    assert 45 >= 44 , "Not Greater"

@pytest.mark.smoke
def test_membership():
    t = (1,2,3)

    assert 3 in t , "Not in the Tuple"

@pytest.mark.skip                         # To Run Skip Marker : pytest Test1.py -vs -m skip
def test_skip():
    assert True == False , "Not True"

x = 5
@pytest.mark.skipif(x > 3, reason = "x is greater than 3")
def test_greater_than():
    assert True

@pytest.mark.parametrize("a,b,c", [(1,2,3),(4,5,6),(7,8,9)])           # TO Run this marker : pytest Test1.py -vs
def test_addition(a,b,c):
    d = a + b + c
    print(d)