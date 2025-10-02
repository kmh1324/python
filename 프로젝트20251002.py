##def factorial(n):
##    output = 1
##    for i in range(1, n + 1):
##        output *= i
##
##    return output
##
##print("1!:", factorial(1))
##print("2!:", factorial(2))
##print("3!:", factorial(3))
##print("4!:", factorial(4))
##print("5!:", factorial(5))


##def factorial(n):
##    if n == 0:
##        return 1
##    else:
##        return n * factorial(n - 1)
##
##print("1!:", factorial(1))
##print("2!:", factorial(2))
##print("3!:", factorial(3))
##print("4!:", factorial(4))
##print("5!:", factorial(5))


##def fibonacci(n):
##    if n == 1:
##        return 1
##    if n == 2:
##        return 1
##    else:
##        return fibonacci(n - 1) + fibonacci(n - 2)
##
##print("fibonacci(1):", fibonacci(1))
##print("fibonacci(2):", fibonacci(2))
##print("fibonacci(3):", fibonacci(3))
##print("fibonacci(4):", fibonacci(4))
##print("fibonacci(5):", fibonacci(5))


##counter = 0
##
##def fibonacci(n):
##    print("fibonacci({})를 구합니다.".format(n))
##    global counter
##    counter += 1
##
##    if n == 1:
##        return 1
##    if n == 2:
##        return 1
##    else:
##        return fibonacci(n - 1) + fibonacci(n - 2)
##
##fibonacci(10)
##print("---")
##print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(counter))


##counter = 0
##
##def fibonacci(n):
##    counter += 1
##    if n == 1:
##        return 1
##    if n == 2:
##        return 1
##    else:
##        return fibonacci(n - 1) + fibonacci(n - 2)
##
##print(fibonacci(10))


##dictionary = {
##    1: 1,
##    2: 1
##}
##
##def fibonacci(n):
##    if n in dictionary:
##        return dictionary[n]
##    else:
##        output = fibonacci(n - 1) + fibonacci(n - 2)
##        dictionary[n] = output
##        return output
##
##print("fibonacci(10):", fibonacci(10))
##print("fibonacci(20):", fibonacci(20))
##print("fibonacci(30):", fibonacci(30))
##print("fibonacci(40):", fibonacci(40))
##print("fibonacci(50):", fibonacci(50))


##def flatten(data):
##    output = []
##    for item in data:
##        if type(item) == list:
##            output += item
##        else:
##            output.append(item)
##    return output
##
##example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
##print("원본:", example)
##print("변환:", flatten(example))


##def flatten(data):
##    output = []
##    for item in data:
##        if type(item) == list:
##            output += flatten(item)
##        else:
##            output.append(item)
##    return output
##
##example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
##print("원본:", example)
##print("변환", flatten(example))







    
