N = int(input())

L = list(map(int, input().split()))

Find = int(input())
sum  = 0

for i in range(N):
    if L[i] == Find:
        sum += 1
print(sum)