##print("안녕하세요")
##print("안녕하세요")
##print("안녕하세요\n")
##print("안녕하세요\n")
##print('안녕하세요', end = "")
##print("안녕하세요", end = '')
##print("\", \'는 따옴표의 대체 기호입니다.")
##print("\\n은 줄바꿈의 대체 기호입니다.")
##print("따옴표는 '역할'이 같아요")
##print('따옴표는 "역할"이 같아요')
##print('따옴표는 "역할'이 같아요")
##print("따옴표는 "역할"이 같아요")
##apple = "사과"
##print(apple, 1, "상자", sep = "++")
##apple = "사과"
##print(apple, 1, "상자")
##print("이샘")
##print("코딩")
##print("학원")
##print("이샘", end = "")
##print("코딩", end = "")
##print("학원", end = "!")
##num1 = 10
##print(num1, type(num1))
##num2 = 3.14
##print(num2, type(num2))
##m_str = "안녕하세요"
##print(m_str, type(m_str))
##print(1+1, type(1+1))
##print(0.3 + 2.04, type(0.3 + 2.04))
##print(1 + 2.3, type(1 + 2.3))
##print('"이샘코딩학원"')
##print(1, 2, 3, sep = "+", end = "=6")
##num1 = 17
##print(num1)
##print("10진수 17 = %d" %(num1))
##print("10진수 17의 8진수 = %o" %(num1))
##print("10진수 17의 16진수 = %x" %(num1))
##num2 = 97
##print("%d %c" %(num2, num2))
##float1 = 1234.567
##print(float1)
##print("기본 출력 %f" % (float1))
##print("지수표기법 %e" % (float1))
##print("소수 둘째자리까지 %.2f" % (float1))
##txt1 = "Hello"
##txt2 = "World"
##
##print("기본 출력\n%s %s" % (txt1, txt2))
##print("7칸 출력\n%7s %7s" % (txt1, txt2))
##num1 = 17
##print(num1)
##print("10진수 17 = {0}".format(num1))
##print("10진수 17의 8진수 = {0:o}".format(num1))
##print("10진수 17의 16진수 = {0:x}".format(num1))


##num2 = 98
##print("{0} {1:c}".format(num2, num2))


##float1 = 1234.567
##print(float1)
##print("기본 출력 {0:f}".format(float1))
##print("지수표기법 {0:e}".format(float1))
##print("소수 둘째자리까지 {0:.2f}".format(float1))


##txt1 = "Hello"
##txt2 = "world!"
##print("기본 출력\n{0:s}".format(txt1, txt2))
##print("7칸 출력\n{0:7s}?".format(txt1, txt2))


##num1 = 17
##print(f'10진수 17 = {num1}')
##print(f'10진수 17의 8진수 = {num1:o}')
##print(f'10진수 17의 16진수 = {num1:x}')


##num2 = 100
##print(f"{num2} {num2:c}")


##float1 = 1234.567
##print(f"기본 출력 {float1:f}")
##print(f"지수표기법 {float1:e}")
##print(f"소수 둘째자리까지 {float1:.2f}")


##txt1 = "Hello"
##txt2 = "World!"
##print(f'기본 출력\n{txt1:s} {txt2:s}')
##print(f'7칸 출력\n{txt1:7s} {txt2:7s}?')


##r = 5
##pi = 3.14
##print('넓이는 %d * %d * %.2f = %.1f' % (r, r, pi, r*r*pi))


##r = 5
##pi = 3.14
##print("넓이는 {0} * {1} * {2:.2f} = {3:.1f}"
##      .format(r, r, pi, r * r * pi))


##r = 5
##pi = 3.14
##print(f'넓이는 {r:d} * {r:d} * {pi:.2f} = {r * r * pi:.1f}')


##golden_ratio = 1.61804
##print(f'소수 첫째 자리까지 출력 : {golden_ratio:.1f}')
##print(f'소수 둘째 자리까지 출력 : {golden_ratio:.2f}')
##print(f'소수 셋째 자리까지 출력 : {golden_ratio:.3f}')
##print(f'소수 넷째 자리까지 출력 : {golden_ratio:.4f}')


##passwd = input("비밀번호 : ")
##print(input("id : "), "입력")


##egg = input("계란은 몇 개?")
##print(egg, type(egg))
##
##egg = int(egg)
##print(egg, type(egg))


##attack = input("공격력은?")
##scale = input("배율은?")
##
##print("데미지는 ", attack * scale)


##attack = int(input("공격력은? "))
##scale = int(input("배율은? "))
##
##print("데미지는", attack * scale)


##minute = input("분을 입력하세요 : ")
##minute = int(minute)
##second = 60 * minute
##
##text = str(minute) + "분=" + str(second) + "초"
##print(text)


##print("환영합니다 ", input("닉네임을 입력하세요 : "), "님!",
##      sep = "")


##float1 = float(input("실수를 입력하세요 : ")) * 10 
##print("%.3f" % (float1))


##num1 = int(input("첫번째 숫자를 입력하세요 : "))
##num2 = int(input("두번째 숫자를 입력하세요 : "))
##num3 = int(input("세번째 숫자를 입력하세요 : "))
##print("총합은 %d" % (num1 + num2 + num3))


##r = int(input("반지름을 입력하세요 : "));
##pi = 3.14
##print("원의 넓이는 %.1f" % (r * r * pi))
##print("원의 둘레길이는 %.1f" % (r * 2 * pi))


##a = int(input("윗변을 입력하세요 : "))
##b = int(input("밑변을 입력하세요 : "))
##c = int(input("높이를 입력하세요 : "))
##
##print("사다리꼴의 넓이는 %.1f" % ((a + b) * c / 2))


nut1 = '밤양갱'
nut2 = "달디단 밤양갱"
nut3 = """달디달고 달디달고, 달디단 밤양갱 밤양갱 내가 먹고 싶었던 건, 달디단, 밤양갱, 밤양갱이야"""
