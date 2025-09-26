# An oracle gives you three numbers. The prophecy is 'TRUE' only if one of the numbers is positive, one is negative, and one is zero. In any other case, the prophecy is 'FALSE'. Check the numbers and reveal the truth.
a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
z = 0
n = 0
p = 0
for i in [a, b, c]:
    if i == 0:
        z += 1
    elif i < 0:
        n += 1
    else:
        p+=1
if z == 1 and p == 1 and n == 1:
    print("TRUE")
else:
    print("FALSE")
