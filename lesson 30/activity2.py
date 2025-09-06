# Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.

class Computer:
    __selling_price = 1000

    # getter method
    def getSellingPrice(self):
        return self.__selling_price
    # setter method
    def setSellingPrice(self, price):
        self.__selling_price = price


comp = Computer()
# print(comp.__selling_price) - will show attribute error
print("Initial price: ", comp.getSellingPrice())
comp.setSellingPrice(2000)
print("Current price; ", comp.getSellingPrice())