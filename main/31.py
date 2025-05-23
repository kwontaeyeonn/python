import random

print("컴퓨터가 생각한 1~20 숫자 맞추기")

n=random.randint(1,20)

while True:
    a = int(input("숫자입력(종료0):"))

    if a==n:
        print("정답!!")
    elif a>n:
        print("더 작은 숫자 입력!")
    elif a<n:
        print("더 큰 숫자 입력!!")
    elif a==0:
        print("종료!")