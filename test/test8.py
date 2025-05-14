a, b, c = map(int, input().split())
d = 1 

while d%a!=0 and d%b!=0 and d%c!=0:
    d+=1 
print(d)

n = int(input())

a = int(input().split())

#for i in range(n):
#    a[i] = int(a[i])

d = []
for i in range(24) :
    d.append(0)

for i in range(n) :
    d[a[i]] += 1

for i in range(1, 24) :
    print(d[i], end=' ')