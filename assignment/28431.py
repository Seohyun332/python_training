input_list = list()

for i in range(5):
    input_list.append(int(input()))

check_dic = dict()
for e in input_list:
    if e in check_dic:
        check_dic[e] += 1
    else:
        check_dic[e] = 1

for key, value in check_dic.items():
    if value % 2 == 1:
        print(key)

# while Tr1ue:1
#     e = input_list[0]
#     try:
#         check_list = input_list[1:]
#         input_list = check_list.remove(e)
#     except:
#         print(e)
#         breakddd
