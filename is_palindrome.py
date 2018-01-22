def is_palindrome(n):
    L = list(str(n))
    M = L[:]
    M.reverse()
    if L == M:
        return n


l = list(filter(is_palindrome, range(1,200)))

print(l)
