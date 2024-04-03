num = int(input())

# use string.rjust(len)

for i in range(num):
    string = "*" * (i + 1)
    print(string.rjust(num, " "))
