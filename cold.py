n = int(input())
temps = list(map(int, input().split()))
count = 0
for t in temps:
    if t < 0:
        count += 1
print(count)
