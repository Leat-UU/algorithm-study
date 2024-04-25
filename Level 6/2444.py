# index = int(input())

# for i in range(1 ,index+1):
#   star = '*' * (2 * i -1)
#   print('{:^{width}}'.format(star, width=2 * index - 1))

# for i in range(index-1, 0, -1):
#     stars = '*' * (2 * i - 1)
#     print('{:^{width}}'.format(stars, width=2 * index - 1))
# 출력형식 오류 .format형식으로 인한 오류 발생 예상

index = int(input())
star = 1 

for i in range(1, index+1):
  print(' ' * (index-i) + '*' * star)
  star += 2

star -=2

for i in range(index-1, 0, -1):
  star -=2
  print(' ' * (index-i) + '*' * star)
  pass

