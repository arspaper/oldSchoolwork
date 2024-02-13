def func1_1(a, s, p):  # 2 piles, +3, *2, >= 375, vanya first win, bad case petya, min s
    if p == 3:
        if a + s >= 375:
            return True
        else:
            return False
    return func1_1(a + 3, s, p + 1) or func1_1(a, s + 3, p + 1)\
        or func1_1(a * 2, s, p + 1) or func1_1(a, s * 2, p + 1)


print("1_1")
for s in range(1, 348):
    if func1_1(27, s, 1):
        print(s)
        break
print()


def func1_2(a, s, p):  # 2 piles, +3, *2, >= 375, petya second win, any case vanya, min max s
    if p == 4:
        if a + s >= 375:
            return True
        else:
            return False
    if a + s >= 375:
        return False
    if p % 2 == 0:  # petya's turns
        return func1_2(a + 3, s, p + 1) and func1_2(a, s + 3, p + 1)\
            and func1_2(a * 2, s, p + 1) and func1_2(a, s * 2, p + 1)
    else:  # vanya's turns
        return func1_2(a + 3, s, p + 1) or func1_2(a, s + 3, p + 1)\
            or func1_2(a * 2, s, p + 1) or func1_2(a, s * 2, p + 1)


print("1_2")
ans = list()
for s in range(1, 348):
    if func1_2(27, s, 1):
        ans.append(s)
print(min(ans), max(ans))
print()


def func1_3(a, s, p):  # 2 piles, +3, *2, >= 375, vanya first can win, vanya second win, any case petya, min s
    if (p == 3 or p == 5) and a + s >= 375:
        return True
    if p == 5 and a + s < 375:
        return False
    if a + s >= 375:
        return False
    if p % 2 == 0:  # petya's turns
        return func1_3(a + 3, s, p + 1) or func1_3(a, s + 3, p + 1)\
            or func1_3(a * 2, s, p + 1) or func1_3(a, s * 2, p + 1)
    else:  # vanya's turns
        return func1_3(a + 3, s, p + 1) and func1_3(a, s + 3, p + 1)\
            and func1_3(a * 2, s, p + 1) and func1_3(a, s * 2, p + 1)


def func1_3_1(a, s, p):  # //this func counts guaranteed win
    if p == 5 and a + s >= 375:
        return True
    if p == 5 and a + s < 375:
        return False
    if a + s >= 375:
        return False
    if p % 2 == 0:  # petya's turns
        return func1_3_1(a + 3, s, p + 1) or func1_3_1(a, s + 3, p + 1)\
            or func1_3_1(a * 2, s, p + 1) or func1_3_1(a, s * 2, p + 1)
    else:  # vanya's turns
        return func1_3_1(a + 3, s, p + 1) and func1_3_1(a, s + 3, p + 1)\
            and func1_3_1(a * 2, s, p + 1) and func1_3_1(a, s * 2, p + 1)


print("1_3")
ans = list()
for s in range(1, 348):
    if func1_3(27, s, 1):
        ans.append(s)
for s in range(1, 348):
    if func1_3_1(27, s, 1):
        ans.append(s)
print(min(ans))
print()


def func2_1(s, p):  # 1 pile, +1, +5, *3, >= 199, vanya first win, bad case petya, min s
    if p == 3:
        if s >= 199:
            return True
        else:
            return False
    return func2_1(s + 1, p + 1) or func2_1(s + 5, p + 1) or func2_1(s * 3, p + 1)


print("2_1")
for s in range(1, 199):
    if func2_1(s, 1):
        print(s)
        break
print()


def func2_2(s, p):  # 1 pile, +1, +5, *3, >= 199, petya second win, any case vanya, min max s
    if p == 4:
        if s >= 199:
            return True
        else:
            return False
    if s >= 199:
        return False
    if p % 2 == 0:  # petya's turns
        return func2_2(s + 1, p + 1) and func2_2(s + 5, p + 1) and func2_2(s * 3, p + 1)
    else:  # vanya's turns
        return func2_2(s + 1, p + 1) or func2_2(s + 5, p + 1) or func2_2(s * 3, p + 1)


print("2_2")
ans = list()
ans.sort()
for s in range(1, 199):
    if func2_2(s, 1):
        ans.append(s)
print(ans[0], ans[1])
print()


