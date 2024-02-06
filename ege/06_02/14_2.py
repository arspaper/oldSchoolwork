exp = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 5 - 2024

remainders = list()
while exp > 25:
    remainders.append(str(exp % 25))
    exp //= 25
remainders.append(str(exp))
remainders.reverse()
out_num = ""
for num in remainders:
    out_num += num
print(out_num.count('0'))