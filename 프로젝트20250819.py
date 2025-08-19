##tips = "len 함수로 문자열의 갯수를 세봅시다."
##print(len(tips))
##number = 15335
##print(len(number))


##year = input("태어난 해를 입력해주세요 : ")
##month = input("태어난 월를 입력해주세요 : ")
##day = input("태어난 일를 입력해주세요 : ")
##date = "{}년 {}월 {}일".format(year, month, day)
##print("당신의 생일은 " + date + "입니다. Happy birthday!")


##num1 = f'{10}/{20}'
##num2 = f'[{10.10}/{20.20}]'
##print(num1)
##print(num2)
##
##pi = 3.14
##num3 = f'[{pi:4.1f}/{pi:010.0f}]'
##print(num3)
##
##str1 = "Python"
##str2 = f'[{str1:10s}/{str1:010s}]'
##print(str2)


##title = input("영화 제목을 입력하세요 : ")
##open = input("개봉 연도를 입력하세요 : ")
##actor = input("주연 배우를 입력하세요 : ")
##info = "{}은(는) {}년에 개봉한 {} 주연의 영화입니다.".format(title, open, actor)
##print(info)


##id = input("아이디를 입력해주세요(6글자 이상): ")
##print("암호화된 아이디: %s" % (id[:3] + "*****"))


##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))
##print(f"num1 + num2 = {num1 + num2}")
##print(f"num1 - num2 = {num1 - num2}")
##print(f"num1 * num2 = {num1 * num2}")
##print(f"num1 / num2 = {num1 / num2:.2f}")


##num = int(input("숫자 입력 : "))
##print(f"{num} + 50 = {num + 50}")
##print(f"{num} - 50 = {num - 50}")
##print(f"{num} * 50 = {num * 50}")
##print(f"{num} / 50 = {num / 50:.3f}")


##w1 = 3
##w2 = 4
##h = 5
##print(f"사다리꼴의 넓이는 ({w1} + {w2}) * {h} / {2} = {(w1 + w2) * h / 2:.1f}")


##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))
##
##print(f"num1 // num2 = {num1 // num2}")
##print(f"num1 % num2 = {num1 % num2}")
##print(f"num1 ** num2 = {num1 ** num2}")


##num = int(input("숫자 입력 : "))
##
##print(f"{num // 4}")
##print(f"{num % 4}")
##print(f"{num ** 4}")


##kg = int(input("몸무게(kg)를 입력하세요 : "))
##m = float(input("키(m)를 입력하세요 : "))
##
##print(f"BMI 지수는 {kg / (m**2):.2f}")


##sec = int(input("초 입력 : "))
##
##min = sec // 60
##sec = sec% 60
##
##hour = min // 60
##min = min % 60
##
##day = hour // 24
##hour = hour % 24
##
##print(f"{day}일{hour}시간{min}분{sec}초")


##number = int(input("세 자리 숫자 입력 : "))
##
##number1 = number % 10
##number = number // 10
##
##number10 = number % 10
##number = number // 10
##number100 = number % 10
##print(f"백의 자리 : {number100}")
##print(f"십의 자리 : {number10}")
##print(f"일의 자리 : {number1}")


##price = int(input("물건의 가격을 입력합니다 : "))
##change = 1000 - price
##
##m500 = change // 500
##change = change % 500
##
##m100 = change // 100
##change = change % 100
##
##m50 = change // 50
##change = change % 50
##
##m10 = change // 10
##change = change % 10
##
##print(f"500원 {m500}개")
##print(f"100원 {m100}개")
##print(f"50원 {m50}개")
##print(f"10원 {m10}개")

##
##num = int(input("다섯 자리 숫자를 입력합니다 : "))
##
##num1 = num % 10
##num = num // 10
##
##num10 = num % 10
##num = num // 10
##
##num100 = num % 10
##num = num // 10
##
##num1000 = num % 10
##num = num // 10
##
##num10000 = num % 10
##
##print(f"만의 자리 : {num10000}")
##print(f"천의 자리 : {num1000}")
##print(f"백의 자리 : {num100}")
##print(f"십의 자리 : {num10}")
##print(f"일의 자리 : {num1}")
##


##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))
##num3 = int(input("세 번째 숫자 입력 : "))
##
##print(f"10000 += num1 -> {10000 + num1}")
##print(f"10000 -= num2 -> {10000 - num2}")
##print(f"10000 *= num3 -> {10000 * num3}")


##txt = input("문자열 입력 : ")
##num = input("숫자 입력 : ")
##
##txt2 = txt
##txt += num
##txt2 *= int(num)
##
##print(txt)
##print(txt2)


##num1, num2, num3 = input("숫자 3개를 입력해주세요 : ").split()
##
##num = 100
##num -= int(num1) + int(num2) + int(num3)
##print(num)


##num = int(input("숫자를 입력해주세요 : "))
##txt = "삐약"
##txt *= num
##
##print(txt)


##egg = int(input("계란 개수 입력 : "))
##tmp = egg
##tmp %= 30
##egg //= 30
##print("계란 {0}판, 나머지 {1}개".format(egg, tmp))


first = int(input("피자를 몇 등분할까? : "))
second = int(input("한조각을 몇 등분할까? : "))
pizza = 100
pizza /= first
pizza /= second

print("이 조각은 피자 한 판의 {0:.2f}".format(pizza))
