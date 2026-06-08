import pytest


@pytest.mark.smoke
def test_sample_one():
    print("Test1")


@pytest.mark.summa
def test_sample_on():
    print("Test2")


@pytest.mark.smoke
def test_sample_o():
    print("Test3")


@pytest.mark.summa
@pytest.mark.xfail(reason="Fail agu..")
def test_hello():
    print("Heloooo")


@pytest.mark.smoke
def test_random_text():
    print("vybhnj k")


@pytest.mark.parametrize("test_input,expected",[(1,3),(3,5),(5,7)])
def test_addition(test_input,expected):
    assert test_input + 2 == expected