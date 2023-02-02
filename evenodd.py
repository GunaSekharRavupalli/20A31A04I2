num = int(input("enter"))
string1 = str(num)
evensum = 0
oddsum = 0
for i in range(0, len(string1)):
    if(i % 2 == 0):
        evensum += int(string1[i])
    else:
        oddsum += int(string1[i])
print(abs(evensum-oddsum))
    