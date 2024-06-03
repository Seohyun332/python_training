def add(a: int, b: int):
    return a + b


def base_counter(seq):
    temp = dict()
    for e in seq:
        if e not in temp:
            temp[e] = 0

        temp[e] += 1
    print(temp)
    return temp
