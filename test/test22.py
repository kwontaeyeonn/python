# def sum(n):
#     s = 1
#     for i in range(1,n+1):
#         s *= i
#     return s

# n = int(input())
# print(sum(n))

# def maxp(a, b):
#     if a >= b: 
#         return a
#     else: 
#         return b

# a, b = map(int,input().split())
# print(maxp(a, b))

# def maxp(a,b):
#     if a>b:
#         return a
#     else:
#         return b
    
# a,b = map(int,input().split())
# print(f'큰 수 : {maxp(a,b)}')

# def num(a):
#     if a<2:
#         return 1
#     else:
#         return num + num(a-1)

import random
def genPass():
    chr = "abcdefg"
    passwd = ""
    for i in range(8):
        ch = random.choice(chr)
        passwd += ch
    return passwd

import random
def pw_crt():
	list = "aeiou"
	passwd = ""
	for i in range(4):
		passwd = random.choice(chr(list))

print("*", pw_crt())


for i in range(3):
    result = genPass()
    print(f"암호 {i+1}: {result}")