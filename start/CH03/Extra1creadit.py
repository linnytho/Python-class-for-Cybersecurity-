for i in range(3):
    number = int (input("What is the number:"))
    divisor = int (input("What is the divisor:"))
    if number % divisor== 0:
        print(number,"is divisible by",divisor)
    else:
        print(number,"is NOT divisible by",divisor)