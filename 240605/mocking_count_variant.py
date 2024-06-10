import pytest
from count_variant import count_vartype
from unittest import mock


# open을 mocking
@mock.patch(
    "builtins.open",
    new_callable=mock.mock_open,
    read_data=(
        "##META\n"
        "#CHROM\tPOS\tID\tREF\tALT\n"
        "chr1\t100\t.\tA\tC\t\n"
        "chr1\t100\t.\tT\tG\t\n"
        "chr2\t100\t.\tAA\tA\t\n"
        "chr3\t100\t.\tA\tAAT\t\n"
        "chr3\t100\t.\tA\tAATG\t\n"
    ),
)
def test_count_vartype(mock_open):
    res = count_vartype("sample.vcf")
    assert res == {"snp": 2, "insertion": 2, "deletion": 1}
