class numb: #protected variable single underscore
    def __init__(self):
        self._protectedVar = 0
obj = numb()
obj._numbVar = 100
print(obj._numbVar)

class Protected: #Protected and Private, private noted by double undersore
    def __init__(self):
        self.__privateVar = 50

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(25)
obj.getPrivate()
