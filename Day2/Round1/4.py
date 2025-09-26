# A guardian has three heads, each speaking a number. You can only pass if the sum of ANY two heads' numbers is greater than the third head's number. This must be true for all three combinations! If you can pass, print 'PROCEED', otherwise, print 'HALT'.
a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
if a > (b+c) and b > (a+c) and c > (a+b):
    print("PROCEED")
else:
    print("HALT")
