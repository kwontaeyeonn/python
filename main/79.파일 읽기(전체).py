f = open('data_1.txt', 'w')

for i in range(1,11):
    line = f'{i}번째 줄\n'
    f.write(line)

f.close()

f = open('data_1.txt', 'r')
while True:
    line = f.readline()
    if line=="":
        break
    print(line)
f. close()