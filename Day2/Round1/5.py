# A royal adviser must categorize a citizen based on their age. If they are under 18, they are a 'MINOR'. If they are 18 to 65 (inclusive), they are an 'ADULT'. However, if their age is exactly 25 and they have a royal decree (true/false value), they are a 'NOBLE'. Anyone over 65 is an 'ELDER'. Determine their title.
a = int(input("Age: "))
d = input("Royal Decree?(yes / no): ").lower()
if a < 18:
    print("MINOR")
elif a == 25 and d == "yes":
    print("NOBLE")
elif 18 <= a <= 65:
    print("ADULT")
else:
    print("ELDER")
