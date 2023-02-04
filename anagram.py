#write a program to check whether the given input is statisfying the condition of anagraph
#INPUT 1-LISTEN
#INPUT 2-SILENT
#output-true
#test case-2
#i1=space
#i2=racer
#output -false
str1=input("enter name:")
str2=input("enter name:")
a=len(str1)
b=len(str2)
sorta=sorted(str1)
sortb=sorted(str2)
if(a==b):
    if(sorta==sortb):
        print("it is a anagram")
    else:
        print("not a anagram")
else:
     print("  if length differs then not at all a anagram")
    