def NumOfZeroesAndOnes(n):
    ones = 0
    zeroes = 0
    while(n):
        if (n&1==1):
            ones+=1
        else:
            zeroes+=1
        
        n>>=1
    print("Number of Ones: ", ones)
    print("Number of Zeroes: ", zeroes)
n = int(input("Enter a number: "))
NumOfZeroesAndOnes(n)
