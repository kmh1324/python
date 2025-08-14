##nut1 = '밤양갱'
##nut2 = "달디단 밤양갱"
##nut3 = """달디달고 달디달고,
##달디단 밤양갱 밤양갱
##내가 먹고 싶었던 건 달디단, 밤양갱, 밤양갱이야"""


##sweat = '달디'
##sweat2 = sweat * 10
##number = 255
##message = sweat2 + ' ' + '단 방양갱' + str(number) + '개'
##print(message)


##line = "=" * 20
##header = "밤양갱 대박 세일"
##footer = "놓치지 마세요!"
##message = line + "\n" + header + "\n" + line + "\n" + footer + "\n" + line
##print(message)


##id = input("아이디 : ")
##password = input("비밀번호 : ")
##message = '당신의 아이디는 "' + str(id) + '"이며,' + '비밀번호는 "' + str(password) + '" 입니다.'
##print(message)


##word = "문자열과 인덱스"
##
##print(word[0])
##print(word[3])
##print(word[5])
##print(word[-1])


##snack = "떡볶이 순대 튀김"
##setmenu = snack[0] + snack[4] + snack[7]
##
##print(setmenu)


##word = "부분만 바꾸려고 하면 에러가 나요"
##print(word)

##word[0] = "수"
##word = "새로 만들어 덮어쓰기는 가능"
##print(word)


##word = "슬라이싱으로 다양하게 문자를 잘라봅시다"
##
##print(word[0:4])
##print(word[7:9])
##print(word[:12])
##print(word[::3])
##print(word[::-3])


##song = "록도닳 고르마 이산두백 과물해동"
##
##reverse = song[::-1]
##
##print(reverse)


##song = "동해물과 백두산이 마르고 닳도록"
##
##part_song = song[:4]
##print(part_song)
##part_song = song[5:13]
##print(part_song)
##part_song = song[14:]
##print(part_song)


##str = input("문자열을 입력하세요 : ")
##print("%s" % (str[1::2]))


##num = input("주민번호를 입력하세요(-포함):")
##print("%s" % (num[2:6]))


##input = "타파에벅서이썬스나짱만스"
##output = input[11] + input[0] + input[3] + input[7] + input[2] + input[4] + input[10] + input[8]
##print(output)


##part_1 = "동해물과 백두산이 마르고 닳도록"
##part_2 = "하느님이 보우하사 우리나라 만세. "
##part_3 = "무궁화 삼천리 화려 강산"
##part_4 = "대한 사람, 대한으로 길이 보전하세."
##print(part_2[15:17])
##print(part_4[17:19])


##part_1 = "동해물과 백두산이 마르고 닳도록"
##part_2 = "하느님이 보우하사 우리나라 만세."
##part_3 = "무궁화 삼천리 화려 강산"
##part_4 = "대한 사람, 대한으로 길이 보전하세."
##
##song = part_1 + "\n" + part_2 + "\n" + part_3[:11] + "강세" + "\n" + part_4 + "\n"
##print(song)


##poison = "이 파이썬 문장에는 독이 있어!"
##print("독" in poison)
##print("약" in poison)


##number = 12345678
##print(1 in number)


##number = "12345678"
##print(1 in number)


##print("1" in number)


##message = "다른 연산자씨리 섞어쓰는 것도 가능해."
##print("연산자" in message[2:10])
##print("연산자" not in "정말 다양한 방법으로" + "연산자를 쓸 수 있어")


##string = "문자열 함수 & 문자열 함수"
##print(string.find("자열"))
##print(string.rfind("함수"))
##print(string.find("자열"))
##print(string.rfind("함수"))


##string = "Hello Python"
##number = "12345"
##print(string.isalpha())
##print(string.isnumeric())
##print(number.isalpha())
##print(number.isnumeric())


##bab = "국밥 컵밥 초밥 김밥 비빔밥"
##
##print("가장 앞에 있는 밥은 " + str(bab.find("밥"))+"번째!")
##
##print("가장 뒤에 있는 밥은 " + str(bab.rfind("밥"))+"번째!")


##eng = "FunnyPython"
##kor = "신나는파이썬"
##blank = "B L A N K"
##
##print(eng.isalpha())
##print(kor.isalpha())
##print(blank.isalpha())


##num = "20240505"
##date = "2024.05.05"
##
##print(num.isnumeric())
##print(date.isnumeric())


##test = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다."
##print("첫번째 완두콩은 " + str(test.find("완두콩")) + "번째에 있습니다.")
##print("두번째 완두콩은 " + str(test.rfind("완두콩")) + "번째에 있습니다.")


##test = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다."
##part_1 = test[test.find("완"):test.find("완") + 11]
##part_2 = test[test.rfind("강"):test.rfind("강") + 11]
##print(part_1)
##print(part_2)


email = input("아이디를 입력해주세요 : ")
print("이 이메일의 아이디는 " + email[:email.find("@")] + "입니다.")
