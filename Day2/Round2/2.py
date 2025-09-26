#You have n bulbs, all initially OFF. On the 1st pass you toggle every bulb; on the 2nd pass you toggle every 2nd bulb; on the 3rd pass you toggle every 3rd bulb... continuing until the nth pass. At the end, which bulbs remain ON? Hint: perfect squares only. What is the pattern and why do those bulbs remain lit? 
n = int(input("No. of Bulbs "))
lst = []
i = 1
while i*i <= n:
    lst.append(i*i)
    i += 1

print("Positions at which bulbs remain on: ", lst)
