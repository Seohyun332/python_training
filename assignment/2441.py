num = int(input())

# use string.rjust(len)

for i in range(num):
    string = "*" * (num - i)
    print(string.rjust(num, " "))
