s = input()
line = len(s)
list = [-1]*26


# print(ord('a')) # 97
# print(ord('z')) # 122
# 25

for i,j in zip(s,range(line)):
  # print(ord(i)-97)
  if list[ord(i) - 97] == -1:
    list[ord(i)-97] = j


for i in list:
  print(i, end = ' ')