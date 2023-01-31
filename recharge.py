calls=3000
C_calls=int(input("enter no of calls:"))
msgs=100
c_msgs=int(input("enter no of messages:"))
data=2.0
c_data=float(input("enter no of data:"))
days=84
c_days=int(input("enter no of days:"))
res=days-c_days
print(res)
if(days>=c_days):
    print("no of days remaining:",res)
    if(calls>=C_calls):
        print("no of calls remaing:",calls-C_calls)
    else:
        print("please top up")
        if(msgs>=c_msgs):
           print("no of msgs remaining:",msgs-c_msgs)
        else:
             print("msgs are over for today")
             if(data>=c_data):
                print("remaing data:",data-c_data)
             else:
                print("data over my buddy")
else:
    print("plan expired")
  




          