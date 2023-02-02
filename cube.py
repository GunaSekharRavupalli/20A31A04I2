#john is a 3rd grade student doing maths work at home
#he should write 1-1000 while writting he found some numbers are not happy
#so he asked his mum
#x=97
#1-happy number
#2-9-SAD numbers
###################################################################################
#write a python program to make list of cubestill the  value n
#test cases:10
#[0,1,8,27,64.__________________1000]
n=int(input("enter number"))
List=[]
for i in range(n+1):
    List.append(i**3)
print(List)   
      
