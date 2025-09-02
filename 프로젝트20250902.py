num1 = int(input("숫자1 : "))
num2 = int(input("숫자2 : "))

if num1 > num2:
    num1, num2 = num2, num1

while True:
    num1 += 1
    if num1 >= num2:
        break
    
    print(f"{(num1) * (num1)}   ", end = "")
