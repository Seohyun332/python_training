import pytest
from p100 import add


def test_add():
    assert add(1, 2) == 3  # 1, 2를 add 한테 던져주었을 때 3이 나오는지 보기


def test_add2():
    assert add(3, 4) == 7
