a, b = map(int, input().split())
v = 0
i = 0
def f(a, b, i):
    if (b - a < 2)or(b < 0)or(a < 0):
        print('Error!')
    else:
        for i in range(a, b+1):
            v = 0
            for q in range(2, i//2+1):
                if i % q == 0:
                    v += 1
            if v == 0:
                print(i)
        
print(f(a, b, i))
