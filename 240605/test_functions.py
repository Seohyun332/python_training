import pytest

from new_functions import f1330, add_number


def test_comp():  ## test_ 가 붙어 있어야 함 > pytest에서 해당 test 를 찾아냄
    assert f1330(1, 2) == "<"


@pytest.mark.parametrize(
    "arg1, arg2, exp",
    [
        (1, 2, "<"),
        (3, 1, ">"),
        (1, 1, "="),
    ],
)
def test_comp2(
    arg1, arg2, exp
):  ## test_ 가 붙어 있어야 함 > pytest에서 해당 test 를 찾아냄
    assert f1330(arg1, arg2) == exp


def test_number():
    assert add_number(1, 4) == 5
