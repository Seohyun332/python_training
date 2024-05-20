seq = ""
with open("./rosalind_dna.txt") as file:
    for line in file:
        seq += line.strip()

print(seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T"))
