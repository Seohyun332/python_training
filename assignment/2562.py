input_list = list()

for i in range(9):
    input_list.append(int(input()))

print(max(input_list))
print(input_list.index(max(input_list)) + 1)


# another version

# input_list = list()

# for i in range(9):
#     input_list.append(int(input()))

# max_num = 0
# for e in input_list:
#     if e > max_num:
#         max_num = e

# print(max_num)
# print(input_list.index(max_num) + 1)
