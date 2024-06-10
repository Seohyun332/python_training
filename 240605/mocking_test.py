import pytest
import new_functions

from unittest.mock import patch


@patch("new_functions.add_number")  # mocking 할 함수 설정 (가짜를 만드는 것이 mocking )
def test_add_number(mock_add):
    mock_add.return_value = (
        11  # 함수에서 나오는 값을 덮어씌우기 (이 함수의 정답값이 11로 설정됨)
    )
    exp = 10

    assert new_functions.add_number(3, 7) == exp


# def test_count_base_from_fasta():
#     exp = {}

#     assert new_functions.count_base_from_fasta("mock.fasta") == exp

## system error!! file 존재 안함

from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


@patch("os.path.isfile")  # 2번째 인자
@patch("new_functions.SeqIO.read")  # 1번째 인자
def test_count_base_from_fasta(mock_seqio, mock_isfile):
    # mocking 2
    mock_isfile.return_value = True
    mock_seqio.return_value = SeqRecord(Seq("AAC"))
    exp = {"A": 2, "C": 1}

    assert new_functions.count_base_from_fasta("mock.fasta") == exp

    mock_seqio.assert_called_once_with("mock.fasta", "fasta")
