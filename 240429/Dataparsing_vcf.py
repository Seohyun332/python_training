### gzip read code
import gzip

with gzip.open("./raw/test.txt.gz", "rt") as file:
    for line in file:
        print(line.strip())


# but cd command need
## cd .\python_training\240429
## python .\Dataparsing_vcf.py

### read VCF file
count_row = 0
with gzip.open("./raw/sample.ann.vcf.gz", "rt") as file:
    for line in file:
        if line.startswith("#"):
            continue
        count_row += 1

print("Data counts : ", count_row)


### only Qual > 1000 data

count_row = 0
with gzip.open("./raw/sample.ann.vcf.gz", "rt") as file:
    for line in file:
        if line.startswith("#"):
            continue

        qual = float(line.strip().split("\t")[5])
        if qual >= 1000:
            count_row += 1

print("Qual 1000 Data counts : ", count_row)


### header

with gzip.open("./raw/sample.ann.vcf.gz", "rt") as file:
    for line in file:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.strip().split("\t")
            continue

print("Header : ", header)
print(header.index("QUAL"))


### 범용성 up

count_row = 0
idx = 0
with gzip.open("./raw/sample.ann.vcf.gz", "rt") as file:
    for line in file:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.strip().split("\t")
            idx = header.index("QUAL")
            continue

        qual = float(line.strip().split("\t")[idx])
        if qual >= 1000:
            count_row += 1

print("Qual 1000 Data counts : ", count_row)


### ts/tv ratio

ts = 0
tv = 0

base = {"A": "purines", "T": "pyrimidines", "G": "purines", "C": "pyrimidines"}
with gzip.open("./raw/sample.ann.vcf.gz", "rt") as file:
    for line in file:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.strip().split("\t")
            ref_idx = header.index("REF")
            alt_idx = header.index("ALT")
            continue

        ref = line.strip().split("\t")[ref_idx]
        alt = line.strip().split("\t")[alt_idx]

        if len(ref) != 1 or len(alt) != 1:
            continue
        else:
            if base[ref] == base[alt]:
                ts += 1
            elif base[ref] != base[alt]:
                tv += 1


print(f"ts/tv ratio: {round(ts/tv, 4)}")

### counting genetype

counts = dict()

with gzip.open("./raw/sample.ann.vcf.gz", "rt") as file:
    for line in file:
        if line.startswith("##"):
            continue

        if line.startswith("#"):
            header = line.strip().split("\t")
            format_idx = header.index("FORMAT")
            sample_idx = header.index("sample")
            continue

        format = line.strip().split("\t")[format_idx]
        sample = line.strip().split("\t")[sample_idx]

        GT_idx = format.split(":").index("GT")

        target = sample.split(":")[GT_idx].replace("|", "/")

        if target not in counts:
            counts[target] = 0  ## 초기화
        counts[target] += 1

print(counts)
