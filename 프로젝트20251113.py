##class FriendList:
##    def __init__(self):
##        self.friends = set()
##
##    def add_friend(self, name):
##        if not self.has_friend(name):
##            self.friends.add(name)
##            print("추가 성공")
##        else :
##            print("추가 실패")
##
##    def remove_friend(self, name):
##        if self.has_friend(name):
##            self.friends.remove(name)
##            print("삭제 성공")
##        else :
##            print("목록에 없는 친구입니다.")
##
##    def has_friend(self, name):
##        return name in self.friends
##
##    def get_all(self):
##        return sorted(list(self.friends))
##
##
##friends = FriendList()
##
##print(friends.get_all())
##
##friends.add_friend('c')
##friends.add_friend('a')
##friends.add_friend('b')
##print(friends.get_all())
##
##friends.remove_friend('a')
##print(friends.get_all())
##
##print(friends.has_friend('a'))
##print(friends.has_friend('b'))



##class WordDictionary:
##    def __init__(self):
##        self.words = {}
##
##    def add_word(self, word, meaning):
##        if word not in self.words:
##            self.words[word] = meaning
##            print("성공")
##        else :
##            print("실패")
##
##    def remove_word(self, word):
##        if word in self.words:
##            del self.words[word]
##            print("성공")
##        else:
##            print("존재하지 않는 단어입니다.")
##
##    def get_meaning(self, word):
##        if word in self.words:
##            return self.words[word]
##        else :
##            print("등록되지 않은 단어입니다.")
##            
##    def get_all(self):
##        print(self.words)
##
##
##
##
##words = WordDictionary()
##
##words.add_word('a', 'ㄱ')
##words.add_word('a', 'ㄱ')
##words.add_word('b', 'ㄴ')
##words.get_all()
##words.remove_word('b')
##words.remove_word('c')
##words.get_all()
##print(words.get_meaning('a'))
##print(words.get_meaning('b'))




