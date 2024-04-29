file = open("./raw/test.txt")
for line in file:
    print(line)

file.close()

file = open("./raw/test.txt")
for line in file:
    print(line.strip())

file.close()

with open("./raw/test.txt") as file:
    for line in file:
        print(line.strip())

sum = 0
for i in range(10):
    sum += i + 1

print(sum)
