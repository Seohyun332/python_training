out_list = list()

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    out_list.append(A + B)


for e in out_list:
    print(e)
