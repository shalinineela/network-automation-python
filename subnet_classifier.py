A=input("ENTER AN IP ADDRESS:").split(".")
B=input("ENTER AN IP ADDRESS:").split(".")
lengthA=len(A)
lengthB=len(B)
print(lengthA)
print(lengthB)
#s=int(iplength)
if lengthA !=4:
    print("invalid")
    exit()
for i in A:
     try:
        num=int(i)
        if num <0 or num >255:
            print("invalid")
     except :
        print("please enter valid address")
        exit()
first=int(A[0])
if 1<=first<=126:
                print("class A")
                exit()
elif 128<=first<=191:
                print("class B")
                exit()
elif 192<=first<=223:
                print("class c")
                exit()
else:
            print("invalid")
            exit()
     
