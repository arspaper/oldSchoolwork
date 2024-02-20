def func1(s, p):  # 1 pile, +1, +2, *3, >=75, vanya first win, bad case petya, min s
    if p == 3:
        if s >= 75:
            return True
        else:
            return False
    return func1(s + 1, p + 1) or func1(s + 2, p + 1) or func1(s * 3, p + 1)


print("1)")
for s in range(1, 75):
    if func1(s, 1):
        print(s)
        break
print()

def func2(a, s, p):  # 2 piles, +1, *2, >=86, vanya first win, bad case petya, min s
    if p == 3:
        if a + s >= 86:
            return True
        else:
            return False
    return func2(a + 1, s, p + 1) or func2(a, s + 1, p + 1)\
        or func2(a * 2, s, p + 1) or func2(a, s * 2, p + 1)


print("2)")
for s in range(1, 72):
    if func2(14, s, 1):
        print(s)
        break
print()


def func3(a, s, p):  # 2 piles, +1, *2, >=231, petya second win, any case vanya, 2 min s
    if p == 4:
        if a + s >= 231:
            return True
        else:
            return False
    if a + s >= 231:
        return False
    if p % 2 == 0:  # petya's turns
        return func3(a + 1, s, p + 1) and func3(a, s + 1, p + 1)\
            and func3(a * 2, s, p + 1) and func3(a, s * 2, p + 1)
    else:  # vanya's turns
        return func3(a + 1, s, p + 1) or func3(a, s + 1, p + 1)\
            or func3(a * 2, s, p + 1) or func3(a, s * 2, p + 1)


print("3)")
ans = list()
for s in range(1, 214):
    if func3(17, s, 1):
        ans.append(s)
ans.sort()
print(ans[0], ans[1])
print()


def func4(s, p):  # 1 pile, +1, +3, *2, >=50, vanya can win first, vanya win second, any case petya, min s
    if (p == 3 or p == 5) and s >= 50:
        return True
    if p == 5 and s < 50:
        return False
    if s >= 50:
        return False
    if p % 2 != 0:  # vanya's turns
        return func4(s + 1, p + 1) and func4(s + 3, p + 1) and func4(s * 2, p + 1)
    else:  # petya's turns
        return func4(s + 1, p + 1) or func4(s + 3, p + 1) or func4(s * 2, p + 1)


def func4_1(s, p):  # //this func counts guaranteed win
    if p == 5 and s >= 50:
        return True
    if p == 5 and s < 50:
        return False
    if s >= 50:
        return False
    if p % 2 != 0:  # vanya's turns
        return func4(s + 1, p + 1) and func4(s + 3, p + 1) and func4(s * 2, p + 1)
    else:  # petya's turns
        return func4(s + 1, p + 1) or func4(s + 3, p + 1) or func4(s * 2, p + 1)


print("4")
ans = list()
for s in range(1, 50):
    if func4(s, 1):
        ans.append(s)
for s in range(1, 50):
    if func4_1(s, 1):
        ans.append(s)
print(min(ans))
print()


def func5():  # 2 piles, +1, (1)*2, (2)*3, >=84, vanya can win first, vanya win second, any case petya, min s
    pass


def func5(a, s, p):  # 2 piles, +3, *2, >= 375, vanya first can win, vanya second win, any case petya, min s
    if (p == 3 or p == 5) and a + s >= 84:
        return True
    if p == 5 and a + s < 84:
        return False
    if a + s >= 84:
        return False
    if p % 2 == 0:  # petya's turns
        return func5(a + 1, s, p + 1) or func5(a, s + 1, p + 1)\
            or func5(a * 2, s, p + 1) or func5(a, s * 3, p + 1)
    else:  # vanya's turns
        return func5(a + 1, s, p + 1) and func5(a, s + 1, p + 1)\
            and func5(a * 2, s, p + 1) and func5(a, s * 3, p + 1)


def func5_1(a, s, p):  # //this func counts guaranteed win
    if p == 5 and a + s >= 84:
        return True
    if p == 5 and a + s < 84:
        return False
    if a + s >= 84:
        return False
    if p % 2 == 0:  # petya's turns
        return func5_1(a + 1, s, p + 1) or func5_1(a, s + 1, p + 1)\
            or func5_1(a * 2, s, p + 1) or func5_1(a, s * 3, p + 1)
    else:  # vanya's turns
        return func5_1(a + 1, s, p + 1) and func5_1(a, s + 1, p + 1)\
            and func5_1(a * 2, s, p + 1) and func5_1(a, s * 3, p + 1)


print("5)")
ans = list()
for s in range(1, 68):
    if func5(16, s, 1):
        ans.append(s)
for s in range(1, 68):
    if func5_1(16, s, 1):
        ans.append(s)
print(min(ans))
print()
