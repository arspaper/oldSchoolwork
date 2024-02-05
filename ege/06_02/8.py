count = 0
for a in range(1, 8):
    for b in range(8):
        for c in range(8):
            for d in range(8):
                for e in range(8):
                    num = [a, b, c, d, e]
                    if 1 not in num:
                        if len(set(num)) == 5:
                            if ((a % 2 == 0) and (b % 2 != 0) and (c % 2 == 0) and (d % 2 != 0) and (e % 2 == 0)) or \
                                    ((a % 2 != 0) and (b % 2 == 0) and (c % 2 != 0) and (d % 2 == 0) and (e % 2 != 0)):
                                count += 1
print(count)
