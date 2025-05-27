f = open('data_2.txt', 'w')
while True:
    content = input("내용 입력:")
    f.write(f'{content}\n')
    if content == '':
        break

f.close()
