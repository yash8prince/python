name = "Harry"

print(name[0:3])
print(name[-4:-1])
print(name[1:4])
print(name[:4]) #is same as print(name[0:4])
print(name[1:]) #is same as print(name[1:5])

#slicing with skip value

a = "0123456789"

print(a[4:7:2]) # 4:7= 456 and jump to second from 4