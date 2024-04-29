n = int(input())
strings = input()
count = 0

for e in strings:
    if e in ["a", "i", "e", "o", "u"]:
        count += 1

print(count)
