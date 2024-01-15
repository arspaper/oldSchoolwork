file_path = "files/№2.txt"

ac = 0
bc = 0
myset = set()


f = open(file_path).readline()

for i in range(len(f) - 6):
    line = f[i:i + 7]
    if line == line[::-1]:
        ac += 1
        myset.add(line)

for i in range(len(f) - 5):
    line = f[i:i + 6]
    if line == "XXZZYY":
        bc += 1


print(ac, bc)
print(f"DIFF PALINDROMES: {len(myset)}")
