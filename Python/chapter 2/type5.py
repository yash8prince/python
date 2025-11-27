a = 45
t = type(a) # class type <int>
print(t)

a = "Yash"
t = type(a) # class type <str>
print(t)

a = "23.65"
t = type(a) # class type <str>
print(t)
# change type of variable 
a = "23.65"
b = float(a) # but the type should be float
t = type(b)
print(t)