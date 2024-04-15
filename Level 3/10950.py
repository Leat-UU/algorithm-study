n = int(input())
l = []

for i in range(n):
  a,b = map(int, input().split())
  c = a+b
  l.append(c)

for i in range(n):
  print(l.pop(0))