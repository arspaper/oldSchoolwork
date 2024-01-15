count_sh = 0
max_sqnc = ""

with open('files/№5.txt', mode="r", encoding="utf-8") as file:
    f = file.readline()
    for i in range(len(f) - 2):
        line = f[i:i + 3]
        if line == "ШИШ":
            count_sh += 1


    sqnc = ""
    for ltr in f:
        if ltr not in sqnc:
            sqnc += ltr
        else:
            if len(sqnc) > len(max_sqnc):
                max_sqnc = sqnc
            sqnc = ""

    if len(sqnc) > len(max_sqnc):
        max_sqnc = sqnc


print(count_sh, max_sqnc)
