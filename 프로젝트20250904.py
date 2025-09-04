##for num in range(1,100):
##    if num > 55:
##        break
##    print(num, end = " ")


##for num in range(7):
##    power = 2 ** num
##    if power > 64:
##        break
##    print(power, end = " ")


##sum_odd = 0
##for i in range(1, 1000, 2):
##    if i % 13 == 0:
##        continue
##    print(i, end = " ")
##    sum_odd += i
##    if sum_odd > 500:
##        break


##odd = 1
##for num in range(1, 20):
##    if num % 2 == 0:
##        continue
##    odd *= num
##    print(f"{num} = {odd}")


##num = int(input("숫자를 입력해주세요 : "))
##
##for i in range(2, 20):
##    
##    if num ** i >= 10000:
##        break
##    print(num ** i, end = " ")
    
    
##num = int(input("숫자를 입력해주세요 : "))
##
##print(f"{num}의 약수: ", end = "")
##for i in range(1, num + 1):
##    if num % i == 0:
##        print(i, end = " ")


##turn = 3
##
##for num in range(1, 101):
##    
##    if num % 3 == 0 and turn == 3 and num % 15 != 0:
##        print(num, end = " ")
##        turn = 5
##
##    elif num % 5 == 0 and turn == 5 and num % 15 != 0:
##        print(num, end = " ")
##        turn = 3


##count = 0
##for num in range(1, 100 + 1):
##    if num % 3 == 0 and '7' in str(num):
##        print(num, end = " ")
##        count += 1
##
##    if count >= 5:
##        break


##for num in range(97, 104):
##    print(chr(num))
##
##text = "ABCDEFG"
##for character in text:
##    print(ord(character))


##text = "HelloPython"
##
##for character in text:
##    if character.isupper():
##        print(character.lower(), end = "")
##    
##    elif character.islower():
##        print(character.upper(), end = "")


##text = "Hello World! How are you doing today?"
##vowels = "aeiouAEIOU"
##count = 0
##
##for char in text:
##    if char in vowels:
##        count += 1
##
##    print(f"모음의 개수: {count}")


##text = "abcdefghijklmnopqrstuvwxyz"
##shift = 3
##
##shifted_text = ""
##
##for character in text:
##    if character.isalpha():
##        shifted_char = chr((ord(character) + shift))
##        shifted_text += shifted_char
##
##print(shifted_text)


##num = int(input("숫자를 입력하세요: "))
##
##sum = 0
##for i in range(1, num + 1):
##    sum += i
##print(sum)


##text = input("문장을 입력하세요: ")
##
##count = 0
##for i in text:
##    if '0' <= i <= '9':
##        count += 1
##print(f"숫자의 개수: {count}")


for i in range(97, 122 + 1):
    print(f"{i}({chr(i)})", end = " ")
