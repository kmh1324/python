##num = []
##for i in range(1, 101):
##    num.append(i)
##    
##num.remove(1)
##for i in range(2, int(100 ** 0.5) + 1):
##    for j in range(2, 101):
##        if j != i and j % i == 0 and j in num:
##            num.remove(j)
##print(num)


##str_list = []
##while True:
##    menu = int(input("1. 추가 2. 삭제 3. 확인 4. 선택추가 5. 종료 : "))
##
##    if menu == 1:
##        text = input("추가할 문자열을 입력해주세요 : ")
##        str_list.append(text)
##        print(str_list)
##
##    elif menu == 2:
##        del str_list[-1]
##        print(str_list)
##
##    elif menu == 3:
##        print(str_list)
##
##    elif menu == 4:
##        text = input("추가할 문자열을 입력해주세요 : ")
##        text_location = int(input("추가할 위치를 입력해주세요 : "))
##        str_list.insert(text_location, text)
##        print(str_list)
##        
##    elif menu == 5:
##        break


##empty_tuple = ()
##print(empty_tuple)
##
##single_tuple = (10,)
##print(single_tuple)
##
##multi_tuple = (10, 20, 30)
##print(multi_tuple)


##n_tuple = (10, 20, 30, 40, 50)
##
##n_tuple[0] = 100
##
##del n_tuple[0]


##t = tuple(range(5))
##print(t)
##t2 = tuple(range(9, 20))
##print(t2)
##t3 = tuple(range(-10, 5, 2))
##print(t3)
##
##t = 10, 20, 30, 40
##print(t, type(t))
##t2 = 10, '이십', 30, 40
##print(t2, type(t2))


##single_tuple = (3,)

##multi_tuple = tuple(range(0, 9, 2))
##print(multi_tuple)


##lunch = ('샐러드', '햄버거', '돈까스', '뷔페')
##dinner = ('만두', '국밥', '초밥', '마라탕')
##
##menu = lunch + dinner
##dinner = dinner[3:] + ('삼겹살',) + dinner[:1]
##
##print(menu)
##print(dinner)


##snack = ('감자칩', '새우깡', '초콜렛')
##print(snack, type(snack), sep = "\n")
##
##list_snack = list(snack)
##print(list_snack, type(list_snack), sep = "\n")


##fruits = ('사과', '귤', '파인에플', '메론')
##reverse_fruits = fruits[::-1]
##print(reverse_fruits)
##
##snack = ('감자칩', '새우깡', '초콜렛')
##print(snack)
##
##potato, shirmp, chocolate = snack
##print(potato)
##print(shirmp)
##print(chocolate)


##t1 = (10, 20, 30, 40, 50)
##t2 = (1, 2, 3, 4, 5)
##
##t3 = t1 + t2
##
##t4 = t1 * 2
##
##print(t3)
##print(t4)


##ice2 = ('메로나', '메로나', '엔초', '민크초코', '호두마루')
##print(ice2)
##
##tmp = ice2.count('메로나')
##
##print('메로나가 {0}개 있습니다.'.format(tmp))


##ice = ('죠스바', '메로나', '돼지바', '호두마루')
##
##txt = '메로나가'
##txt += f"{ice.index('메로나') + 1}번째에 있습니다."
##print(txt)
##
##print('ice에 총', len(ice), '개 있습니다.')


##num_tuple = (11, 22, 31, 44, 23, 59)
##print(f"31은 {num_tuple.index(31)}번째에 있습니다.")


##ice2 = ('메로나', '메로나', '엔초', '민크초코', '호두마루')
##ice2 = list(ice2)
##
##for i in ice2[::2]:
##    print(i)


##multi_tuple = ('a', 'b', 'c')
##print(multi_tuple)
##multi_tuple = ('a', 'B', 'c')
##print(multi_tuple)


##empty = set()
##
##s = {1, 2, 3, 5, 7, 11, 13, 17, 19}
##print(s)
##
##s = set([3, 4, 5, 2, 1, 2, 2, 3, 6, 4, 5])
##print(s)


##s = {6, 3, 7, 2, 9}
##print(s)
##s.add(8)
##s.add(6)
##print(s)
##s.remove(7)
##print(s)


##test = {1, 2, 3, 4, 5}
##print(test)


##import random
##
##set_dice = set()
##for i in range(20):
##    dice_num = random.randint(1, 20)
##    set_dice.add(dice_num)
##print(set_dice)


##set2, set3, set5 = set(), set(), set()
##for i in range(1, 31):
##    if i % 2 == 0:
##        set2.add(i)
##        
##    if i % 3 == 0:
##        set3.add(i)
##
##    if i % 5 == 0:
##        set5.add(i)
##print(set2, set3, set5, sep = "\n")


##set1 = {9, 4, 6, 2, 1}
##print(set1)
##if 6 in set1:
##    print("set1안에 6이 있습니다.")
##if 10 in set1:
##    print("set1안에 10이 있습니다.")
##
##for el in set1:
##    if el % 2 == 0:
##        print(el)


##set1 = {9, 4, 6, 2, 1}
##set2 = {8, 4, 7, 3, 2}
##
##set3 = set1.union(set2)
##print(set3)
##
##set4 = set1.intersection(set2)
##print(set4)


##set1 = {9, 4, 6, 2, 1}
##set2 = {8, 4, 7, 3, 2}
##
##set5 = set1.difference(set2)
##print(set5)
##
##set6 = set2.difference(set1)
##print(set6)


##set1 = {'가', '나', '다', '라'}
##set2 = {'가', '나', '다'}
##
##if set2.issubset(set1):
##    print("set1안에 set2를 포함!")
##if set1.issuperset(set2):
##    print("set2는 set1에 포함!")
    

##set1 = {1, 3, 2, 5, 7}
##set2 = {3, 8, 4, 5}
##
##print("집합1의 구성", set1)
##print("집합2의 구성", set2)
##print()
##
##print("합집합", set1.union(set2))
##print("교집합", set1.intersection(set2))
##print("집합1 - 집합2 차집합", set1.difference(set2))
##print("집합2 - 집합1 차집합", set2.difference(set1))


set1 = {1, 3, 2, 5, 7}
set2 = {3, 8, 4, 5}

print("집합1의 구성", set1)
print("집합2의 구성", set2)
print()

if not set1.issubset(set2):
    print("집합 1은 집합 2에 포함되지 않음")
if not set1.issuperset(set2):
    print("집합 2는 집합 1에 포함되지 않음")
list_set1 = list(et1.difference(set2))
print("대칭차집합", )
