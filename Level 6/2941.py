kropia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

text = input()
text_len = len(text)

for i in kropia:
  count = text.count(i)
  text_len -= count


print(text_len)