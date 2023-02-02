#ARM strong number
#rule : 371= no of digits=3
#3^3+7^3+1^3=373
sum=0
n=(int(input("enter numberrrrr")))
while(n!=0):
    r=n/10
    sum+=(r*r*r)/(pow(r,3))
    n=n/10
    if(sum==n):
       print("armstong")
    else:
        print("not")

