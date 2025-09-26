# A potion's color changes based on temperature. If it's below 0, it turns 'BLUE'. If it's above 100, it turns 'RED'. If it's exactly 50, it turns 'PURPLE'. For anything else, it remains 'CLEAR'. What color is the potion?
t = int(input("Temperature: "))
if t < 0:
    print("BLUE")
elif t == 50:
    print("RED")
elif t > 100:
    print("PURPLE")
else:
    print("CLEAR")
