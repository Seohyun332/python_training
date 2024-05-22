def gugudan(num):
    str = ""
    for i in range(1, 10):
        str += f"{num} * {i} = {num * i} \n"
        # if i == 9:
        #     pass
        # else:
        #     str += "\n"
    return str


# file write
num = int(input())

f = open(f"gugu_{num}_result.txt", "w+")
f.write(gugudan(num))
f.close()

## 단순히 구구단 출력

# for i in range(2,10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')

# 교수님 코드


# def gugu(num):
#     with open(f"gugu_{num}_result.txt", "w") as handle:
#         for i in range(1, 10):
#             handle.write(f"{num} * {i} = {num*i} \n")


# gugu(6)
