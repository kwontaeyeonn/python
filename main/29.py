while True:
    n = int(input())
    
    if n%5==0:
        print("5의 배수 입니다.")
    elif n%5!=0:
        print("5의 배수가 아닙니다.")
    elif n==0:
        break