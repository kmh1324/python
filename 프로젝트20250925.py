##dic = {}
##dic['name'] = '코딩이'
##dic['score'] = {'국어': 90, '영어': 82, '수학': 71}
##dic['address'] = '천안시 불당동'
##
##print(f'학생이름 : {dic["name"]}')
##print(f'학생성적 => \
##국어 {dic["score"]["국어"]}점 \
##수학 {dic["score"]["수학"]}점 \
##영어 {dic["score"]["영어"]}점')
##
##print(f'총점은 : {sum(dic["score"].values())} \
##평균은 : {sum(dic["score"].values()) / 3:.2f}')
##
##print(f'주소는 : {dic["address"]}')


##word_list = {
##    "coding": "코딩",
##    "soccer": "축구",
##    "loop": "반복문",
##    "condition": "조건"
##    }
##
##print("영어 단어 뜻 맞추기")
##
##for word in word_list:
##    answer = input(f"{word} : ")
##    if answer == word_list[word]:
##        print("정답입니다!!")
##    else :
##        print("틀렸습니다.")
##        break


##print('for문으로 변경한다면 ')
##
##print('학생성적 =>', end = ' ')
##for k, v in dic['score'].items():
##    print(f'{k} {v}점', end = ' ')
##print()
##total = sum(dic['score'].values())
##avg = total / len(dic['score'].values())
##
##print(f'총점은 : {total} 평균은 : {avg}')


##account_info = {
##    "first_account": {"id": "leesam0044", "password": "1234567"},
##    "second_account": {"id": "leesam0022", "password": "11223344"}
##    }
##
##while True:
##    input_id = input("아이디 : ")
##    input_ps = input("패스워드 : ")
##
##    correct_count = 0
##    for account in account_info:
##        id, ps = account_info[account].values()
##        if input_id == id and input_ps == ps:
##            correct_count = 1
##            break
##            
##    if correct_count:
##        print("로그인 성공!")
##    else :
##        print("로그인 실패!")
##        break


##registration = {}
##
##while True:
##    choice = input('1.회원가입 2.로그인 3.종료 중 입력 : ')
##    choice = int(choice)
##
##    if choice == 1:
##        print('회원가입을 시작합니다.')
##        red_id = input('아이디 입력 : ')
##        red_pw = input('패스워드 입력 : ')
##        red_pw2 = input('패스워드 다시 입력 : ')
##
##        if red_id in registration.keys():
##            print('아이디 중복됨, 다른 아이디로 회원가입하세요.')
##            continue
##
##        if red_pw != red_pw2:
##            print('패스워드가 틀림. 다시 회원가입하세요.')
##            continue
##
##        registration[red_id] = red_pw
##        print('회원가입 성공')
##
##    elif choice == 2:
##        print('로그인을 시작합니다.')
##        login_id = input('아이디 입력 : ')
##        login_pw = input('패스워드 입력 : ')
##
##        if login_id in registration.keys():
##            if registration[login_id] == login_pw:
##                print('로그인 성공')
##            else :
##                print('패스워드 틀림')
##        else :
##            print('아이디 없음')
##
##    elif choice == 3:
##        print('종료하겠습니다.')
##        break


##vocabulary = {}
##
##vocabulary['abstract'] = '추상화'
##vocabulary['variable'] = '변수'
##vocabulary['function'] = '함수'
##vocabulary['loop'] = '반복문'
##
##for key, value in vocabulary.items():
##    word = input(f'{key}의 뜻은? : ')
##
##    if word == value:
##        print('정답입니다')
##    else :
##        print('틀렸습니다ㅠㅠ')
##    print()


##import random
##vocabulary = {}
##
##vocabulary['abstract'] = '추상화'
##vocabulary['variable'] = '변수'
##vocabulary['function'] = '함수'
##vocabulary['loop'] = '반복문'
##
##vocab_shuffled = list(vocabulary.keys())
##random.shuffle(vocab_shuffled)
##for key in vocab_shuffled:
##    word = input(f'{key}의 뜻은? : ')
##
##    if word == vocabulary[key]:
##        print('정답입니다')
##    else :
##        print('틀렸습니다ㅜㅜ')
##    print()


##array = []
##
##for i in range(0, 20, 2):
##    array.append(i * i)
##
##print(array)


##array = [i * i for i in range(0, 20, 2)]
##
##print(array)


##array = ["사과", "자두", "초콜릿", "바나나", "체리"]
##output = [fruit for fruit in array if fruit != "초콜릿"]
##
##print(output)


##number = int(input("정수 입력> "))
##
##if number % 2 == 0:
##    print("""\
##        입력한 문자열은 {}입니다.
##        {}는(은) 짝수입니다.""".format(number, number))
##
##else :
##    print("""\
##        입력한 문자열은 {}입니다.
##        {}는(은) 홀수입니다.""".format(number, number))


##number = int(input("정수 입력> "))
##
##if number % 2 == 0:
##    print("""입력한 문자열은 {}입니다.
##{}는(은) 짝수입니다.""".format(number, number))
##
##else:
##    print("""입력한 문자열은 {}입니다.
##{}는(은) 홀수입니다.""".format(number, number))


##number = int(input("정수 입력> "))
##
##if number % 2 == 0:
##    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number, number))
##
##else :
##    print("입력한 문자열은 {}입니다.\n{}는(은) 짝수입니다.".format(number, number))


##test = (
##    "이렇게 입력해도 "
##    "하나의 문자열로 연결되어 "
##    "생성됩니다."
##)
##
##print("test:", test)
##print("type(test):", type(test))


##number = int(input("정수 입력> "))
##if number % 2 == 0:
##    print(("입력한 문자열은 {}입니다.\n"
##           "{}는 짝수입니다."
##           ).format(number, number))
##
##else :
##    print(("입력한 문자열은 {}입니다.\n"
##           "{}는 홀수입니다."
##           ).format(number, number))


number = int(input("정수 입력> "))

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다."
        "{}는(은) 짝수입니다."
        ]).format(number, number))

else :
    print("\n".join([
        "입력한 문자열은 {}입니다."
        "{}는(은) 짝수입니다."
        ]).format(number, number))
    
