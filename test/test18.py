a = input("문자열 입력: ")
word = a.upper()
print(f'대문자 변환: {word}')
word = a.lower()
print(f'소문자 변환: {word}')


b = len(a)
print(f'문자열 길이: {b}')


li = a.split()
print(f'공백으로 분리: {li}')

li = a.split('.')
print(f'마침표로 분리: {li}')

cnt = 0
for i in range(b):
    if 'o' in a[i]:
        print(f'o의 위치: {cnt}')
    else:
        cnt += 1

cnt = 0
for i in range(b):
    if 'o' in a[i]:
        cnt += 1
print(f'o의 개수: {cnt}')

a = a.replace('Python', 'AI')
print(f'Python을 AI로 변환: {a}')