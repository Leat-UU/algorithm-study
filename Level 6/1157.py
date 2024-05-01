word = input().upper() 
list = [0] * 26 # 알파벳 갯수만큼 배열 만들기.
# print(ord('A'), ord('Z'))
# A -> 65, Z -> 90 

for i in word:
  list[ord(i) - ord('A')] +=1 

max_list = max(list)

if list.count(max_list) > 1: # count 함수를 통해 최대값의 갯수가 1개보다 많을 경우 '?' 출력
  print('?')
else:
  print(chr(list.index(max_list) + 65)) 
