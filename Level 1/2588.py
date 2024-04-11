A = input()
B = input()

intA = int(A)
intB = int(B)

first = int(B[0])
second = int(B[1])
third = int(B[-1])


out1 = intA*third
out2 = intA*second
out3 = intA*first
out4 = out1 + out2*10 + out3*100

print(out1)
print(out2)
print(out3)
print(out4)