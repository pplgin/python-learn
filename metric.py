import time, functools

def metric(func):
    def spent(*args, **kw):
        print('%s executed in %s ms' % (func.__name__, time.time()))
        m = func(*args, **kw)
        print('%s execut end in %s ms' % (func.__name__, time.time()))
        return m
    return spent




@metric
def fast(x, y):
    time.sleep(0.12)
    return x+y

@metric
def slow(x,y):
    time.sleep(3)
    return x * y

fast(1,2)
slow(4,4)
