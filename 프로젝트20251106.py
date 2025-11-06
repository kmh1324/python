##import math
##
##
##class Circle:
##    def __init__(self, radius):
##        self.radius = radius
##
##    def get_circumference(self):
##        return 2 * math.pi * self.radius
##
##    def get_area(self):
##        return math.pi * (self.radius ** 2)
##
##circle = Circle(10)
##print("원의 둘레:", circle.get_circumference())
##print("원의 넓이:", circle.get_area())


##import math
##
##class Circle:
##    def __init__(self, radius):
##        self.__radius = radius
##
##    def get_circumference(self):
##        return 2 * math.pi * self.__radius
##
##    def get_area(self):
##        return math.pi * (self.__radius ** 2)
##
##
##circle = Circle(10)
##print("# 원의 둘레와 넓이를 구합니다.")
##print("원의 둘레:", circle.get_circumference())
##print("원의 넓이:", circle.get_area())
##print()
##
##print("# radius에 접근합니다.")
##print(circle.__radius)


##import math
##
##class Circle:
##    def __init__(self, radius):
##        self.__radius = radius
##
##    def get_circumference(self):
##        return 2 * math.pi * self.__radius
##
##    def get_area(self):
##        return math.pi * (self.__radius ** 2)
##
##    def get_radius(self):
##        return self.__radius
##
##    def set_radius(self, value):
##        self.__radius = value
##
##circle = Circle(10)
##print("원의 둘레와 넓이를 구합니다.")
##print("원의 둘레:", circle.get_circumference())
##print("원의 넓이:", circle.get_area())
##print()
##
##print("# __radius에 접근합니다.")
##print(circle.get_radius())
##print()
##
##circle.set_radius(2)
##print("반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
##print("원의 둘레:", circle.get_circumference())
##print("원의 넓이:", circle.get_area())


##import math
##
##class Circle:
##    
##    def __init__(self, radius):
##        self.__radius = radius
##        
##    def get_circumference(self):
##        return 2 * math.pi * self.__radius
##    
##    def get_area(self):
##        return math.pi * (self.__radius ** 2)
##    
##    @property
##    def radius(self):
##        return self.__radius
##
##    @radius.setter
##    def radius(self, value):
##        if value < 0:
##            raise TypeError("길이는 양의 숫자여야 합니다.")
##        self.__radius = value
##
##print("# 데코레이터를 사용한 Getter와 Setter")
##circle = Circle(10)
##print("원래 원의 반지름:", circle.radius)
##circle.radius = 2
##print("변경된 원의 반지름:", circle.radius)
##print()
##
##print("# 강제로 예외를 발생시킵니다.")
##circle.radius = -10


##class Parent:
##    def __init__(self):
##        self.value = "테스트"
##        print("Parent 클래스의 __init()__메소드가 호출되었습니다.")
##
##    def test(self):
##        print("Parent 클래스의 test() 메소드입니다.")
##
##class Child(Parent):
##    def __init__(self):
##        super().__init__()
##        print("Child 클래스의 __init()__ 메소드가 호출되었습니다.")
##
##child = Child()
##child.test()
##print(child.value)


##class CustomException(Exception):
##    def __init__(self):
##        super().__init__()
##
##raise CustomException


##class CustomException(Exception):
##    def __init__(self):
##        super().__init__()
##        print("#### 내가 만든 오류가 생성되었어요! ####")
##
##    def __str__(self):
##        return "오류가 발생했어요"
##
##raise CustomException


##class CustomException(Exception):
##    def __init__(self, message, value):
##        super().__init__()
##        self.message = message
##        self.value = value
##
##    def __str__(self):
##        return self.message
##
##    def print(self):
##        print("##### 오류 정보 #####")
##        print("메시지:", self.message)
##        print("값:", self.value)
##
##try:
##    raise CustomException("딱히 이유 없음", 273)
##except CustomException as e:
##    e.print()


##class Customer:
##    def __init__(self, name, customer_id):
##        self.__name = name
##        self.__customer_id = customer_id
##
##    def name(self):
##        return self.__name
##
##    def customer_id(self):
##        return self.__customer_id
##
##    def get_name(self):
##        return self.__name
##
##    def get_customer_id(self):
##        return self.__customer_id
##
##    def set_name(self, value):
##        self.__name = value
##
##    def set_customer_id(self, value):
##        self.__customer_id = value
##
##customer = Customer("abc", 1234)
##
##name = input("고객명을 입력해주세요: ")
##customer.set_name(name)
##
##customer_id = int(input("고객 번호를 입력해주세요: "))
##customer.set_customer_id(customer_id)
##
##print(customer.name())
##print(customer.customer_id())


class Circle:
    PI = 3.141592
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return self.radius * self.radius * Circle.PI

class Cylinder:
    def __init
