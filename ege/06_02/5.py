def my_function(n):
    bin_n = bin(n)[2:]
    if n % 3 == 0:
        new_bin_n = bin_n + bin_n[-3:]
    else:
        new_bin_n = bin_n + bin((n % 3) * 3)[2:]
    return int(new_bin_n, 2)

ans = list()
a = 0
for i in range(10000):
    a += 1
    if my_function(a) > 151:
        ans.append(my_function(a))

print(min(ans))
