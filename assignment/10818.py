len = int(input())

arr = list(map(int, input().split()))

mi = min(arr)
ma = max(arr)

s = "{0} {1}".format(mi, ma)
print(s)
