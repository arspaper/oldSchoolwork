"""
def my_function(n):
    bin_n = bin(n)[2:]
    bin_remainder_3 = bin(n % 3)[2:].zfill(2)
    new_bin_n = bin_n + bin_remainder_3
    bin_remainder_5 = bin(int(new_bin_n, 2) % 5)[2:].zfill(3)
    out_num = new_bin_n + bin_remainder_5
    return int(out_num, 2)


counter = 0
tgt = [1111111110, 1444444416]
for i in range(-100000000, 100000000):
    f = my_function(i)
    if tgt[0] <= f <= tgt[1]:
        counter += 1

print(counter)
"""
print(int(bin(1444444416)[2:][:-5], 2) - int(bin(1111111110)[2:][:-5], 2) - 1)
