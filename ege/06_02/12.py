for i in range(4, 10000):
    n = "5" + "2" * i
    while "52" in n or "2222" in n or "1122" in n:
        if "52" in n:
            n = n.replace("52", "11", 1)
        if "2222" in n:
            n = n.replace("2222", "5", 1)
        if "1122" in n:
            n = n.replace("1122", "25", 1)
    n = [int(digit) for digit in n]
    if sum(n) == 64:
        print(i)
