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


##for i in range(97, 122 + 1):
##    print(f"{i}({chr(i)})", end = " ")


##input_text = input("문장을 입력하세요: ")
##vowels = "aeiouAEIOU"
##output_text = ""
##
##count = 0
##for ch in input_text:
##    if ch in vowels:
##        output_text += '*'
##        count += 1
##    else :
##        output_text += ch
##    
##print(f"변환된 문장: {output_text}")
##print(f"바뀐 모음의 개수: {count}")


##import random
##
##password = ""
##for i in range(0, 6):
##    tmp = random.randint(0, 1)
##    if tmp == 1:
##        password += chr(random.randint(48, 57))
##    else :
##        password += chr(random.randint(65, 80))
##        
##print(f"추천 비밀번호 : {password}")


##cnt = 0
##
##for y in range(1, 6):
##    for x in range(1, 6):
##        cnt += 1
##    print(cnt)


##for hour in range(1, 13):
##    for minute in range(1, 61):
##        print(f'{hour}시 {minute}분')
     

##for day in range(1, 8):
##    print(f'{day}일차')
##    for time in range(1, 4):
##        if time == 1:
##            print('아침', end = ' ')
##        if time == 2:
##            print('낮', end = ' ')
##        if time == 3:
##            print('밤')


##for y in range(5):
##    sentence = ''
##    for x in range(5):
##        sentence += str(y)
##    print(sentence)


##for y in range(1, 5):
##    pyramid = ''
##    for x in range(y):
##        pyramid += str(y)
##    print(pyramid)


##i = 1
##txt = ''
##while i < 4:
##    j = 1
##    txt += f'{i}학년 '
##    while j < 6:
##        txt += f'{j}반 '
##        j += 1
##    i += 1
##    txt += '\n'
##
##print(txt)


##num = 10
##cnt = 0
##for y in range(1, num + 1):
##    for x in range(1, num + 1):
##        cnt += 1
##        print(cnt, end = ' ')
##    print()


##num = int(input("숫자를 입력해주세요 : "))
##cnt = 0
##for y in range(1, num + 1):
##    for x in range(1, y):
##        cnt += 1
##        print(cnt, end = ' ')
##    print()


##for y in range(5):
##    for x in range(5):
##        print(chr(ord('A') + x + y), end = ' ')
##    print()


##string = "abcd"
##
##for y in range(len(string)):
##    for x in range(y, len(string)):
##        print(string[y:x+1])


##num = 0
##for i in range(6):
##    for j in range(5):
##        num += 10
##        print(num, end = " ")
##    print()    


##for i in range(5):
##    for j in range(i + 1):
##        print(chr(ord('A') + i), end = " ")
##    print()


##for i in range(5):
##    for j in range(i + 1):
##        print(chr(ord('A') + i + j), end = " ")
##    print()


##for i in range(1, 10):
##    print(2, '*', i, '=', 2 * i)
##
##for i in range(1, 10):
##    print('2* %d = %d' % (1, 2 * i))
##
##for i in range(1, 10):
##    print('{0}*{1} = {2}'.format(2, i, 2 * i))


##for i in range(1, 10):
##    print('{0}*{1}={2}'.format(2, i, 2 * i))
##for i in range(1, 10):
##    print('{0} * {1} = {2}'.format(3, i, 3 * i))
##for i in range(1, 10):
##    print('{0} * {1} = {2}'.format(4, i, 4 * i))
##for i in range(1, 10):
##    print('{0} * {1} = {2}'.format(5, i, 5 * i))


##dan = 2
##for i in range(1, 10):
##    print('{0} * {1} = {2}'.format(dan, i, dan * i))
##dan += 1
##for i in range(1, 10):
##    print('{0} * {1} = {2}'.format(dan, i, dan * i))
##dan += 1
##for i in range(1, 10):
##    print('{0} * {1} = {2}'.format(dan, i, dan * i))
##dan += 1
##for i in range(1, 10):
##    print('{0} * {1} = {2}'.format(dan, i, dan * i))


for dan in range(2, 10):
    for i in range(1, 10):
        print('{0} * {1} = {2}', format(dan, i, dan * i))

for dan in range(2, 10):
    print('===={0}')
