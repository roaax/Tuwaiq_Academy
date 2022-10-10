
''' Intro To Python'''
print("Test")
My_age = 24
print(My_age)

#-------------------------------
# Define Variables & Print it
#-------------------------------
print("-----------Define Variables & Print it-------------")

my_age :int = 24
my_name : str = "Roaa"
print(my_age, my_name)

#-----------------------------------
#   Assign One Value to multi var 
#-----------------------------------
var1 = var2 = var3 = "Same Value"
# All var1 , var2 , var3 will print the same value 
print("-----------Assign One Value to Multiple Variables -------------")
print(var1)
print(var2) 
print(var3)

#--------------------------------------------------
#   Assign multiple Values to Multiple Variables
#--------------------------------------------------
print("-----------Assign Multiple Values to Multiple Variables -------------")
var4 , var5 = 33 , "Hi"
print(var4 , var5)




#-----------------------------------
#      Convert from string to int
#-----------------------------------
print("----------- Convert from string to int -------------")
some_value  : str = "50"
some_value_int  : int = int(some_value)
print(some_value_int)