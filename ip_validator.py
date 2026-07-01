
ipaddress=input("ENTER AN IP ADDRESS:").split(".")
iplength=len(ipaddress)
print(iplength)
#s=int(iplength)
if iplength!=4:
    print("invalid")
    exit()
for i in ipaddress:
     try:
        num=int(i)
        if num<0 or num>255:
                print("invalid")
                exit()
     except:
        print("please enter valid address")
        exit()
else:
  print("valid")
