def fan(s, len=3):
    if len % 2 == 0:
        return 0
    d = ":fan:"
    t = ":" + s + ":"

    for i in range(len):
        if i == len // 2:
            total = (d * (len // 2)) + t + (d * (len // 2))
            print(total)
        else:
            print(d * len)


fan(input())
