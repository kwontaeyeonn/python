#방법1
n = int(input())
a = list(map(int, input().split()))

min = a[0]
for i in range(n):
    if a[i] < min:
        min = a[i]

print(min)

#방법2
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a.sort()
print(a[0])