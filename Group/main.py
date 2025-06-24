import random

# 단어장 데이터 저장용 (언어별 구분 가능하게 dict 사용)
chinese = []
japanese = []
eng = []

while True:
    # Step 1: 언어 설정
    print()
    language = input("학습할 언어를 입력하세요:(영어-1/중국어-2/일본어-3/중단-0): ")
    # 잘못 입력했을떄
    if language not in ["영어", "중국어", "일본어", '1', '2', '3', '0']:
        language = input("설정 할 언어를 다시 입력해주세요: ")
        if language == '1':
            print('영어를 선택하셨습니다')
        if language == '2':
            print('중국어를 선택하셨습니다')
        if language == '3':
            print('일본어를 선택하셨습니다')
        elif language=="영어" or language=="일본어" or language=="중국어":
            print(f'{language}를 선택하셨습니다')    
            
    else:
        if language == '1':
            print('영어를 선택하셨습니다')
        if language == '2':
            print('중국어를 선택하셨습니다')
        if language == '3':
            print('일본어를 선택하셨습니다')
        elif language=="영어" or language=="일본어" or language=="중국어":
            print(f'{language}를 선택하셨습니다')


    if language == '0':
        break

    print("=================")
    # level = input("자신의 레벨을 입력하세요 (상/중상/중/중하/하): ")

    # Step 2: 메뉴 선택
    print()
    mode = input("메뉴를 선택하세요 (문제 풀기:1, 단어 추가:2, 단어장 출력:3): ")
    #오류났을때
    if mode not in ['1', '2', '3']:
        mode = input("메뉴를 다시 선택해주세요: ")

    #정상작동
    else:
        # 문제풀기
        if mode == '1':
            correct = 0
            wrong = 0
            # 영어일때
            if language == '영어' or language == '1':
                if not eng:
                    print("❗ 단어장이 비어 있습니다. 먼저 단어를 추가하세요.")
                else: 
                    n = int(input("몇 문제 풀까요? : "))
                    # 리스트에서 단어 추출
                    questions = random.sample(eng, min(n, len(eng)))
                    menu = input("뜻을 보고 맞출지, 단어를 보고 맞출지 입력 (뜻/단어): ")
                    # (questions, 1) == (반복대상, 시작번호)
                    for i, word in enumerate(questions, 1):
                        if menu == "뜻":
                            answer = input(f"{i}번 문제-'{word['meaning']}'는?: ")
                            # strip() = 문자열 양쪽 공백 삭제
                            if answer.strip() == word['word']:
                                print("✅ 정답!")
                                correct += 1
                            else:
                                # 다시 풀기
                                print(f"❌ 오답! 다시 입력해보세요")
                                answer = input(f"{i}번 문제 다시풀기!-'{word['meaning']}'는?: ")
                                if answer.strip() == word['word']:
                                    print("✅ 정답!")
                                    correct += 1
                                else:
                                    print(f"❌ 오답! {i}번 정답: {word['word']}")
                                    wrong += 1

                        elif mode == "단어":
                            answer = input(f"{i}번 문제 - '{word['word']}'의 뜻은? ")

                            if answer.strip() == word['meaning']:
                                print("✅ 정답!")
                                correct += 1
                            else:
                                print(f"❌ 오답! 다시 입력해보세요")
                                answer = input(f"{i}번 문제 다시풀기!-'{word['word']}'의 뜻은?: ")

                                if answer.strip() == word['meaning']:
                                    print("✅ 정답!")
                                    correct += 1
                                else:
                                    print(f"❌ 오답! {i}번 정답: {word['meaning']}")
                                    wrong += 1
            #중국어일떄
            elif language == '중국어' or language == '2':
                if not chinese:
                    print("❗ 단어장이 비어 있습니다. 먼저 단어를 추가하세요.")
                else:
                    n = int(input("몇 문제 풀까요? : "))
                    # 리스트에서 단어 추출
                    questions = random.sample(chinese, min(n, len(chinese)))
                    menu = input("뜻을 보고 맞출지, 단어를 보고 맞출지 입력 (뜻/단어): ")

                    # (questions, 1) == (반복대상, 시작번호)
                    for i, word in enumerate(questions, 1):
                        if menu == "뜻":
                            answer = input(f"{i}번 문제-'{word['meaning']}'는?: ")

                            # strip() = 문자열 양쪽 공백 삭제
                            if answer.strip() == word['word']:
                                print("✅ 정답!")
                                correct += 1
                            else:
                                # 다시 풀기
                                print(f"❌ 오답! 다시 입력해보세요")
                                answer = input(f"{i}번 문제 다시풀기!-'{word['meaning']}'는?: ")

                                if answer.strip() == word['word']:
                                    print("✅ 정답!")
                                    correct += 1
                                else:
                                    print(f"❌ 오답! {i}번 정답: {word['word']}")
                                    wrong += 1
                        elif mode == "단어":
                            answer = input(f"{i}번 문제 - '{word['word']}'의 뜻은? ")

                            if answer.strip() == word['meaning']:
                                print("✅ 정답!")
                                correct += 1
                            else:
                                print(f"❌ 오답! 다시 입력해보세요")
                                answer = input(f"{i}번 문제 다시풀기!-'{word['word']}'의 뜻은?: ")

                                if answer.strip() == word['meaning']:
                                    print("✅ 정답!")
                                    correct += 1
                                else:
                                    print(f"❌ 오답! {i}번 정답: {word['meaning']}")
                                    wrong += 1
            #일본어 일때
            elif language == '일본어' or language == '3':
                if not japanese:
                    print("❗ 단어장이 비어 있습니다. 먼저 단어를 추가하세요.")
                else:
                    n = int(input("몇 문제 풀까요? : "))
                    # correct = 0
                    # wrong = 0
                    # 리스트에서 단어 추출
                    questions = random.sample(japanese, min(n, len(japanese)))
                    menu = input("뜻을 보고 맞출지, 단어를 보고 맞출지 입력 (뜻/단어): ")

                    # (questions, 1) == (반복대상, 시작번호)
                    for i, word in enumerate(questions, 1):
                        if menu == "뜻":
                            answer = input(f"{i}번 문제-'{word['meaning']}'는?: ")

                            # strip() = 문자열 양쪽 공백 삭제
                            if answer.strip() == word['word']:
                                print("✅ 정답!")
                                correct += 1
                            else:
                                # 다시 풀기
                                print(f"❌ 오답! 다시 입력해보세요")
                                answer = input(f"{i}번 문제 다시풀기!-'{word['meaning']}'는?: ")

                                if answer.strip() == word['word']:
                                    print("✅ 정답!")
                                    correct += 1
                                else:
                                    print(f"❌ 오답! {i}번 정답: {word['word']}")
                                    wrong += 1
                        elif mode == "단어":
                            answer = input(f"{i}번 문제 - '{word['word']}'의 뜻은? ")

                            if answer.strip() == word['meaning']:
                                print("✅ 정답!")
                                correct += 1
                            else:
                                print(f"❌ 오답! 다시 입력해보세요")
                                answer = input(f"{i}번 문제 다시풀기!-'{word['word']}'의 뜻은?: ")

                                if answer.strip() == word['meaning']:
                                    print("✅ 정답!")
                                    correct += 1
                                else:
                                    print(f"❌ 오답! {i}번 정답: {word['meaning']}")
                                    wrong += 1



            print()
            print("===== 결과 =====")
            print(f"정답 : {correct}개")
            print(f"오답 : {wrong}개")


    if mode == '2':
        print()
        n = int(input("추가할 단어 개수 입력 : "))
        if language=="영어":
            for i in range(n):
                word = input("단어 입력: ")
                meaning = input("뜻 입력: ")
                eng.append({'word': word, 'meaning': meaning})
            print()
            print("단어장이 업데이트 되었습니다.")
            for i, entry in enumerate(eng, 1):
                print(f"{i}. {entry['word']} - {entry['meaning']}")
        if language=="중국어":
            for i in range(n):
                word = input("단어 입력: ")
                meaning = input("뜻 입력: ")
                chinese.append({'word': word, 'meaning': meaning})
            print()
            print("단어장이 업데이트 되었습니다.")
            for i, entry in enumerate(chinese, 1):
                print(f"{i}. {entry['word']} - {entry['meaning']}")
        if language=="일본어":
            for i in range(n):
                word = input("단어 입력: ")
                meaning = input("뜻 입력: ")
                japanese.append({'word': word, 'meaning': meaning})
            print()
            print("단어장이 업데이트 되었습니다.")
            for i, entry in enumerate(japanese, 1):
                print(f"{i}. {entry['word']} - {entry['meaning']}")



    elif mode == "3":
        if language=="영어":
            if not eng:
                print("단어장이 비어 있습니다.")
            else:
                print("현재 단어장: ")
                for i, entry in enumerate(eng, 1):
                    print(f"{i}. {entry['word']} - {entry['meaning']}")
        if language=="중국어":
            if not chinese:
                print("단어장이 비어 있습니다.")
            else:
                print("현재 단어장: ")
                for i, entry in enumerate(chinese, 1):
                    print(f"{i}. {entry['word']} - {entry['meaning']}")
        if language=="일본어":
            if not japanese:
                print("단어장이 비어 있습니다.")
            else:
                print("현재 단어장: ")
                for i, entry in enumerate(japanese, 1):
                    print(f"{i}. {entry['word']} - {entry['meaning']}")
                    
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")