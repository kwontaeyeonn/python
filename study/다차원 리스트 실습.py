# arr = []
# pass1 = 0
# for i in range(5):
#     num = list(map(int,input().split()))
#     arr.append(num)

# for student in arr:
#     total = 0
#     for j in student:
#         total += j
#     avg = total / len(student)

#     if avg>=80:
#         print("pass")
#         pass1 += 1

#     else:
#         print("fail")

# print("f'합격자는 {pass1}명")

# # 파스칼 삼각형 출력
# tg = []
# for i in range(5):
# 	row = []
# 	for j in range(i+1):
# 		if j==0 or j==i:
# 			row.append(1)
# 		else:
# 			row.append(tg[i-1][j-1]+tg[i-1][j])
# 	tg.append(row)

# for j in tg:
#     print(*j)

arr = []

for i in range(4):
	row = list(map(int,input().split()))
	arr.append(row)

for i in range(4):
	hap = 0
	for j in range(2):
		hap = arr[i][j]
	print(hap//2, end=" ")
print()

for i in range(2):
	hap = 0
	for j in range(4):
		hap += arr[j][i]
	print(hap//2, end=" ")
print()

hap = 0
for i in range(4):
	for j in range(4):
		hap += arr[i][j]
print(hap//8)