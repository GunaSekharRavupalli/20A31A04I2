email="guna@gmail.com"
pwd=1234
otp=46211
cemail=input("enter email:")
cpwd=int(input("enter pwd:"))
if(email==cemail and pwd==cpwd):
    cotp=int(input("enter OTP:"))
    if(otp==cotp):
        print("otp enterd succesful")
    else:
            print("wrong otp buddyy")
    print("login unsuccessful")
elif(email!=cemail and pwd==cpwd):
    print("login failed due to mail")
elif(email==cemail and pwd!=cpwd ):
    print("login failed due to password")
else:
    print("sorry dude!!!!")


a=5
b=True
if(0==True):
    print("cool")
else:
    print("hot")

    