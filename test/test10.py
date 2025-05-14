import random
com = random.sample(range(1,10),3)
user = list(map(int,input().split()))
S = 0
B = 0
if com[0] == user[0]:
    S += 1
elif user[0] in com:
    B += 1
if com[1] == user[1]:
    S += 1
elif user[1] in com:
    B += 1
if com[2 ] == user[2]:
    S += 1
elif user[2] in com:
    B += 1

print(f"랜덤 리스트: {com}")
print(f"사용자 입력 리스트: {user}")
print(f"S = {S}, B = {B}")