#!/usr/bin/env python3
# example workign with Functions
#By 

def rick_roll():
 print ("Never gonna give you up.")
 print ("Never gonna let you down.")
 print ("Never gonna run around.")
 print ("And hurt you.")

def add_two_nums(num1, num2):
 answer= num1 + num2
 print (answer)

def mult_two_nums (num1, num2):
 answer = num1 * num2
 return answer

ans = mult_two_nums(5,6)
print(ans)
ans = mult_two_nums(ans,7)
print(ans)


 #rick_roll()
#print ("Were no strangers to love.......")
#rick_roll()

add_two_nums(5, 7)
add_two_nums(12,89)
foo = 42
bar = 8675309
add_two_nums(foo,bar)

num1 = 5
num2 = 7
add_two_nums(num2, num1)