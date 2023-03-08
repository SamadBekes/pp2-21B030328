s = input()

cnt_Up = 0
cnt_Low = 0
for i in s:
    if i.isupper():
        cnt_Up += 1
    elif i.islower():
        cnt_Low += 1

print('Counter of upper case letters is:', cnt_Up)
print('Counter of lower case letters is:', cnt_Low)