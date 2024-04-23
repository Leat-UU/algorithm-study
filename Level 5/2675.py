case = int(input())

for i in range(case):
  num, s = map(str, input().split())
  num = int(num)
  p = ""

  for j in s:
    p += j*num
  print(p)
