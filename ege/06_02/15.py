for A in range(0, 10000):
    check = False
    for x in range(0, 200):
        for y in range(0, 200):
            if not ((x + 2 * y < A) or (y > x) or (x > 60)):
                check = True
    if not check:
        print(A)
        break
