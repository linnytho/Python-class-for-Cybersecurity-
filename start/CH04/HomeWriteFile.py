import os

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
file_path = os.path.join(script_dir,"hackme.txt")

name = input("What is your name")
color = input ("What is your favorite color")
pet = input("What was your first pet's name")
mother = input("What is your mother's maiden name")
school= input("What elementary school did you attend")

f = open(file_path,"w")
f.write(name+"\n")
f.write(color+"\n")
f.write(pet+"\n")
f.write(mother+"\n")
f.write(school+"\n")
f.close()

f = open (file_path,"r")
print ("Here is someone to hack - imfortmation")
print(f.read())
f.close()