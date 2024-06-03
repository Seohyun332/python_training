import pytest


def test_function():
    assert (1, 2, 3) == (1, 2, 3)


# def test_function2():
#     assert (2, 3, 4) == (2, 1, 4)


## False test

from TDD import add, base_counter


def test_add():
    exp = 5
    assert add(2, 3) == exp


def test_base():
    seq = "AATCG"
    result = {"A": 2, "T": 1, "C": 1, "G": 1}
    assert base_counter(seq) == result


## 옳은 답을 정확히 기재하는 것
# 실수한 function의 결과를 그대로 담을 경우 > 정확하지 않을 수 있음


@pytest.mark.parametrize(("a", "b", "expected"), [(2, 4, 6), (6, 9, 15), (28, 1, 29)])
def test_add2(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "seq, dic",
    [
        ("AATC", {"A": 2, "T": 1, "C": 1}),
        ("AAAAGTCGTCC", {"A": 4, "T": 2, "G": 2, "C": 3}),
    ],
)
def test_base2(seq, dic):
    assert base_counter(seq) == dic
