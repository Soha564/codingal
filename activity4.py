# Grocery Discont Checker
amount = 1200
loyal = True
banned = False
if banned or amount <= 0:
    print("Purchase denied.")
elif amount > 1000 and loyal:
    print(f"15% disconut is granted, {round(amount* 0.85, 2)}")
elif amount > 1000:
    print(f"10% discount is granted, {round(amount* 0.9, 2)}")
elif loyal:
    print(f"5% disconut is granted, {round(amount* 0.95, 2)}")
else:
    print("No discount granted.")
    