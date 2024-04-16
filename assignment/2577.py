v = list()
total = 0

for i in range(3):
    v.append(int(input()))

total = v[0] * v[1] * v[2]

d = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

for e in str(total):
    d[e] += 1

for i in range(10):
    print(d.get(str(i)))
