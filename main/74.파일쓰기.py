#74
f = open('data_1.txt', 'w')

for i in range(1,11):
    line = f'{i}번째 줄\n'
    f.write(line)

f.close()

#75
f = open('data_1.txt', 'a')

for i in range(11,21):
    line = f'{i}번째 줄\n'
    f.write(line)

f.close()

f = open('data_1.txt', 'r')

# content = f.readline()
# content = f.readlines()
content = f.read()
print(content)

f.close()