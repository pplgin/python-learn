def findMinAndMax(L=[]):
    if len(L) == 0:
        pass
    else:
        min = L[0]
        max = L[0]  
        for x in L:
            if x >= max:
                max = x
            if x <= min:
                min = x
        return (min, max)
            

x = findMinAndMax([1,4,6,0,19])
print('#', x)
