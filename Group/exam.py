import random

eng = []
chinese = []
japanese = []

while True:
    print()
    language = input("학습할 언어를 입력하세요: (1:영어, 2:중국어, 3:일본어, 0:종료): ")
    if language == "0":
        break
    if language not in ['1', '2', '3', '영어', '중국어', '일본어']:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue

    print()
    print("=================")
    mode = input("메뉴를 선택하세요 (문제 풀기:1, 단어 추가:2, 단어장 출력:3): ")
    if mode not in ['1', '2', '3']:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue

    # 언어별 단어장 선택
    if language == '1':
        wordbook = eng
        word = "영어"
    elif language == '2':
        wordbook = chinese
        word = "중국어"
    else:
        wordbook = japanese
        word = "일본어"

    if mode == '1':
        if not wordbook:
            print("단어장이 비어 있습니다. 먼저 단어를 추가하세요.")
            continue
        n = int(input("몇 문제 풀까요? : "))
        questions = random.sample(wordbook, min(n, len(wordbook)))
        menu = input("뜻을 보고 맞출지, 단어를 보고 맞출지 입력 (뜻/단어): ")
        print()
        correct = 0
        wrong = 0
        for i in range(len(questions)):
            word = questions[i]
            if menu == "뜻":
                answer = input(f"{i+1}번 문제-'{word['meaning']}'는?: ")
                if answer == word['word']:
                    print("정답입니다")
                    correct += 1
                else:
                    print(f"오답! 다시 입력해보세요")
                    answer = input(f"{i+1}번 문제 다시풀기!-'{word['meaning']}'는?: ")
                    if answer == word['word']:
                        print("정답입니다")
                        correct += 1
                    else:
                        print(f"오답! {i+1}번 정답: {word['word']}")
                        wrong += 1
            elif menu == "단어":
                answer = input(f"{i+1}번 문제 - '{word['word']}'의 뜻은? ")
                if answer == word['meaning']:
                    print("정답입니다")
                    correct += 1
                else:
                    print(f"오답! 다시 입력해보세요")
                    answer = input(f"{i+1}번 문제 다시풀기!-'{word['word']}'의 뜻은?: ")
                    if answer == word['meaning']:
                        print("정답입니다")
                        correct += 1
                    else:
                        print(f"오답! {i+1}번 정답: {word['meaning']}")
                        wrong += 1
        print()
        print("===== 결과 =====")
        print(f"정답 : {correct}개")
        print(f"오답 : {wrong}개")
        break

    elif mode == '2':
        n = int(input("추가할 단어 개수 입력 : "))
        for i in range(n):
            word = input("단어 입력: ")
            meaning = input("뜻 입력: ")
            wordbook.append({'word': word, 'meaning': meaning})
        print()
        print("단어장이 업데이트 되었습니다.")
        for i in range(len(wordbook)):
            entry = wordbook[i]
            print(str(i+1) + ". " + entry['word'] + " - " + entry['meaning'])

    elif mode == "3":
        if not wordbook:
            print("단어장이 비어 있습니다. 단어를 추가해주세요")
        else:
            print("현재 단어장: ")
            for i in range(len(wordbook)):
                entry = wordbook[i]
                print(str(i+1) + ". " + entry['word'] + " - " + entry['meaning'])
            print()
            break