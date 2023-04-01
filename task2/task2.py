import sys

with open(sys.argv[1]) as f:
    line = f.readlines()

n = list(map(int, line))
avg = round(sum(n) / len(n))

m = [abs(n[i] - avg) for i in range(len(n))]
print(sum(m))
