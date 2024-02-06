nums = list()
max_num = 0
max_sum = 0
counter = 0

with open("17.txt") as file:
    for num in file:
        nums.append(num.rstrip())
        if int(num) % 100 == 13:
            max_num = max(max_num, int(num))

for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]
    if sum((len(a) == 3, len(b) == 3, len(c) == 3)) == 2:
        if sum((int(a), int(b), int(c))) <= max_num:
            counter += 1
            max_sum = max(max_sum, sum((int(a), int(b), int(c))))

print(counter, max_sum)