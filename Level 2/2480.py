A, B, C = map(int, input().split())

if A == B == C:
  print(10000+A*1000)
elif A == B or A == C or B == C:
  if A==B or A==C:
    print(1000+A*100)
  else:
    print(1000+C*100)
elif A != B != C:
  maxnum = max(A,B,C)
  print(maxnum*100)