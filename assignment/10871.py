lens, num = map(int, input().split())

numbers = input().split()
ls = list()

# int type casting
# append elements
for e in numbers:
    ls.append(int(e))

# length
ls = ls[:lens]

# output
for i in range(len(ls)):
    if ls[i] < num:
        print(ls[i], end=" ")


### make list : int type casting
# n = list(map(int, input().split()))
# print(n)
