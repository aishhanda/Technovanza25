# A dragon guards three piles of gold: 10, 15, and 20 coins. A knight can only pass if the total is NOT exactly 45, AND the first pile has exactly 10 coins. Tell the knight if he should 'PASS' or 'FAIL'.
a, b, c = 10, 15, 20

if a == 10 and (a + b + c != 45):
    print("PASS")
else:
    print("FAIL")
