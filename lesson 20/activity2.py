import random
import time

def getRandomDate(starDate, endDate):
    print("Print random date between", starDate, "and", endDate)

    randomGenerator = random.random()
    dateformat = '%m/%d/%Y' # MM/DD/YYYY


    startTime = time.mktime(time.strptime(starDate, dateformat))
    # time.mktime(time.strptime(starDate, dateformat)) => (Y, m, d, ...)
    #time.mktime => 1577825200.0
    endTime = time.mktime(time.strptime(endDate, dateformat))

    randomTime = startTime + randomGenerator * (endTime - startTime)

    print(randomTime)
    randomDate = time.strftime(dateformat, time.localtime(randomTime))

    print(time.localtime(randomTime))
    print(time.strftime(dateformat, time.localtime(randomTime)))

    return randomDate

    

print("Random date =", getRandomDate ("1/1/2020", "12/30/2025"))


