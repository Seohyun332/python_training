import sys


def count_vartype(file_path):
    data = {"snp": 0, "insertion": 0, "deletion": 0}

    with open(file_path) as handle:
        for line in handle:
            if line.startswith("##"):
                continue
            if line.startswith("#"):
                header = line.strip().split("\t")

                ref_idx = header.index("REF")
                alt_idx = header.index("ALT")
                continue

            row = line.strip().split("\t")

            ref = row[ref_idx]
            alt = row[alt_idx]

            if len(ref) == 1 and len(alt) == 1:
                data["snp"] += 1
            elif len(ref) < len(alt):
                data["insertion"] += 1
            elif len(ref) > len(alt):
                data["deletion"] += 1

    return data
