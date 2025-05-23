arr = []

for i in range(4):
	row = list(map(int, input().split()))
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

n,m = map(int,input().split())
arr = []
for i in range(n):
	row = []
	for j in range(m):
		# txt = f'({i}, {j})'
		row.append((i, j))
