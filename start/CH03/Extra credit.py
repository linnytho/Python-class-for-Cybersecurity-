for number in range (3):
     number = int(input ("Sample output:"))
     if number > 1:
        for i in range(2, number):
            if number % i == 0:
                 print (number, "is NOT prime")
                 break
        else:
            print (number, "is prime")