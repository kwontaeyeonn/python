age = 17
height = 170.5
tf = False #0

print(int(age), int(height), int(tf))
print(type(age), type(height), type(tf))

a = 10
b = -2.5
c = 0xDA #218

print(a, type(a))
print(b, type(b))
print(c, type(c))

print(a+b, type(a+b))

a = True
if(a): #만약 (a)가 참이라면
    print("참")

a = []
b = [1, 2, 3]
c = ['DGSW', '1학년', '화이팅']
d = [1, 2, 'DGSW', 'daegu']
e = [1, 2, ['DGSW', 'daegu']]

print(b[0])
print(c[-1])    # 리스트 마지막 요솟값
print(e[2])     # 리스트는 또 다른 리스트 값을 포함할 수 있다.
print(e[-1][0]) # 리스트의 마지막 요소인 ['DGSW', 'daegu']의 첫 번째 요소를 불러온다.

a = [1, 2, ['a', 'b', ['DGSW', ['daegu']]]]
print(a[2][2][0])
