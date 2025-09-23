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


##set1 = {1, 3, 2, 5, 7}
##set2 = {3, 8, 4, 5}
##
##print("집합1의 구성", set1)
##print("집합2의 구성", set2)
##print()
##
##if not set1.issubset(set2):
##    print("집합 1은 집합 2에 포함되지 않음")
##if not set1.issuperset(set2):
##    print("집합 2는 집합 1에 포함되지 않음")
##
##diff1 = set1.difference(set2)
##diff2 = set2.difference(set1)
##
##set3 = diff1.union(diff2)
##print("대칭차집합", set3)


##text = input("문자열을 입력해주세요 : ")
##letters = set()
##
##for i in text:
##    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
##        letters.add(i)
##print(letters)


##list1 = [1, 2, 3, 4, 8, 16]
##list2 = [1, 2, 3, 4, 5]
##print("리스트1의 구성", list1)
##print("리스트2의 구성", list2)
##
##set1 = set(list1)
##set2 = set(list2)
##set3 = set1.union(set2)
##list3 = list(set3)
##
##print("리스트 3", list3)


##import random
##
##set5 = set()
##
##r_set5 = set()
##
##count = 0
##while True:
##    num = int(input("1~30사이의 숫자를 입력해주세요 : "))
##    if num >= 1 and num <= 30 and num not in set5:
##        set5.add(num)
##        count += 1
##        
##    else :
##        print("다시 입력해주세요.")
##
##    if count == 5:
##        break
##
##count = 0
##while True:
##    r_num = random.randint(1, 30)
##    if r_num >= 1 and r_num <= 30 and r_num not in r_set5:
##        r_set5.add(r_num)
##        count += 1
##        
##    if count == 5:
##        break
##
##print(set5)
##print(r_set5)
##
##intersection_set = set5.intersection(r_set5)
##print(intersection_set)
##print(len(intersection_set))


##dic = {'newjeans':'hypeboy', 'c언어':'기본언어'}
##dic['이샘'] = '전문학원'
##dic['코딩'] = '뿌듯해'
##
##print('딕셔너리 키값들 출력 :', dic.keys())
##print('딕셔너리 벨류값 출력 :', dic.values())
##print('딕셔너리 키, 벨류 동시 출력 :', dic.items())
##print('=' * 60)
##
##print('기본출력 :', dic['c언어'], dic['이샘'], dic['코딩'])


##print('keys', '=' * 60)
##for key in dic.keys():
##    print(key)
##
##print('values', '=' * 60)
##for value in dic.values():
##    print(value)
##
##print('items', '=' * 60)
##for key, value in dic.items():
##    print(key, value)


##hypeboy = '이샘'
##if hypeboy in dic.keys():
##    print('키값이 존재합니다')
##
##newjeans = '뉴진스'
##if newjeans in dic.keys():
##    print(newjeans, '가 존재합니다')
##else :
##    print(newjeans, '가 키값으로 존재하지 않습니다.')
##    print('{0}가 존재하지 않습니다.'.format(newjeans))
##    print(f'{newjeans}가 존재하지 않습니다.')
##
##coding = '전문학원'
##if coding in dic.values():
##    print(coding, '이 value값으로 존재합니다')
##else :
##    print(coding, '이 value값으로 존재하지 않습니다')


##score = {"국어": 80, "수학": 92, "영어": 87}
##
##print("국어 :", score["국어"])
##print("수학 :", score["수학"])
##print("영어 :", score["영어"])
##print(f"총점 : {score["국어"] + score["수학"] + score["영어"]}", end = "    ")
##print(f"평균 : {(score["국어"] + score["수학"] + score["영어"]) / 3:.2f}")


##game_character = {"name": "AAA", "lv": 10, "hp": 50, "equip": ["sword", "shield", "potion", "map"]}
##print(game_character)
##
##del game_character["lv"]
##print(game_character)
##
##del game_character["equip"][1]
##print(game_character)
##
##del game_character["equip"]
##print(game_character)
##
##temp = game_character.pop("name")
##print(temp)
##print(game_character)
##
##del game_character
##print(game_character)


##potions = {
##    "red": "초보자용 HP 포션",
##    "blue": "초보자용 MP 포션",
##    "yellow": "초보자용 SP 포션",
##    "purple": "고급 HP/MP 포션"
##    }
##
##for name, description in list(potions.items()):
##    if "초보자용" in description:
##        del potions[name]
##
##print(potions)


followers = {
    "강민수": True,
    "이철수": False,
    "오민지": True,
    "박수민": False
    }

key = list(followers.keys())

print("이전 팔로워 :", key)

for key in list(followers.keys()):
    if followers[key] == False:
        del followers[key]

key = list(followers.keys())

print("현재 팔로워 :", key)






































      
