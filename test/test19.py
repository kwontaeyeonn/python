import math
lst = list(range(1,11))

#평균
mean = sum(lst) / len(lst)
print("평균 : {mean}")

#분산
vsum = sum([(i-mean)**2 for i in lst]) / len(lst)
print(f'분산: {vsum}')

#표준편차
std = math.sqrt(vsum)
print(f'표준편차: {std}')

#최대 공약수, 최소공배수
gcd = math.god(*lst)
lcm = math.lcm(*lst)
print(f'최대공약수 {gcd} 최ㅗ소공배수: {lcm}')