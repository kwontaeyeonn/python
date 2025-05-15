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
def num(a):
    count = 0

    for j in range(n):
        count += li[j]
    count = count/len(li)

n = int(input())
for i in range(n):
    li = list(map(int,input().split()))

print(n)