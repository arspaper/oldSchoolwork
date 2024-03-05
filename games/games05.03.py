"""
Table
SПВПВП...
123456...
"""


def func1(s, p):  # 1 pile, +1, odd *2, even *1.5, >= 108, vanya first win, any case petya, max s
    if p == 3:
        if s >= 108:
            return True
        else:
            return False
    if p < 3 and s >= 108:
        return False
    else:
        if p % 2 == 0:
            if s % 2 == 0:
                return func1(s + 1, p + 1) or func1(s * 1.5, p + 1)  # стратегия победителя
            else:
                return func1(s + 1, p + 1) or func1(s * 2, p + 1)  # стратегия победителя
        else:
            if s % 2 == 0:
                return func1(s + 1, p + 1) and func1(s * 1.5, p + 1)  # стратегия проигравшего(любой ход)
            else:
                return func1(s + 1, p + 1) and func1(s * 2, p + 1)  # стратегия проигравшего(любой ход)

ans = list()
print("1")
for s in range(1, 108):
    if func1(s, 1):
        ans.append(s)
print(max(ans))
print()


def func2(a, s, p):  # 2 piles, +1, *3, >= 45, vanya first win, bad case petya, min s
    if p == 3:
        if a + s >= 45:
            return True
        else:
            return False
    return func2(a + 1, s, p + 1) or func2(a, s + 1, p + 1)\
        or func2(a * 3, s, p + 1) or func2(a, s * 3, p + 1)


print("2")
for s in range(1, 41):
    if func2(4, s, 1):
        print(s)
        break
print()


def func3(x, h):  # 1 pile, +1, +3, *2, >= 50, petya win second, any case vanya, 3 s
    if h == 4 and x >= 50:
        return 1
    elif h == 4 and x < 50:
        return 0
    elif x >= 50 and h < 4:
        return 0
    else:
        if h % 2 != 0:
            return func3(x + 1, h + 1) or func3(x + 3, h + 1) or func3(x * 2, h + 1)  # стратегия победителя
        else:
            return func3(x + 1, h + 1) and func3(x + 3, h + 1) and func3(x * 2, h + 1)  # стратегия проигравшего


ans = list()
print("3")
for s in range(1, 50):
    if func3(s, 1):
        print(s)
print()


def func4(a, s, p):  # 2 piles, < +1, < +2, < *2, >= 81, petya win second, any case vanya, min max s
    if p == 4:
        if a + s >= 81:
            return True
        else:
            return False
    if a + s >= 81 and p < 4:
        return False
    else:
        if p % 2 == 0:  # vanya
            if a < s:
                return func4(a + 1, s, p + 1) and func4(a + 2, s, p + 1) and func4(a * 2, s, p + 1)
            else:
                return func4(a, s + 1, p + 1) and func4(a, s + 2, p + 1) and func4(a, s * 2, p + 1)
        else:
            if a < s:
                return func4(a + 1, s, p + 1) or func4(a + 2, s, p + 1) or func4(a * 2, s, p + 1)
            else:
                return func4(a, s + 1, p + 1) or func4(a, s + 2, p + 1) or func4(a, s * 2, p + 1)


ans = list()
print("4")
for s in range(1, 69):
    if func4(12, s, 1):
        ans.append(s)

print(min(ans), max(ans))
print(ans)


def f(x, h):
    if (h == 3 or h == 5) and x >= 42:
        return 1
    elif h == 5 and x < 42:
        return 0
    elif x >= 42 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 2, h + 1) or f(x * 2, h + 1)  # стратегия победителя
        else:
            return f(x + 1, h + 1) and f(x + 2, h + 1) and f(x * 2, h + 1)  # сратегия проигравшего


def f1(x, h):
    if h == 3 and x >= 42:
        return 1
    elif h == 3 and x < 42:
        return 0
    elif x >= 42 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f1(x + 1, h + 1) or f1(x + 2, h + 1) or f1(x * 2, h + 1)  # стратегия победителя
        else:
            return f1(x + 1, h + 1) and f1(x + 2, h + 1) and f1(x * 2, h + 1)  # стратегия проигравшего(любой ход)


for x in range(1, 41):
    if f(x, 1) == 1:
        print(x)
print("5")
for x in range(1, 41):
    if f1(x, 1) == 1:
        print(x)


def f(x, y, h):
    if (h == 3 or h == 5) and x + y <= 20:
        return 1
    elif h == 5 and x + y > 20:
        return 0
    elif x + y <= 20 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x - 1, y, h + 1) or f(x, y - 1, h + 1) or f(x // 2, y, h + 1) or f(x, y // 2,
                                                                                        h + 1)  # стратегия победителя
        else:
            return f(x - 1, y, h + 1) and f(x, y - 1, h + 1) and f(x // 2, y, h + 1) and f(x, y // 2,
                                                                                           h + 1)  # стратегия проигравшего(любой ход)


def f1(x, y, h):
    if h == 3 and x + y <= 20:
        return 1
    elif h == 3 and x + y > 20:
        return 0
    elif x + y <= 20 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f1(x - 1, y, h + 1) or f1(x, y - 1, h + 1) or f1(x // 2, y, h + 1) or f1(x, y // 2,
                                                                                            h + 1)  # стратегия победителя
        else:
            return f1(x - 1, y, h + 1) and f1(x, y - 1, h + 1) and f1(x // 2, y, h + 1) and f1(x, y // 2,
                                                                                               h + 1)  # стратегия проигравшего(любой ход)


for x in range(10, 100):
    if f(x, 10, 1) == 1:
        print(x)
print("====")
for x in range(1, 100):
    if f1(x, 10, 1) == 1:
        print(x)