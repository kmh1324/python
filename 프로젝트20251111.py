##class SalaryMan:
##    def __init__(self, salary = 1000000):
##        self.salary = salary
##    
##    def get_annual_gross(self):
##        return self.salary * 12 + (self.salary * 5)
##
##print(SalaryMan().get_annual_gross())
##print(SalaryMan(2000000).get_annual_gross())


##class Account:
##    def __init__(self, owner, balance):
##        self.__owner = owner
##        self.__balance = balance
##
##    def get_owner(self):
##        return self.__owner
##
##    def set_owner(self, value):
##        self.__owner = value
##
##    def get_balance(self):
##        return self.__balance
##
##    def set_balance(self, value):
##        self.__balance = value
##
##    def deposit(self, amount): 
##        self.set_balance(self.get_balance() + amount)
##        
##
##    def withdraw(self, amount):
##        if amount <= self.get_balance():
##            self.set_balance(self.get_balance() - amount)           
##        else :
##            return amount
##
##
##owner = input("계좌명을 입력하세요: ")
##account = Account(owner, 0)
##print(f"\n계좌명: {account.get_owner()}, 잔액: {account.get_balance()}\n")
##
##while True:        
##    menu = int(input("1. 입금, 2. 출금 입력(번호입력 외 종료): "))
##
##    if menu == 1:
##        amount = int(input("\n원하는 금액을 입금해주세요: "))
##        account.deposit(amount)
##        print(f"\n{amount}원 입금. 잔액 : {account.get_balance()}\n")
##        
##    elif menu == 2:
##        amount = int(input("\n원하는 출금액을 입력해주세요: "))
##        
##        if account.withdraw(amount) == amount:
##            print(f"\n잔액이 부족합니다.\n현재잔액: {account.get_balance()}\n")
##            continue
##        
##        print(f"\n{amount}원 출금. 잔액 : {account.get_balance()}\n")
##
##    else :
##        break


class FriendList:
    def __init__(self, friends = set()):
        self.friends = friends

    add_friend(self, name):
        if name not in self.friends:
            self.friends.add(self.name)
            print("추가 성공")
        else :
            print("추가 실패")

    remove_friend(self, name):
        if name in self.friends:
            self.friends.remove(name)
            print("삭제 성공")
        else :
            print("삭제 실패")

    has_friend
        
