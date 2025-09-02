##print("# 연습문제")
##print("\\\\\\\\")
##print("-" * 8)


##print("안녕하세요"[1:3])
##print("안녕하세요"[2:4])
##print("안녕하세요"[1:])
##print("안녕하세요"[:3])


##import random
##
##count = 0
##while count < 5:
##    print(random.randint(10,101))
##    count += 1


##import random
##
##count = 0
##while count < 5:
##    print(random.randrange(10, 101, 10))
##    count += 1


##import random
##
##count = 0
##while count < 20:
##    print(f"{random.randint(3,12)} ", end = "")
##    count += 1


##import random
##
##count = 0
##while count < 7:
##    print(random.randrange(2, 100, 5))
##    count += 1


##import random
##
##correct = random.randint(1, 100)
##
##while True:
##    answer = int(input("1~100 사이 숫자를 입력해 주세요  : "))
##
##    if answer > correct:
##        print("더 낮은 숫자가 정답입니다.")
##
##    elif answer < correct:
##        print("더 높은 숫자가 정답입니다.")
##
##    else:
##        print("정답입니다.")
##        break;


##import random
##
##correct = random.randint(1, 1000)
##
##count = 0
##while True:
##    answer = int(input("1~100 사이 숫자를 입력해 주세요  : "))
##
##    if answer > correct:
##        print("더 낮은 숫자가 정답입니다.")
##        count += 1
##
##    elif answer < correct:
##        print("더 높은 숫자가 정답입니다.")
##        count += 1
##
##    else:
##        print("정답입니다.")
##        count += 1
##        break;
##print("현재 입력 횟수", count)


##import random
##
##digit100 = random.randint(0, 9)
##
##while True:
##    temp = random.randint(0, 9)
##
##    if temp != digit100:
##        digit10 = temp
##        break
##
##while True:
##    temp = random.randint(0, 9)
##
##    if temp != digit100 and digit10 != temp:
##        digit1 = temp
##        break
##
##print(digit100 * 100 + digit10 * 10 + digit1)


##import random
##
##digit100 = random.randint(0, 9)
##
##while True:
##    temp = random.randint(0, 9)
##
##    if temp != digit100:
##        digit10 = temp
##        break
##
##while True:
##    temp = random.randint(0, 9)
##
##    if temp != digit100 and digit10 != temp:
##        digit1 = temp
##        break
##
##total = digit100 * 100 + digit10 * 10 + digit1
##
##answer = int(input("세자리 숫자를 입력해주세요 : "))
##
##a100 = answer // 100
##answer %= 100
##a10 = answer // 10
##answer %= 10
##a1 = answer
##
##strike = 0
##ball = 0
##
##if a100 == digit100:
##    strike += 1
##elif a100 == digit10:
##    ball += 1
##elif a100 == digit1:
##    ball += 1
##    
##if a10 == digit100:
##    strike += 1
##elif a10 == digit10:
##    ball += 1
##elif a10 == digit1:
##    ball += 1
##    
##if a1 == digit100:
##    strike += 1
##elif a1 == digit10:
##    ball += 1
##elif a1 == digit1:
##    ball += 1
##print(f"{strike} strike, {ball} ball")


##for num in range(5) :
##    print(num, end = " ")


##for num in range(1, 20) :
##    print(num, end = " ")


##for num in range(1, 18, 3):
##    print(num, end = " ")


##for i in range(10):
##    print('안녕', i, '번째')
##
##for i in range(1, 10):
##    print('안녕', i, '번째')
##
##for i in range(1, 11):
##    print('안녕', i, '번째')


##for i in range(2, 101, 2):
##    print(i, end = " ")


##for i in range(1, 100, 2):
##    print(i, end = " ")


##for i in range(10, 0, -1):
##    print(i, end = " ")


##total = 0
##for i in range(1, 101):
##    total += i
##
##print(total)


##for i in range(5, 101, 5):
##    print(i, end = " ")

##total = 0
##for i in range(3, 100, 3):
##    total += i
##
##print(total)


##for i in range(1, 11):
##    if i % 2 == 0:
##        print('짝수번 안녕')
##    elif i % 2 == 1:
##        print('홀수번 안녕')
    

##first_num = int(input('시작값 입력:'))
##last_num = int(input('끝값 입력:'))
##
##for i in range(first_num, last_num + 1):
##    if i % 2 == 0:
##        print('짝수 :', i)
##    elif i % 2 == 1:
##        print('홀수 :', i)


##print('시작값 입력: ')
##first_num = int(input())
##
##print('끝값 입력: ')
##last_num = int(input())
##
##for i in range(first_num, last_num + 1):
##    if i % 2 == 0:
##        print('짝수 :', i)
##    elif i % 2 == 1:
##        print('홀수 :', i)


first = int(input("시작값 입력 : "))
last = int(input("끝값 입력 : "))

for i in range(first, last + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end = " ")
