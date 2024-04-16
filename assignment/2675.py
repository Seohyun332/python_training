n = int(input())

out_list = list()

for i in range(n):
    string = input().split()

    number = int(string[0])

    newstring = []

    for e in string[1]:
        newstring.append(e * number)

    out_list.append("".join(newstring))

for e in out_list:
    print(e)
