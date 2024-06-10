def f1330(a: int, b: int):
    if a > b:
        return ">"
    elif a < b:
        return "<"
    elif a == b:
        return "="


def add_number(num1: int, num2: int):
    return num1 + num2


from Bio import SeqIO
import os
import sys


def count_base_from_fasta(file_path):
    if not os.path.isfile(file_path):  # 파일 존재 여부 검사
        print("# ERROR : file does not exist.")
        sys.exit()

    recode = SeqIO.read(file_path, "fasta")

    count = dict()

    for base in recode.seq:
        if base not in count:
            count[base] = 0
        count[base] += 1

    return count
