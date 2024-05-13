str_num = input()
num = int(str_num)

result = str_num.find("7")

if result == -1:
    if num % 7 == 0:
        print(1)
    else:
        print(0)
else:
    if num % 7 == 0:
        print(3)
    else:
        print(2)
