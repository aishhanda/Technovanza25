# A king taxes his subjects. If their income is over 1000 gold, the tax is 20%. If it's over 500 but not over 1000, it's 15%. If it's 500 or less but greater than 0, it's 10%. If income is 0, there is no tax. Given an income, calculate and print the exact gold amount owed in tax.
i = int(input("Income: "))
if i <= 0:
    print("No Tax")
elif i <= 500:
    a = i * 10/100
    print(a)
elif i <= 1000:
    a = 50 + (i - 500)*(15/100)
    print(a)
else:
    a = 125 + (i - 1000)*(20/100)
    print(a)
