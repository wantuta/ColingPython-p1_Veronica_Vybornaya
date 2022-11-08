def solution(n, k):
    if k > n:
        a = k // n
        b = k - n
        return(a,b)
    elif k == n:
        return(n, 0)
    else:
        a = 1
        b = n - k
        return(a, b)

n = int(input())
k = int(input())
print(solution(n, k))
