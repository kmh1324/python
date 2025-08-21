##num = 1357
##
##temp = num
##temp %= 10
##print(temp)
##num //= 10
##
##temp = num
##temp %= 10
##print(temp)
##num //= 10
##
##temp = num
##temp %= 10
##print(temp)
##num //= 10
##
##temp = num
##temp %= 10
##print(temp)


##num1, num2, num3, num4, num5 = input("숫자 5개를 입력해주세요 : ").split()
##
##average = (int(num1) + int(num2) + int(num3) + int(num4) + int(num5)) / 5
##
##print(f"{average:.03f}")


##text = input("문자열을 입력해주세요 : ")
##text_split = text.split()
##
##text1 = text_split[0]
##text1 = text1[0:1].upper() + text1[1:] + " "
##text = text1
##
##text2 = text_split[1]
##text2 = text2[0:1].upper() + text2[1:] + " "
##text += text2
##
##print(text)


##num1 = float(input("첫 번째 숫자 입력 : "))
##num2 = float(input("두 번째 숫자 입력 : "))
##
##print(f"num1 > num2 = {num1 > num2}")
##print(f"num1 < num2 = {num1 < num2}")
##
##print(f"num1 >= num2 = {num1 >= num2}")
##print(f"num1 <= num2 = {num1 <= num2}")
##
##print(f"num1 == num2 = {num1 != num2}")
##print(f"num1 != num2 = {num1 != num2}")


##num1 = float(input("첫 번째 숫자 입력 : "))
##num2 = float(input("두 번째 숫자 입력 : "))
##num3 = float(input("세 번째 숫자 입력 : "))
##
##ascending = num1 < num2 < num3
##descending = num1 > num2 > num3
##
##print(f"{type(ascending)}, {type(descending)}")
##print(f"num1<num2<num3 = {ascending}")
##print(f"num1>num2>num3 = {descending}")


##num = int(input("숫자를 입력해주세요 : "))
##print(f"{num < 100}")


##num = int(input("숫자를 입력해주세요 : "))
##print(f"{30 < num < 60}")


##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))
##
##print(f"둘 다 양수? = {num1 > 0 and num2 > 0}")
##print(f"하나라도 양수? = {num1 > 0 or num2 > 0}")
##
##print(f"num1은 0인가? = {not num1}")
##print(f"num2는 0인가? = {not num2}")


##num = int(input("숫자를 입력해주세요 : "))
##print(f"{num == 0 or num == 10 or num == 100}")


##num = int(input("숫자를 입력해주세요 : "))
##print(f"{num % 2 == 1 or num % 8 == 0 and num != 0}")


##level = int(input('레벨을 입력해 주세요 : '))
##
##if level == 15:
##    print("현재 래밸은 15입니다.")
##
##if level != 15:
##    print("현재 레벨은 15가 아닙니다.")


##level = int(input('레벨을 입력해 주세요 : '))
##
##if level >= 10:
##    print("현재 래밸은 10을 넘습니다.")
##
##if level <= 20:
##    print("현재 래밸은 20보다 작습니다.")


##level = int(input('레벨을 입력해 주세요 : '))
##if level > 10:
##    print("현재 래밸은 10을 넘습니다.")
##
##if level < 20:
##    print("현재 래밸은 20보다 작습니다.")
##
##print("Loading...")


##answer = "이샘_코딩_학원"
##word = input("단어를 입력해주세요 : ")
##
##if word in answer:
##    print("해당 단어가 포함되어 있습니다.")
##
##if word not in answer:
##    print("해당 단어가 포함되어 있지 않습니다.")


##level = int(input('레벨을 입력해 주세요 : '))
##if level < 30:
##    print("레벨이 모자릅니다.")
##
##if 30 <= level <= 40:
##    print("적정 레벨입니다.")
##
##if level > 40:
##    print("레벨이 너무 높습니다.")


##month = int(input('몇 월인지 입력해주세요 : '))
##
##if month >= 3 and month <= 5:
##    season = "봄"
##
##if month >= 6 and month <= 8:
##    season = "여름"
##
##if month >= 9 and month <= 11:
##    season = "가을"
##
##if month >= 12 or month <= 2:
##    season = "겨울"
##
##print(f"지금 계절은 {season}입니다.")


##number = int(input("숫자를 입력해주세요 : "))
##
##if number % 3 == 0 or number % 5 == 0:
##    print("{}는 3이나 5의 배수입니다.".format(number))


##num = int(input("숫자를 입력해주세요 : "))
##
##if num % 2 == 0:
##    print(f'{num}는 짝수입니다.')


##temperature = int(input("현재 온도를 입력해주세요 : "))
##if temperature < 25:
##    info = "시원한 날씨"
##
##if 25 <= temperature > 30:
##    info = "따뜻한 날씨"
##
##if temperature >= 30:
##    info = "더운 날씨"
##print(f"날씨 상태: {info}")

































