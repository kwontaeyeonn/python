import random

a = input("가위, 바위, 보 중에 하나 입력: ")

num = ('가위', '바위', '보')

n = random.choice(num)

print("user: ", a, " com: ", n, " -> " , sep='', end='')

if a=='가위':
    if n=='가위':
        print("비겼음")
    elif n=='바위':
        print("졌음")
    else:
        print("이겼음")
elif a=='바위':
    if n=='바위':
        print("비겼음")
    elif n=='가위':
        print("이겼음")
    else:
        print("졌음")
else:
    if n=='보':
        print("비겼음")
    elif n=='가위':
        print("졌음")
    else:
        print("이겼음")