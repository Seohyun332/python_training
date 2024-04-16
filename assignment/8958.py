n = int(input())
output_list = list()

for i in range(n):
    num = 0
    string = input()
    string = string.replace("X", " ")
    for e in string.split():
        le = len(e)
        num = num + (le * (le + 1)) / 2

    output_list.append(int(num))

for e in output_list:
    print(e)
