# #39_1
# d = int(input())
# count = 0
# for i in range(1,d+1):
#     count += i

# print(f'1부터 {d}까지의 합은 {count}')

# #39_2
# e = int(input("자연수 입력:"))
# cot = 1
# for i in range(e,0,-1):
#     cot = cot*i
# print(f'{e}!은 {cot}')

#40
import random
num1 = random.randint(1,101)
num2 = random.randint(1,101)
count = 0

if num1>num2:
    for i in range(num2, num1+1):
        count = count+i
    print(f'{num2}~{num1} => {count}')


elif num1==num2:
    count == num1
    print(f'{num1}~{num2} => {count}')

else:
    for i in range(num1,num2+1):
        count = count + i
    print(f'{num1}~{num2} => {count}')

