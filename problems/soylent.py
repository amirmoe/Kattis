from sys import stdin
import math

rows = stdin.readline()

for line in stdin:
    calories = float(line)
    print(int(math.ceil(calories/400)))