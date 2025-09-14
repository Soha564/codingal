import random
class FruitQuiz:
    # Create a constructor
    def __init__(self):

        # Create a dictionary of fruits as keys and outside colour as value
        self.fruits =  {'apple':'red',
                        'orange' : 'orange',
                        'watermelon': 'green',
                        'banana': 'yellow'}
        
    # Function for the quiz, here a fruit will be cosen randomly
    def quiz(self):
        while(True):

            fruit, colour = random.choice(list(self.fruits.items()))

            print("What is the outside colour of {}".format(fruit))

            user_answer = input()
            if(user_answer.lower() == colour):
                print("Correct Answer!")
            else:
                print("Wrong Answer..")
            option = int(input("Enter 0, if you want to continue otherwise enter 1: "))
            if option:
                break
print("Welcome to the Fruit Quiz!")
fq = FruitQuiz()
fq.quiz()