def func2_3(s, p):  # 1 pile, +1, +5, *3, >= 199, vanya first can win, vanya second win, any case petya, min s
    if (p == 3 or p == 5) and s >= 199:
        return True
    if p == 5 and s < 199:
        return False
    if s >= 199:
        return False
    if p % 2 != 0:  # vanya's turns
        return func2_3(s + 1, p + 1) and func2_3(s + 5, p + 1) and func2_3(s * 3, p + 1)
    else:  # petya's turns
        return func2_3(s + 1, p + 1) or func2_3(s + 5, p + 1) or func2_3(s * 3, p + 1)


def func2_3_1(s, p):  # //this func counts guaranteed win
    if p == 5 and s >= 199:
        return True
    if p == 5 and s < 199:
        return False
    if s >= 199:
        return False
    if p % 2 != 0:  # vanya's turns
        return func2_3(s + 1, p + 1) and func2_3(s + 5, p + 1) and func2_3(s * 3, p + 1)
    else:  # petya's turns
        return func2_3(s + 1, p + 1) or func2_3(s + 5, p + 1) or func2_3(s * 3, p + 1)


print("2_3")
ans = list()
for s in range(1, 199):
    if func2_3(s, 1):
        ans.append(s)
for s in range(1, 199):
    if func2_3_1(s, 1):
        ans.append(s)
print(min(ans))
print()


def func3_1(s, p):  # 1 pile, +1, *2, >= 21, petya second win, any case vanya, min s
    if p == 4:
        if s >= 21:
            return True
        else:
            return False
    if s >= 21:
        return False
    if p % 2 != 0:  # vanya's turns
        return func3_1(s + 1, p + 1) or func3_1(s * 2, p + 1)
    else:  # petya's turns
        return func3_1(s + 1, p + 1) and func3_1(s * 2, p + 1)


print("3_1")
for s in range(1, 21):
    if func3_1(s, 1):
        print(s)
        break
print()


def func3_2(s, p):  # 1 pile, +1, *2, >= 21, vanya first can win, vanya second win, any case petya, min s
    if (p == 3 or p == 5) and s >= 21:
        return True
    if p == 5 and s < 21:
        return False
    if s >= 21:
        return False
    if p % 2 != 0:  # vanya's turns
        return func3_2(s + 1, p + 1) and func3_2(s * 2, p + 1)
    else:  # petya's turns
        return func3_2(s + 1, p + 1) or func3_2(s * 2, p + 1)


def func3_2_1(s, p): # //this func counts guaranteed win
    if p == 5 and s >= 21:
        return True
    if p == 5 and s < 21:
        return False
    if s >= 21:
        return False
    if p % 2 != 0:  # vanya's turns
        return func3_2(s + 1, p + 1) and func3_2(s * 2, p + 1)
    else:  # petya's turns
        return func3_2(s + 1, p + 1) or func3_2(s * 2, p + 1)


print("3_2")
ans = list()
for s in range(1, 21):
    if func3_2(s, 1):
        ans.append(s)
for s in range(1, 21):
    if func3_2_1(s, 1):
        ans.append(s)
print(min(ans))
print()


def func3_3(s, p):  # 1 pile, +1, *2, >= 21, petya first can win, petya second can win, petya third win, any case
    # vanya, 2 min s
    if (p == 2 or p == 4 or p == 6) and s >= 21:
        return True
    if p == 6 and s < 21:
        return False
    if s >= 21:
        return False
    if p % 2 == 0:  # vanya's turns
        return func3_3(s + 1, p + 1) and func3_3(s * 2, p + 1)
    else:  # petya's turns
        return func3_3(s + 1, p + 1) or func3_3(s * 2, p + 1)


def func3_3_1(s, p):  # //this func counts guaranteed win
    if p == 6 and s >= 21:
        return True
    if p == 6 and s < 21:
        return False
    if s >= 21:
        return False
    if p % 2 == 0:  # vanya's turns
        return func3_3_1(s + 1, p + 1) and func3_3_1(s * 2, p + 1)
    else:  # petya's turns
        return func3_3_1(s + 1, p + 1) or func3_3_1(s * 2, p + 1)


print("3_3")
ans = list()
for s in range(1, 21):
    if func3_3(s, 1):
        ans.append(s)
for s in range(1, 21):
    if func3_3_1(s, 1):
        ans.append(s)
ans.sort()
print(ans[0], ans[1])
print()
