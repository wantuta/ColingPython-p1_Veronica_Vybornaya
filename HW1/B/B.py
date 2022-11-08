def solution(n):
    p1 = '   _~_  '
    p2 = '  (o o)  '
    p3 = ' /  V  \ '
    p4 = '/(  _  )\ '
    p5 = '  ^^ ^^  '
    print (p1 * n, end = '\n')
    print (p2 * n, end = '\n')
    print (p3 * n, end = '\n')
    print (p4 * n, end = '\n')
    print (p5 * n, end = '\n')
    

n = int(input(('How many penguins do you need? ')))
print(solution(n))
