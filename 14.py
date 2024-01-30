my_list = list()
for x in range(37):
    for y in range(37):
        expression = (1 * 37 ** 7 + 2 * 37 ** 6 + x * 37 ** 5 + 6 *
                      37 ** 4 + 4 * 37 ** 3 + 3 * 37 ** 2 + y * 37 + 7)
        if expression % 36 == 0:
            my_list.append(y * 37 + x)
            break

print(max(my_list))
