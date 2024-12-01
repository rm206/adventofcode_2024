from collections import defaultdict

col1, col2 = [], defaultdict(int)

lines = []
with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.split() for line in lines]

for line in lines:
    _, v2 = line
    col2[int(v2)] += 1

res = 0
for line in lines:
    v1, _ = line
    v1 = int(v1)
    res += v1 * col2[v1]

print(res)
