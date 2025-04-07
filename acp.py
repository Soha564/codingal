# Rohan is bored wearing the jacket and pullover now. He wants to wear something light and soft. But he also doesn't want to get the cold by not wearing weather-appropriate clothes. So he will design a program and check what temperature is suitable for wearing light clothes.
print("/n🌨️ 🌧️ 🌸 ☀️ 🍂  Temperature Guide  🌨️ 🌧️ 🌸 ☀️ 🍂/n")
temp = int(input("Please enter the temperature:"))
rain =  input("Please state with a yes or no if it raining:")
if temp >= 8 and temp <= 15 and rain == "yes":
    print("I believe it is spring and i would suggest that u wear a rain coat or something light yet waterproof.")
elif temp >= 16 and temp <=20 and rain == "no":
    print("I belive it is summer time and i would suggest to wear a cardigan or something light.")
elif temp > 20 and rain == "no":
    print("I believe it is summer and i would suggest not to wear any type of jacket / coat or even a cardigan")
elif temp <= 7 and rain == "no":
    print("I believe it is winter and i would suggest to wear a thick coat that has good insulation and maybe consider a scarf, hat and gloves.")
elif temp >= 8 and temp <= 15 and rain == "no":
    print("I believe it is autumn, and i would suggest to wear a medium weight jackethowever mabey layering abit more in the morning might help since the morning tends to be more chillly and the afternoon more milder.")
else:
    print("Sorry but your description doesn't correlate?")
print("Have fun outside!")
