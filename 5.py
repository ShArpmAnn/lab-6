s = input()
def f(s):
    s = s.replace(' ','').lower()
    return 'да' if s == s[::-1] else 'нет'
print(f(s))
