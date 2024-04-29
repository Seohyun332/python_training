seq = ""
with open("./raw/test.fasta") as file:
    for line in file:
        if line.startswith(">"):
            continue

        seq += line.strip()  # enter del

print(len(seq))


print(f'A : {seq.count("A")}')
print(f'T : {seq.count("T")}')
print(f'G : {seq.count("G")}')
print(f'C : {seq.count("C")}')
# print("C : " + str(seq.count("C")))


### dict count ###

seq = ""
with open("./raw/test_aa.fasta") as file:
    for line in file:
        if line.startswith(">"):
            continue

        seq += line.strip()  # enter del

data = dict()

for aa in seq:
    if aa not in data:
        data[aa] = 0
    data[aa] += 1

print(data)
