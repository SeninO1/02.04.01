n =int(input())
a = set()
if 1 <= n <= 100000:
    for i in range(n):
        b = int(input())
        if abs(b) < 2 * 10 ** 9:
            a.add(b)
print(len(a))