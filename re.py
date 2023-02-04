import re
'''str1="she sells apples"
str2="sells"
if re.match(str1,str2):
    print("match found")
else:
    print(str2,"not present")
str3="hello"
if re.match(str1,str3):
    print("foundv match")'''
import re
str1 ="she sells apples"
str2 ="sells"
if re.search(str1,str2):
    print("match found")
else:
    print(str2,"not present")
import re
str1 ="she sells sea shells at sea shore"
str2 ="sea"
rep=" ocean"
ns=re.sub(str2,rep,str1,1)
print(ns)
import re#re-regular 
p=r"[a,e,i,o,u]"
if re.search(p,"bsvc"):
    print("match found")
else:
    print("match not found")
    