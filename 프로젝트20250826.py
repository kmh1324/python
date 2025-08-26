##num = int(input("숫자를 입력해주세요 : "))
##
##if num % 2 == 0:
##    print(f'{num}는 짝수입니다.')


##temperature = int(input("현재 온도를 입력해주세요 : "))
##if temperature < 25:
##    info = "시원한 날씨"
##
##if 25 <= temperature < 30:
##    info = "따뜻한 날씨"
##
##if temperature >= 30:
##    info = "더운 날씨"
##    
##print(f"날씨 상태: {info}")


##str = input("문자열을 입력하세요: ")
##
##if " " in str:
##    print("공백이 포함되어 있습니다.")
##
##if " " not in str:
##    print("공백이 포함되어 있지 않습니다.")


##age = int(input("나이를 입력해주세요 : "))
##
##if age >= 15:
##    print("15세 관람가")
##if age >= 12:
##    print("12세 관람가")
##print("전체관람가")


##apple = int(input("사과의 개수를 입력해 주세요: "))
##if apple > 0:
##    print("사과가 있습니다.")
##
##else:
##    print("사과가 없습니다.")


##apple = int(input("사과의 개수를 입력해 주세요:"))
##
##if apple == 10:
##    print("사과는 10개 있습니다.")
##
##elif apple == 0:
##    print("사과는 하나도 없습니다.")


##text = input("문장을 입력하세요: ")
##
##if ' ' in text:
##    print("공백이 포함되어 있습니다.")
##else:
##    print("공백이 포함되어 있지 않습니다.")


##string = input("문자를 입력하세요: ")
##
##if string.isalpha():
##    print("알파벳 혹은 한글입니다.")
##elif string.isnumeric:
##    print("숫자입니다.")
##else:
##    print("숫자입니다.")


##height = 170
##
##if height > 150:
##    print("키가 150 이상입니다.")
##if height > 160:
##    print("키가 160 이상입니다.")


##height = 170
##if height > 150:
##    print("키가 150 이상입니다.")
##elif height > 160:
##    print("키가 160 이상입니다.")    


##height = int(input("키를 입력해주세요:"))
##
##if height > 150:
##    print("키가 150이상입니다.")
##elif height > 160:
##    print("키가 160 이상입니다.")
##else:
##    print("키가 150 미만입니다.")


##height = int(input("키를 입력해주세요: "))
##
##if height > 170:
##    print("키가 170 이상입니다.")
##elif height > 160:
##    print("키가 160 이상입니다.")
##elif height > 150:
##    print("키가 150 이상입니다.")
##else:
##    print("키가 150 미만입니다.")


##num1 = float(input("첫 번째 숫자: "))
##num2 = float(input("두 번째 숫자: "))
##num3 = float(input("세 번째 숫자: "))
##
##average = (num1 + num2 + num3) / 3
##
##if average >= 50:
##    print("평균이 50 이상입니다.")
##else:
##    print("평균이 50 미만입니다.")


##email = input("이메일 주소를 입력해주세요: ")
##if '@' in email and '.' in email:
##    print("유효한 이메일 주소입니다.")
##elif '@' in email:
##    print("'.'가 없습니다.")
##elif '.' in email:
##    print("'@'가 없습니다.")
##else:
##    print("유효하지 않은 이메일 주소입니다.")


##url = input("URL을 입력하세요: ")
##if url.find("http://")>=0:
##    print("HTTP 프로토콜입니다.")
##elif url.find("https://")>=0:
##    print("HTTPS 프로토콜입니다.")
##elif url.find("ftp://")>=0:
##    print("FTP 프로토콜입니다.")
##else: 
##    print("알 수 없는 프로토콜입니다.")


##key= input("방향키를 입력해주세요 (w/a/s/d) : ")
##
##if 'w' in key:
##    print("위 방향키를 입력하셨습니다.")
##    
##elif 'a' in key:
##    print("좌 방향키를 입력하셨습니다.")
##
##elif 'd' in key:
##    print("우 방향키를 입력하셨습니다.")
##
##elif 's' in key:
##    print("아래 방향키를 입력하셨습니다.")
##
##else :
##    print("잘못 입력하셨습니다.")


##num = int(input("숫자를 입력해주세요: "))
##if num > 0:
##    print("number은 양수입니다.")
##elif num == 0:
##    print("number은 0입니다.")
##else :
##    print("number은 음수입니다.")
##
##if num % 2 == 0:
##    print("number은 짝수입니다.")
##else :
##    print("number은 홀수입니다.")


##print("숫자를 입력해주세요.")
##num = int(input())
##
##if 10 <= num <= 99:
##    print("두자리 숫자입니다.")
##else :
##    print("두자리 숫자가 아닙니다.")


