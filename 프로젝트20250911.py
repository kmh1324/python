##for dan in range(2, 10):
##    print('===={0}단===='.format(dan))
##    for su in range(1, 10):
##        print('{0} * {1} = {2}'.format(dan, su, dan * su))


##for su in range(1, 10):
##    for dan in range(2, 10):
##        print(f'{dan:d}*{su:d} = {dan * su:-2d}', end = "  ")
##    print()


##for su in range(1, 10):
##    for dan in range(2, 10):
##        if dan % 2 == 0:
##            continue
##        print(f'{dan:2d}*{su:2d} = {dan * su:-3d}', end = "  ")
##    print()


##for dan in range(2, 10, 3):
##    for su in range(1, 10):
##        for dan_2 in range(dan, dan + 3):
##            print(f'{dan_2:2d} * {su:2d} = {dan_2 * su:-3d}', end = "  ")
##        print()
##    print()


##dan1 = int(input("몇단부터? : "))
##dan2 = int(input("몇단까지? : "))
##
##for dan in range(dan1, dan2 + 1):
##    for su in range(1, 10):
##        print(f"{dan}*{su}={dan*su}")
##    print()


##num = int(input("몇개씩? : "))
##dan1 = int(input("몇단까지? : "))
##
##for dan in range(2, dan1, num):
##    for su in range(1, 10):
##        for dan_2 in range(dan, dan + num):
##            if dan_2 > dan1:
##                break
##            print(f'{dan_2:d} * {su:d} = {dan_2 * su:2d}', end = "  ")
##        print()
##    print()


##for i in range(1, 6):
##    print("*", end = "")


##for i in range(1, 6):
##    for j in range(1, 6):
##        print("*", end = "")
##    print()


##for i in range(1, 6):
##    for j in range(1, i + 1):
##        print("*", end = '')
##    print()


##for i in range(1, 6):
##    for j in range(i, 6):
##        print("*", end = '')
##    print()


##for out in range(1, 6):
##    for blank in range (out, 6):
##        print(" ", end = '')
##    for star in range(1, out + 1):
##        print("*", end = '')
##    print()


##for out in range(1, 6):
##    for blank in range(1, out + 1):
##        print(" ", end = '')
##    for star in range(out, 6):
##        print("*", end = '')
##    print()


##for i in range(5):
##    for blank in range(5 - i):
##        print(" ", end = '')
##    for star in range(i * 2 + 1):
##        print("*", end = "")
##    print()


##for i in range(5):
##    for blank in range(5 - i):
##        print(" ", end = '')
##    for star in range(i * 2 + 1):
##        print("*", end = "")
##    print()
##    
##for j in range(3, -1, -1):
##    for blank in range(5 - j):
##        print(" ", end = '')
##    for star in range(j * 2 + 1):
##        print("*", end = "")
##    print()


##s = "PYTHON"
##for y in range(len(s)):
##    for x1 in range(len(s) - y - 1):
##        print(" ", end = "")
##    for x2 in range(2 * y + 1):
##        print(s[x2 % len(s)], end = "")
##    print()


##s = "시간을달려서"
##n = len(s)
##for y in range(n):
##    for x in range(n):
##        if y <= x and y <= n - 1 - x or y >= x and y >= n - 1 - x:
##            print(s[x], end = "")
##        else :
##            print("  ", end = "")
##    print()


##s = "테두리를 만들자"
##n = 7
##for y in range(n):
##    for x in range(n):
##        if y == 0 or y == n -1 or x == 0 or x == n - 1:
##            print(s[(x + y) % len(s)], end = "")
##        else :
##            print("  ", end = "")
##    print()


##s = "빙글빙글돌아가는파이썬"
##n = 15
##for y in range(n):
##    for x in range(n):
##        min_desk = min(y, x, n-1-y, n-1-x)
##        print(s[min_desk & len(s)], end = "")
##    print()


##s = "문자열로V자그리기"
##rows = 5
##
##for y in range(rows):
##    for x in range(len(s)):
##        if y == 0 or y == rows - 1:
##            if x % (2 * rows - 2) ==  y:
##                print(s[x], end = "")
##            else:
##                print(" ", end = "")
##        elif x % (2 * rows - 2) == y or x % (2 * rows - 2 - y):
##            print(s[x], end = "")
##        else :
##            print(" ", end = "")
##    print()


##s1 = "파이썬은즐거워"
##s2 = "파이썬은 재밌어"
##common = ""
##for letter1 in s1:
##    for letter2 in s2:
##        if letter1 == letter2 and letter1 not in common:
##            common += letter1
##print(f"공통 문자: {common}")


##s = "AABBCCCC"
##compressed = ""
##i = 0
##while i < len(s):
##    count = 1
##    for j in range(i + 1, len(s)):
##        if s[j] == s[i]:
##            count += 1
##        else :
##            break
##    if count > 1:
##        compressed += str(count) + s[i]
##    else :
##        compressed += s[i]
##    i += count
##print(f"압축된 문자열: {compressed}")


s = "ABABABABA"
pattern = "ABA"
for i in range(len(s) - len(pattern) + 1):
    match = True
    for j in range(len(pattern)):
        if s [i + j] != pattern[j]:
            match = False
            break
    if match:
        print(f"패턴 발견 위치: {i}")
