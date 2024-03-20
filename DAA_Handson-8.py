def Part(li, l, h):
    p = li[h]
    i = l - 1
    for j in range(l, h):
        if li[j] <= p:
            i += 1
            li[i], li[j] = li[j], li[i]
    li[i + 1], li[h] = li[h], li[i + 1]
    return i + 1

def qs(li, l, h):
    if l < h:
        pi = Part(li, l, h)
        qs(li, l, pi - 1)
        qs(li, pi + 1, h)

def stat(li, i):
    length = len(li)
    if i < 0 or i >= length:
        return None
    qs(li, 0, length - 1)
    return li[i]
#Example
li = [3, 2, 1, 5, 4]
i = 3
res = stat(li, i)
print(f"The {i}th order statistic: {res}")
