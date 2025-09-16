##text = input("영어로 문자열을 입력해주세요: ")
##result = ""
##
##for i in text:
##    count = 0   
##    if i not in result:
##        for j in range(len(text)):
##            if i in text[j]:
##                count += 1
##
##        print(f"{i}: {count}")               
##        result += i


##count = 5
##while count > 0:
##    print(count)
##    count -= 1


##for count in range(5, 0, -1):
##    print(count)


##i = 2
##while i <= 10:
##    print(i)
##    i += 2


##for i in range(2, 11, 2):
##    print(i)


##text = "Hello"
##i = len(text) - 1
##while i >= 0:
##    print(text[i], end = '')
##    i -= 1

##text = "Hello"
##for char in reversed(text):
##    print(char, end = '')


##n = 1
##while n <= 100:
##    print(n, end = ' ')
##    n *= 2
##print()
##
##for i in range(7):
##    print(2**i, end = ' ')


##print("for 버전 소수 구하기: ")
##for num in range(2, 20):
##    is_prime = True
##    for i in range(2, int(num ** 0.5) + 1):
##        if num % i == 0:
##            is_prime = False
##            break
##    if is_prime:
##        print(num, end = ' ')


##print("for 버전 소수 구하기: ")
##num = 2
##while num < 20:
##    is_prime = True
##    
##    i = 2
##    while i < int(num ** 0.5) + 1:
##        if num % i == 0:
##            is_prime = False
##            break
##        i += 1
##        
##    if is_prime:
##        print(num, end = ' ')
##    num += 1


##num_list = [10, 20, 30, 40, 50]
##print("num_list : ",num_list)
##print("num_list의 길이 : ", len(num_list))
##
##test_list = ["하나", 2, 3.0]
##print(test_list[0], type(test_list[0]))
##print(test_list[1], type(test_list[1]))
##print(test_list[2], type(test_list[2]))


##sample = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
##
##print(sample[1])
##print(sample[-1])
##print(sample)
##print(sample[0:len(sample)])
##print(sample[::-1])
##
##txt = list("테스트 중")
##print(txt)
##
##txt[4] = "끝"
##print(txt)


##sample = []
##sample1 = list()
##
##sample2 = list('예시문장입니다.')
##
##print(sample)
##print(sample2[2:4])
##print(sample2[1:5:2])


##phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['#', 0, '*']]
##
##print(phone)
##print(phone[0])
##print(phone[1])
##print(phone[2])
##print(phone[3])
##print(phone[0][0])
##print(phone[1][1])
##print(phone[2][0])
##print(phone[3][1])


##test = [1, 2, 3]
##print(test[2])
##
##test.append(4)
##print(test)
##
##del test[1]
##print(test)


##animals = ['고양이', '너구리', '강아지', '사자']
##search = input("동물 이름을 입력하세요 : ")
##
##if search in animals:
##    print("해당 동물이 리스트에 있습니다.")
##else :
##    print("해당 동물이 리스트에 없습니다.")


##test = [1, 2, 3]
##
####test[3] = 4
##test.insert(0, 5)
##
##test.remove(2)
##print(test)
##
##temp = test.pop(2)
##print(temp, test)


##list = []
##for i in range(3, 8):
##    list.append(i)
##print(f"리스트 안에 {list}이 있습니다.")


##list = []
##for i in range(3):
##    in_text = input("데이터를 입력해주세요 : ")
##    list.append(in_text)
##print(list)


##alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
##print(alphabet)
##
##char_6 = alphabet.pop(6)
##print(char_6)
##print(alphabet)


##text = list(input("문자열을 입력해주세요 : "))
##
##for i in range(len(text) - 1, -1, -1):
##    print(text[i], end = '')


##num = []
##for i in range(1, 101):
##    num.append(i)
##print(num)


##alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
##
##index_ch = alphabet.index("B")
##print(index_ch, alphabet[index_ch])
##
##ch = input("알파벳을 입력하세요: ")
##index_ch = alphabet.index(ch)
##print(ch, "는 ", index_ch + 1, "번째 알파벳", sep = "")


##num = []
##for i in range(1, 101):
##    num.append(i)
##
##num.remove(1)
##for i in range(1, 101):
##    if not i == 2 and i % 2 == 0:  
##        num.remove(i)
##print(num)


##num = []
##for i in range(1, 101):
##    num.append(i)
##
##num.remove(1)
##for i in range(1, 101):
##    if (not i == 2 and not i == 3) and i % 2 == 0 or i % 3 == 0:  
##        num.remove(i)
##      
##print(num)


##num = []
##for i in range(1, 101):
##    num.append(i)
##
##num.remove(1)
##for i in range(1, 101):
##    if (not i == 2 and not i == 3 and not i == 5 and i % 2 == 0 or i % 3 == 0 or i % 5 == 0:  
##        num.remove(i)
##      
##print(num)


##num = []
##for i in range(1, 101):
##    num.append(i)
##
##num.remove(1)
##for i in range(1, 101):
##    if (not i == 2 and not i == 3 and not i == 5 and not i == 7) and i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:  
##        num.remove(i)
##      
##print(num)


num = []
for i in range(1, 101):
    num.append(i)

num.remove(1)
for i in range(1, 101):
    if not i == 2 and not i == 3 and not i == 5 and not i == 7 and i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:  
        num.remove(i)
      
print(num)
