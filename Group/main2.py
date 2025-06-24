import random

# 언어별 단어장을 저장할 리스트 초기화
eng = []       # 영어 단어장
chinese = []   # 중국어 단어장
japanese = []  # 일본어 단어장

# 메인 루프
while True:
    print()
    # Step 1: 사용자가 학습할 언어 선택
    language = input("학습할 언어를 입력하세요: (1:영어, 2:중국어, 3:일본어, 0:종료): ")
    if language == "0":  # 0 입력 시 프로그램 종료
        break
    if language not in ['1', '2', '3', '영어', '중국어', '일본어']:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue  # 올바르지 않은 입력일 경우 처음으로 돌아감
    if language == '1':
        print('영어를 선택하셨습니다')
    elif language == '2':
        print('중국어를 선택하셨습니다')
    elif language == '3':
        print('일본어를 선택하셨습니다')
    elif language=="영어" or language=="일본어" or language=="중국어":
        print(f'{language}를 선택하셨습니다')    
            
    print()
    print("=================")
    # Step 2: 메뉴 선택
    mode = input("메뉴를 선택하세요 (문제 풀기:1, 단어 추가:2, 단어장 출력:3): ")
    if mode not in ['1', '2', '3']:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue

    # Step 3: 선택한 언어에 따라 해당 단어장 설정
    if language == '1' or language == "영어":
        wordbook = eng
        word = "영어"
    elif language == '2' or language == "중국어":
        wordbook = chinese
        word = "중국어"
    elif language == '3' or language == "일본어":
        wordbook = japanese
        word = "일본어"

    # 문제 풀기
    if mode == '1':
        if not wordbook:
            print("단어장이 비어 있습니다. 먼저 단어를 추가하세요.")
            continue

        # 출제할 문제 수 입력
        n = int(input("몇 문제 풀까요? : "))
        # 단어장에서 무작위로 문제 선택
        questions = random.sample(wordbook, min(n, len(wordbook))) #n과 wordbook의 길이 중 더 작은 수를 사용
        # 문제 출제 방식 선택 (뜻 보고 단어 맞추기 / 단어 보고 뜻 맞추기)
        menu = input("뜻을 보고 맞출지, 단어를 보고 맞출지 입력 (뜻/단어): ")
        print()
        correct = 0  # 정답 수
        wrong = 0    # 오답 수

        # 문제 반복
        for i in range(len(questions)):
            word = questions[i]
            if menu == "뜻":
                # 뜻 제시 → 단어 입력
                answer = input(f"{i+1}번 문제-'{word['meaning']}'는?: ")
                if answer == word['word']:
                    print("정답입니다")
                    correct += 1
                else:
                    print("오답! 다시 입력해보세요")
                    answer = input(f"{i+1}번 문제 다시풀기!-'{word['meaning']}'는?: ")
                    if answer == word['word']:
                        print("정답입니다")
                        correct += 1
                    else:
                        print(f"오답! {i+1}번 정답: {word['word']}")
                        wrong += 1
            elif menu == "단어":
                # 단어 제시 → 뜻 입력
                answer = input(f"{i+1}번 문제 - '{word['word']}'의 뜻은? ")
                if answer == word['meaning']:
                    print("정답입니다")
                    correct += 1
                else:
                    print("오답! 다시 입력해보세요")
                    answer = input(f"{i+1}번 문제 다시풀기!-'{word['word']}'의 뜻은?: ")
                    if answer == word['meaning']:
                        print("정답입니다")
                        correct += 1
                    else:
                        print(f"오답! {i+1}번 정답: {word['meaning']}")
                        wrong += 1

        # 결과 출력
        print()
        print("===== 결과 =====")
        print(f"정답 : {correct}개")
        print(f"오답 : {wrong}개")
        break  # 문제 푼 뒤 프로그램 종료

    # 단어 추가
    elif mode == '2':
        n = int(input("추가할 단어 개수 입력 : "))
        for i in range(n):
            word = input("단어 입력: ")
            meaning = input("뜻 입력: ")
            # 단어장에 단어 추가 (딕셔너리 형태로 저장)
            wordbook.append({'word': word, 'meaning': meaning})

        # 단어장 출력
        print()
        print("단어장이 업데이트 되었습니다.")
        for i in range(len(wordbook)):
            entry = wordbook[i]
            print(str(i+1) + ". " + entry['word'] + " - " + entry['meaning'])
            # + 연산자를 문자열과 연결하기위해 문자열(str)로 변환

    # 단어장 출력
    elif mode == "3":
        if not wordbook:
            print("단어장이 비어 있습니다. 단어를 추가해주세요")
        else:
            print("현재 단어장: ")
            for i in range(len(wordbook)):
                entry = wordbook[i]
                print(str(i+1) + ". " + entry['word'] + " - " + entry['meaning'])
            print()
            break  # 단어장 출력 후 종료
