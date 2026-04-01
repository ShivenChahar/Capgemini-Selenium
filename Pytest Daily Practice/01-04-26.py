import pytest

def test_change():
    assert "hello" == "hello", 'Not Equal'
    assert 6 == 6 , "Not Equal"

def test_comparison():
    assert 45 >= 44 , "Not Greater"

@pytest.mark.shiven
def test_membership():
    t = (1,2,3)

    assert 3 in t , "Not in the Tuple"