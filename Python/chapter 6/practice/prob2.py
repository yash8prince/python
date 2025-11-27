m1 = int(input("subject 1: "))
m2 = int(input("subject 2: "))
m3 = int(input("subject 3: "))
    
m= (m1+m2+m3)/300*100

if(m>=40 and m1>=33 and m2>=33 and m3>=33):
    print("Passed: %",m)
else:
    print("failed: %",m)
