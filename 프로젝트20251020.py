##import random 
##
##print("# random 모듈")
##
##print("- random():", random.random())
##
##print("- uniform(10, 20):", random.uniform(10, 20))
##
##print("- randrange(10):", random.randrange(10))
##
##print("- choice([1, 2, 3, 4, 5]):", random.choice([1, 2, 3, 4, 5]))
##
##print("- shuffle([1, 2, 3, 4, 5]):", random.shuffle([1, 2, 3, 4, 5]))
##
##print("- sample([1, 2, 3, 4, 5], k=2):", random.sample([1, 2, 3, 4, 5], k=2))


##import sys
##
##print(sys.argv)
##print("---")
##
##print("getwindowsversion:()", sys.getwindowsversion())
##print("---")
##print("copyright:", sys.copyright)
##print("---")
##print("version:", sys.version)
##
##sys.exit()


import os

print("현재 운영체제:", os.name)
print("현재 폴더:", os.getcwd)
print("현재 폴더 내부의 요소:", os.listdir())

os.mkdir("hello")
os.rmdir("hello")

with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

os.remove("new.txt")

os.system("dir")
