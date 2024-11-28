from math import log, floor
def sqr(n):
    counter = 0
    a = 1
    b = n
    while b - a > 0:
        counter += 1
        s = (a + b) // 2
        if s * s== n :
            return s
        elif s * s > n:
            b = s
        else:
            a = s +1

    print("n: ", n, 'counter:', counter)
    return b

for i in range(1,100):
    sqr(i)
    print(floor(log(i,2)))
