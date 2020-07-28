# this is the value a function uses when called without passing it a value
# only parameters at the end of a parameter list can have a default value as Values are assigned by position
#       example    def greeting(a,b=7)

def student_names(names='Bluelime'):
    print('Hello ' + names)
    
student_names()  # Hello Bluelime   **** The default value
student_names('Rich')  # Hello Rich
student_names('Carl')  # Hello Carl

