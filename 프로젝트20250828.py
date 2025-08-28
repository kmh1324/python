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


##first = int(input("첫번째 숫자를 입력해 주세요 : "))
##second = int(input("두번째 숫자를 입력해 주세요 : "))
##three = int(input("세번째 숫자를 입력해 주세요 : "))
##
##if first > second:
##    temp = first
##    first = second
##    second = temp
##
##if second > three:
##    temp = second
##    second = three
##    three = temp
##
##if first > second:
##    temp = first
##    first = second
##    second = temp
##
##print(first, second, three)


##first = int(input("첫번째 숫자를 입력해 주세요 : "))
##second = int(input("두번째 숫자를 입력해 주세요 : "))
##three = int(input("세번째 숫자를 입력해 주세요 : "))
##
##if first > second:
##    temp = first
##    first = second
##    second = temp
##
##if second > three:
##    temp = second
##    second = three
##    three = temp
##
##if first > second:
##    temp = first
##    first = second
##    second = temp
##
##a, b, c = first, second, three
##if (a + 1 == b and b + 1 == c) or (a - 1 == b and b - 1 == c):
##    print("스트레이트!")
##else:
##    print("X")


##while True:
##    print("무한 반복중...")


##count = 0
##while count < 3:
##    print("{0}회 반복 중...".format(count))
##    count += 1


##count = 0
##
##while count < 100:
##    if count % 3 == 0:
##        print("3의 배수 : {0}".format(count))
##    count += 1


##while False:
##    print("False라면 출력이 되지 않습니다...")


##count = 3
##
##while count > 0:
##    print("{0}...".format(count))
##    count -= 1


##number = 20
##
##while number <= 1000000:
##    print(f"{number}")
##    number *= 10


##i = 0
##while i < 5:
##    print("파이썬")
##    i += 1


##i = 1
##sum = 0
##while i <= 10:
##    sum += i
##    i += 1
##
##print(sum)


##i = 0
##while i <= 200:
##    i += 1
##    if i % 5 == 0:
##        print(f"{i} ", end = "")


##i = 0
##while i <= 200:
##    i += 1
##    if i % 5 == 0:
##        print(f"{i} ", end = "")
##
##    if i % 25 == 0:
##        print("\n", end = "")


##count = 0
##
##while True:
##    print("{}번째 반복중...".format(count))
##    count += 1
##    if count >= 5:
##        break


##count = 0
##while count < 13:
##    count += 1
##    if count % 2 == 0 and count % 3 == 0:
##        continue
##    print(f'{count}는 6의 배수가 아닙니다.')


##total = 0
##while True:
##    number = int(input("양수를 입력해주세요 : "))
##    if number == 0:
##        break
##    elif number < 0:
##        print("음수를 입력하셨습니다.")
##        continue
##    total = total + number
##    print('현재까지의 양수의 합은 {0}입니다.'.format(total))


##word = "Hellowhile"
##count = 0
##
##while count < len(word):
##    if count % 2 == 1:
##        count += 1
##        continue
##    print(word[count], end = "")
##    count += 1


##result = ""
##while True:
##    word = input("단어를 입력하세요 ('end'를 입력하면 종료): ")
##    if word == "end":
##        break
##    if len(word) < 3:
##        continue
##    result += word + " "
##print(f"입력된 단어들: {result}")


##while True:
##    sentence = input("열글자 이상의 문장을 입력하세요 ('quit'이 포함되면 종료): ")
##    if "quit" in sentence:
##        break
##    if len(sentence) < 10:
##        print("10글자 미만입니다.")
##        continue
##    print(sentence[::-1])


##number = 1
##multi = number
##
##while True:
##    multi *= number
##
##    if multi >= 5000:
##        break
##    number += 1
##    
##print(f"number : {number}")
##print(f"multi : {multi}")


##i = 1
##while i <= 49:
##    if i % 3 == 0:
##        i += 1
##        continue
##
##    if i % 5 == 0:
##        i += 1
##        continue
##        
##    print(f"{i} ", end = "")
##    i += 1


##num1 = int(input("숫자1 : "))
##num2 = int(input("숫자2 : "))
##
##while True:
##    num1 += 1
##    if num1 >= num2:
##        break
##    
##    print(f"{(num1) * (num1)}   ", end = "")
    

text = input("문장을 입력해주세요 : ")

print("바뀐 문장 : ", end = "")
count = 0
while count < len(text):
    if count % 2 == 0:
        print(text[count], end = "")
        count += 1
    else:
        print("■", end = "")
        count += 1























