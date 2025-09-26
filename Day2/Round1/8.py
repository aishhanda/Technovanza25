# To join the Alchemist's Guild, your entry score must be over 70. However, if you have a special recommendation (a true/false value), you only need a score over 50. But, a perfect score of 100 makes you a 'MASTER' regardless of recommendation. Otherwise, you're an 'APPRENTICE' if you pass, or 'REJECTED'.
s = int(input("Entry Score: "))
r = input("Recommendation? (True/False): ").strip().lower() == "true"

if s == 100:
    print("MASTER")
elif (s > 50 and r) or s > 70:
    print("APPRENTICE")
else:
    print("REJECTED")
