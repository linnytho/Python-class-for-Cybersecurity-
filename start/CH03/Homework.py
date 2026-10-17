def send_message ():
   for i in range (10):
       print("Yeah it is")
       
answer= input ("Is today a good day? (y/n)")

if answer =="y" or answer =="Y":
     send_message() 
elif answer =="n" or answer == "N":
    print("No it is not")
 