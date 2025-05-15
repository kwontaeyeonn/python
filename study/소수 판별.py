# def num(A):
#     yak=[]
#     for i in range(1,A+1):
#         if A%i==0:
#             yak.append(i)
#         else:
#             continue
#     if len(yak)>2 or len(yak)==1:
#         return f'소수가 아닙니다.'
#     else:
#         return f'소수입니다.'
    
    
# a = int(input())

# print(num(a))
era = [1 for i in range(10001)]
n = int(input())
for i in range(1001):
    if i == 0 or i == 1:
        era[i] = 0
        continue
    if era[i] == 0: 
        continue
    for j in range(i*j, 10001, i):
        era[j] = 0
s = 0
cnt = 0
for i in list(map(int,input().split())):
    if era[i]:
        s += 1
        cnt += 1
ret = f'{(s/cnt):.2f}'
print(ret)