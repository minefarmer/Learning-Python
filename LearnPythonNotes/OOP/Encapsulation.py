'''ENCAPSULATION
Incapsulation is the process of restricting access to methods and variables in a class in order to prevent direct data modification so it prevents accidental data modification encapsulation, it basically allows the internal representation of an object to be hidden from view outside of the objects defination
Process of restricting access to methods and variables to prevent direct data modification
Public methods and variables are accessible from anywhere in a program
Privite methods and variables are accessible from thier own class

Double underscore prefix before an object name makes it private

Set method is used to set value for variable, while get method is used to retrieve the value of the variable

'''
# 
# 
# 
# 
# 
# 
# 
# 
# 
class Cars:
    def __init__ (self,speed,color):
        self.__speed = speed
        self.__color = color
    
    def set_speed(self,value):
        self.__speed = value
        
    def get_speed(self):
        return self.__speed
    
    def set_color(self,value):
            self.__color = value
        
    def get_color(self):
        return self.__color

ford = Cars(250, 'green')
nissan = Cars(300,'red')
toyata = Cars(350, 'blue')

ford.set_speed(750)

ford.__speed = 800

print(ford.get_speed())  # 500

print(ford.get_color())  # green
        