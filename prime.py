num = 21
var = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            var = True
    if var:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")