##num = int(input("숫자를 입력해주세요 : "))
##
##if num % 3 == 0:
##    print("이 숫자는 3의 배수입니다.")
##if num % 6 == 0:
##    print("이 숫자는 6의 배수입니다.")
##if num % 9 == 0:
##    print("이 숫자는 9의 배수입니다.")


##text = input("알파벳을 입력해주세요 : ")
##
##if 'a' <= text <= 'z':
##    print("소문자 입니다.")
##
##if 'A' <= text <= 'Z':
##    print("대문자 입니다.")


##print("숫자 1과 숫자 2를 입력해주세요.")
##number1 = int(input())
##number2 = int(input())
##
##if number1 > number2 :
##    print("숫자 1이 숫자 2보다 큽니다.")
##else:
##    if number1 < number2:
##        print("숫자 2가 숫자 1보다 큽니다.")
##    else:
##        print("숫자 1과 숫자 2가 같습니다.")


##print("숫자 1과 숫자 2를 입력해주세요: ")
##number1 = int(input())
##number2 = int(input())
##
##if number1 > number2 :
##    print("숫자 1이 숫자 2보다 큽니다.")
##elif number1 > number2 :
##    print("숫자 2가 숫자 1보다 큽니다.")
##else:
##    print("숫자 1과 숫자 2가 같습니다.")


##score = 75
##
##if score > 90:
##    print("성적은 A등급 입니다.")
##elif score > 80:
##    print("성적은 B등급 입니다.")
##elif score > 70:
##    print("성적은 C등급 입니다.")
##elif score > 60:
##    print("성적은 D등급 입니다.")
##else:
##    print("성적은 F등급 입니다.")


##weight = int(input('무게를 입력해주세요 : '))
##express = input('특송여부 (y/n) : ')
##domestic = input('국내 배송 여뷰 (y/n) : ')
##
##if weight <= 2 and (expresss == 'y' or domestic == 'y'):
##    print("무료 배송입니다.")
##elif weight <= 5 and (express == 'y' or domestic == 'y'):
##    print("유로 배송입니다.")
##else:
##    print("배송 불가합니다.")


##player_atk = int(input("현재 공격력 : "))
##player_exp = 10
##monster_atk = 100
##
##if monster_atk > player_atk :
##    print("몬스터의 승리!")
##    print("경험치를 잃었다...")
##    player_exp -= 5
##elif monster_atk < player_atk :
##    print("플레이어의 승리!")
##    print("경험치를 얻었다!!")
##    player_exp += 5
##else:
##    print("몬스터와의 무승부..")
##    print("아무런 일도 일어나지 않았다.")
##
##print(f"현재 경험치 : {player_exp} 레벨업까지 : {100 - player_exp}")



##print("[계산기 프로그램]")
##
##choice = input("연산자를 입력해주세요. (+,-,*,/): ")
##
##num1 = float(input("첫 번째 숫자 : "))
##num2 = float(input("두 번째 숫자 : "))
##
##if choice == '+':
##    resulte = num1 + num2
##    print(f"결과: {num1} + {num2} = {resulte}")
##    
##elif choice == '-':
##    resulte = num1 - num2
##    print(f"결과: {num1} - {num2} = {resulte}")
##    
##elif choice == '*':
##    resulte = num1 * num2
##    print(f"결과: {num1} * {num2} = {resulte}")
##    
##elif choice == '/':
##    if num2 != 0:
##        resulte = num1 / num2
##        print(f"결과: {num1} / {num2} = {resulte}")
##    else:
##        print("오류: 0으로 나눌 수 없습니다.")
##else:
##    print("연산자를 잘못 입력하셨습니다.")


##score = int(input("숫자를 입력해주세요.(0~100) : "))
##if 45 <= score <= 55:
##    print("Perpect!!")
##elif 35 <= score <= 65:
##    print("Excellent!!")
##else:
##    print("good!!")


##print("연도를 입력해주세요")
##year = int(input())
##if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
##    print("윤년입니다.")
##else:
##    print("윤년이 아닙니다.")


num1 = int(input("첫번째 숫자를 입력해주세요 : "))
num2 = int(input("두번째 숫자를 입력해주세요 : "))
num3 = int(input("세번째 숫자를 입력해주세요 : "))

if num1 < num2 and num1 < num3:
    first = num1
    if num2 < num3:
        second = num2
        three = num3
    else:
        second = num3
        three = num2
elif num2 < num1 and num2 < num3:
    first = num2
    if num1 < num3:
        second = num1
        three = num3
    else:
        second = num3
        three = num1
else:
    first = num3
    if num1 < num2:
        second = num1
        three = num2
    else:
        second = num2
        three = num1

print(f"{num1} {num2} {num3}")
