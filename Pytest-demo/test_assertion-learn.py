import pytest


@pytest.mark.smoke
def test_string_concat():
    assert "GH" + "gh" == "GHgh"
    print("String Concatenation Passed")

@pytest.mark.summa
@pytest.mark.skip(reason= "Summa thaa try pannikalam nu ")
def test_equal_assertion():
    x = 5
    y = 5
    assert x == y
    print("Equal (==) Assertion Passed")

@pytest.mark.smoke
def test_not_equal():
    assert 10 != 5
    print("Not Equal (!=) Assertion Passed")

@pytest.mark.summa
@pytest.mark.skip(reason= "Summa thaa try pannikalam nu ")
def test_greater_than():
    assert 10 > 5
    print("Greater Than (>) Assertion Passed")

@pytest.mark.smoke
def test_less_than():
    assert 5 < 10
    print("Less Than (<) Assertion Passed")

@pytest.mark.summa
@pytest.mark.skip(reason= "Summa thaa try pannikalam nu ")
def test_greater_or_equal():
    assert 10 >= 10
    assert 15 >= 10
    print("Greater or Equal (>=) Assertion Passed")
    

@pytest.mark.smoke
def test_less_or_equal():
    assert 5 <= 5
    assert 5 <= 10
    print("Less or Equal (<=) Assertion Passed")

@pytest.mark.summa
@pytest.mark.skip(reason= "Summa thaa try pannikalam nu ")
def test_in_operator():
    assert 10 in [5, 10, 15, 20]
    assert "a" in "apple"
    print("'in' Operator Assertion Passed")

@pytest.mark.smoke
def test_not_in_operator():
    assert 99 not in [5, 10, 15]
    assert "z" not in "apple"
    print("'not in' Operator Assertion Passed")

@pytest.mark.summa
@pytest.mark.skip(reason= "Summa thaa try pannikalam nu ")
def test_is_operator():
    a = [1, 2, 3]
    b = a
    assert a is b          
    print("'is' Operator Assertion Passed")

@pytest.mark.smoke
def test_is_not_operator():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert a is not b     
    print("'is not' Operator Assertion Passed")

@pytest.mark.summa
@pytest.mark.skip(reason= "Summa thaa try pannikalam nu ")
def test_assertion_with_message():
    assert 1 + 1 == 2, "Basic math should always work"
    print("Assertion with custom message Passed")