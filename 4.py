q = int(input())
a = []
b = []
c = []
def f(q):
    if q<2:
        print('Error')
    else:
        print('1 матрица')
        for i in range(q**2):
            a.append(int(input()))
        print('2 матрица')
        for i in range(q**2):
            b.append(int(input()))
        for i in range(0, q**2):
            c.append(a[i]+b[i])

        for i in range(1, q+1):
            for v in range(q*i - q, q*i):
                print(c[v], end=' ')
            print('')
print(f(q))
