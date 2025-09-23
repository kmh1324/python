##dictionary = {
##    "name": "7D 건조 망고",
##    "type": "당절임",
##    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
##    "origin": "필리핀"
##    }
##
##print("name:", dictionary["name"])
##print("type:", dictionary["type"])
##print("ingredient:", dictionary["ingredient"])
##print("origin:", dictionary["origin"])
##print()
##
##dictionary["name"] = "8D 건조 망고"
##print("name:", dictionary["name"])


##dictionary = {}
##
##print("요소 추가 이전:", dictionary)
##
##dictionary["name"] = "새로운 이름"
##dictionary["head"] = "새로운 정신"
##dictionary["body"] = "새로운 몸"
##
##print("요소 추가 이후:", dictionary)


##dictionary = {
##    "name": "7D 건조 망고",
##    "type": "당절임"
##    }
##
##print("요소 제거 이전", dictionary)
##
##del dictionary["name"]
##del dictionary["type"]
##
##print("요소 제거 이후", dictionary)


##dictionary = {
##    "name": "7D 건조 망고",
##    "type": "당절임",
##    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
##    "origin": "필리핀"
##    }
##
##key = input("> 접근하고자 하는 키: ")
##
##if key in dictionary:
##    print(dictionary[key])
##else:
##    print("존재하지 않는 키에 접근하고 있습니다.")


##dictionary = {
##    "name": "7D 건조 망고",
##    "type": "당절임",
##    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
##    "origin": "필리핀"
##    }
##
##value = dictionary.get("존재하지 않는 키")
##print("값:", value)
##
##if value == None:
##    print("존재하지 않는 키에 접근했었습니다.")
    

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "차자황색소"],
    "origin": "필리핀"
    }

for key in dictionary:
    print(key, ":", dictionary[key])
