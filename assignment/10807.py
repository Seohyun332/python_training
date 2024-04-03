num = int(input())

n_list = input().split()
n_list = n_list[:num]  # letter cut

find_e = input()

count = 0

for e in n_list:
    if e == find_e:
        count += 1
print(count)
