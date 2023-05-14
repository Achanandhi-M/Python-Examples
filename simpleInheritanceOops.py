class Father:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def displayFather(self):
        print('Father Name:' , self.name)
        print('Father Age:' , self.age)
            

class Son(Father):
    def __init__(self, name,age):
        super().__init__(name,age)

    def displaySon(self):
          print('Son Name :' , self.name)
          print('Son Age :' , self.age)


fatherObj=Father("Arjunan",27)
fatherObj.displayFather()

sonObj=Son("Abimanyu", 18)
sonObj.displaySon()
sonObj.displayFather()#Inheriting the properites of Parent class