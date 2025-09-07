# Write a program to create two classes for two different countries that consist of three methods to display the following information of respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes.

class England:
    def capital(self):
        print("The capital of the England is London.")

    def language(self):
        print("Usually, people in England speak English.")

class Japan:
    def capital(self):
        print("The capital of Japan is Tokyo.")

    def language(self):
        print("Usually, people in Japan speak Japanese.")


class China:
    def capital(self):
        print("The capital of China is Beijing.")

    def language(self):
        print("Usually, people in China speak Mandarin.")

e = England()
j = Japan()
c = China()

# Polymorphism
countries = (e, j, c)

for country in countries:
    print("\n ---------------------------------------\n")
    country.capital()
    country.language()
    print("\n ---------------------------------------\n")


