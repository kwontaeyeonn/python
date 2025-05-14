#36_1
for i in range(5):
    print(1)

#36_2
for i in range(5):
    print(f'{i}번째 : 1')

#37_1
for i in range(1,100):
    print(i)

#37_2
for i in range(100,0,-1):
    print(i)

#38_1
a = int(input("어디까지 출력할까요?:"))
for i in range(1,a+1):
    print(i)

#38_2
b = int(input("어디부터 출력할까요?:"))
for i in range(b,-1,-1):
    print(i)

#38_3
c = int(input("몇 단?:"))
print("="*3, c, "단", "="*3, sep="")
for i in range(1,10):
    print(f'8 * {i} = {i*8}')

