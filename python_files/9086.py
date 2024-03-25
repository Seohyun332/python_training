num = int(input())

str_list = list()
for i in range(num):
    str_list.append(input())

for st in str_list:
    out = st[0] + st[len(st) - 1]
    print(out)


# in python list
# [ 'H' , 'E', 'L', 'L', 'O' ]
# index : -1  = end letter
# (-) index is right start index
