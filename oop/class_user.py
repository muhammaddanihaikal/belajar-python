class User:
    
    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.__name = name
    
    def getUser(self) :
        return {
            "email" : self.__email,
            "password" : self.__password,
            "name" : self.__name
        }

    def setUser(self, email, password, name):
        self.__email = email
        self.__password = password
        self.__name = name


user1 = User("user1@gmail.com", "123", "dani")
print(user1.getUser())
user1.setUser(
    "user1a@gmail.com",
    "1234",
    "dania"
)
print(user1.getUser())