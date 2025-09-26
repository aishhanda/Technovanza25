"""You are at coordinates (x, y) in a maze. You can escape if you are on the edge (x=0 or y=0) but NOT if you are in a corner (x=0 AND y=0). If you can escape, print 'ESCAPE'. Otherwise, print 'TRAPPED'."""
x = int(input("Type X: "))
y = int(input("Type Y: "))
if (x == 0 or y == 0) and not (x == 0 and y == 0):
    print("ESCAPE")
else:
    print("TRAPPED")
