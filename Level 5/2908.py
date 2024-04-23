# 문자열 뒤집는 방법들 https://itholic.github.io/python-reverse-string/

num1, num2 = input().split()

num1 = int(num1[::-1])
num2 = int(num2[::-1])

if num1 > num2 :
  print(num1)
else:
  print(num2)