print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play.")
score = 0

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score += 1 
else: 
    print("Incorrect!")
    
answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1 
else: 
    print("Incorrect!")

answer = input("What is the standard port number for HTTPS? ")

if answer.lower() == "443":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    
    
answer = input("What is the standard port number for SFTP? ")

if answer.lower() == "22":
    print("Correct!")
    score += 1 
else: 
    print("Incorrect!")

answer = input("What is the standard port number for DNS? ")

if answer.lower() == "53":
    print("Correct!")
    score += 1 
else: 
    print("Incorrect!")
    
answer = input("What does WAF stand for? ")

if answer.lower() == "web application firewall":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 6) * 100) + "%.")