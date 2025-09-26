# A goblin demands a toll. If a traveler has more than 50 silver OR more than 5 gold, they pay the 'RICH TAX'. If they have less than 10 silver AND 0 gold, they are 'TOO POOR' and pass free. Everyone else pays the 'NORMAL TOLL'. What is the traveler's fate?
s = int(input("Silver coins: "))
g = int(input("Gold coins: "))
if s > 50 or g > 5:
    print("RICH TAX")
elif s < 10 and g == 0:
    print("TOO POOR")
else:
    print("NORMAL TOLL")
