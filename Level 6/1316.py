n = int(input())
count = 0 

for _ in range(n):
    text = input()
    group_word = True

    for i in range(len(text) - 1):
        if text[i] != text[i + 1]:
            if text[i] in text[i + 1:]:
                group_word = False
                break

    if group_word:
        count += 1

print(count) 
