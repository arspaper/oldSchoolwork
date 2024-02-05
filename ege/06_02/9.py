count = 0
with open('9.txt') as file:
    for line in file:
        nums = list(map(int, line.split()))
        num_counts = {}

        for num in nums:
            if num not in num_counts:
                num_counts[num] = 1
            else:
                num_counts[num] += 1

        twice_nums = []
        other_nums = []

        for num, cnt in num_counts.items():
            if cnt == 2:
                twice_nums.append(num)
            elif cnt == 1:
                other_nums.append(num)

        if len(twice_nums) == 2 and len(other_nums) == 3:

            avg_repeating = sum(twice_nums) / len(twice_nums)
            avg_all = sum(nums) / len(nums)

            if avg_repeating < avg_all:
                count += 1

print(count)