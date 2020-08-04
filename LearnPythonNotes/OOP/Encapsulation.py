'''ENCAPSULATION
Incapsulation is the process of restricting access to methods and variables in a class in order to prevent direct data modification so it prevents accidental data modification encapsulation, it basically allows the internal representation of an object to be hidden from view outside of the objects defination
Process of restricting access to methods and variables to prevent direct data modification
Public methods and variables are accessible from anywhere in a program
Privite methods and variables are accessible from thier own class

Double underscore prefix before an object name makes it private



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
        self.speed = speed
        self.color = color
    
    def set_speed(self,value):
        self.speed = value
        
    def get_speed(self):
        return self.speed

ford = Cars(250, 'green')
nissan = Cars(300,'red')
toyata = Cars(350, 'blue')

ford.set_speed(450)

ford.speed = 500

print(ford.get_speed())  # 500

print(ford.color)  # green
        