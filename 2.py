a, n = map(int, input('Введи сумму и срок вклада: ').split())
v = 0.0
m = a
def F(a, n):
    if (a // 10000) >= 17:
        v = 5
    else:
        v = (a // 10000)*0.3
    
    if n < 4:
        v += 3
        for i in range(n):
            a *= 1 + v/100
        return a - m
    elif (n>3)and(n<7):
        v += 3
        for i in range(3):
            a *= 1 + v/100
        v += 2
        for i in range(n-3):
            a *= 1 + v/100
        return a - m
    else:
        v += 3
        for i in range(3):
            a *= 1 + v/100
        v += 2
        for i in range(3):
            a *= 1 + v/100
        v -= 3
        for i in range(n-6):
            a *= 1 + v/100
        return a - m

print(F(a, n))
