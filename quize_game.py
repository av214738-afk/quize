print("Welcome to my computer quize!")

playing=input("Do you want to play? ")

if playing != "yes":
    
    print("Okay! Let's play:)")

answer=input("What does CPU stand for? ")
if answer == "central processing unit":
    print("correct!")
else:
    print("Incorrect!")

answer=input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("correct!")
else:
    print("Incorrect!")

answer=input("What does RAM stand for? ")
if answer == "random access memory":
    print("correct!")
else:
    print("Incorrect!")

answer=input("What does HTTPS stand for? ")
if answer == "hypertext transfer protocol secure":
    print("correct!")
else:
    print("Incorrect!")
