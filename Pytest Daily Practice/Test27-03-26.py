# def test_testEquality():
    # assert 4 == 5, 'Oops!'
    # assert 'Hello' != 'Hiii', 'Wowwee!'
    # assert 'Hello' == 'Hiii', 'Oops!'

# def test_comparison():
#     assert 4 < 5, "Oops!"

def test_membership():
    assert 4 in (1,2,3,4,5,6), "Oops!"
    assert 8 not in (1,2,3,4,5,6), "Oops!"
