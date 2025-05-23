import random

User = list(map(int, input("2개 입력(1~6, 중복허용):").split()))

n = [1,2,3,4,5,6]

Com = random.choices(n,k=2)

if User[0] in Com and User[1] in Com:
    print(f'Com={Com} User={User}\n' '1등')
elif User[0] in Com and User[0] in Com:
    print(f'Com={Com} User={User}\n''2등')

else:
    print("3등")