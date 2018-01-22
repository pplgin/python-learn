def triangles(n):
    ret = [1]
    while len(ret) <= n:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i-1]
        ret.append(1)
        pre = ret[:]



def tanx(n):
    ret = [1]
    while len(ret) <= n:
        yield ret
        ret = [*ret, 0]
        ret = [ret[i-1] + ret[i] for i in range(len(ret))]

for x in triangles(5):
    print('#', x)

for s in tanx(5):
    print('s', s)


