import random

#단어장
eng = []

print("=====시작=====")

# 추가할 단어 개수 입력
n = int(input("추가할 단어 개수를 입력하세요: "))

# 단어와 뜻 입력 받기
for i in range(1,n+1):
    word = input(f"{i}. 영어 단어 입력: ")
    meaning = input(f"{i}. 단어의 뜻 입력: ")
    print() #공백 한줄 출력
    #eng리스트에 딕셔너리 형태로 단어와 뜻 넣기
    eng.append({'word': word, 'meaning': meaning})

print()
#단어장이 업데이트 되었음을 알림
print("===단어장 업데이트 완료===")

# 풀 문제 개수 입력
count = int(input("풀 문제 개수를 입력하세요: "))
print() #공백 한줄 출력

# 리스트에서 랜덤으로 문제 추출
questions = random.sample(eng, min(n, len(eng)))

correct = 0
wrong = 0

#문제 풀기가 시작했음을 알려주기
print('====문제 풀기 시작====')
#문제 번호(1부터 시작)
i = 1
for word in questions:
    #문제 번호와 문제(뜻) 출력
    print()
    answer = input(f"{i}번 문제 - '{word['meaning']}'는?: ")

    #입력한 뜻이 단어와 똑같을떄
    if answer == word['word']:
        print("정답입니다!")
        #정답에 1추가
        correct += 1

    #입력한 뜻이 단어랑 다를때
    else:
        # 다시 풀기
        print(f"오답입니다. 다시 입력해보세요")
        answer = input(f"{i}번 문제 다시풀기 - '{word['meaning']}'는?: ")
        
        #입력한 뜻이 단어랑 같을때
        if answer == word['word']:
            print("정답입니다!")
            #정답에 1추가
            correct += 1
        #틀렸을때
        else:
            #정답 출력
            print(f"오답입니다. {i}번 정답: {word['word']}")
            #오답에 1추가
            wrong += 1
    #문제 번호를 순서대로 출력하기 위해 1을 반복해서 더하기
    i += 1


# 결과 출력
print()
print("문제를 모두 풀었습니다.")
print()
print("=====결과 출력====")
print(f"정답 개수: {correct}")
print(f"오답 개수: {wrong}")
