col1, col2 = [], []
lines = []
with open("input.txt", "r") as file:
    lines = file.readlines()

lines = [line.split() for line in lines]
for line in lines:
    v1, v2 = line
    col1.append(int(v1))
    col2.append(int(v2))

col1.sort()
col2.sort()

res = 0

for v1, v2 in zip(col1, col2):
    res += abs(v1 - v2)

print(res)
