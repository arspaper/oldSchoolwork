from fnmatch import *


for x in range(0, 10 ** 8, 317):
    if fnmatch(str(x), '12??1*56'):
        print(str(x), str(x // 317))
