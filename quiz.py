print("Welcome to my computer quiz :)..")

playing = input('Do you want to play?? ')

if playing.lower() != "yes":
    quit()

print('ok lets play..' )
score = 0

answer = input("What is the capital of india? ")
if answer == "Delhi": 
    print('correct!')
    score += 1
else:
    print('incorrect!')


answer = input("The ram stand for? ")
if answer == "Random access memory": 
    print('correct!')
    score += 1
else:
    print('incorrect!')


answer = input("In memory full name of kb? ")
if answer == "kilobyte":
    print('correct')
    score += 1
else:
    print('incorrect!') 


answer = input("What is the smallest unit of data in computer? ")
if answer == "Bit": 
    print('correct!')
    score += 1
else:
    print('incorrect!') 


answer = input("In 1st generation of computer which technology was used? ")
if answer == "Vaccum tube": 
    print('correct!')
    score += 1
else:
    print('incorrect!')

print("You got " + str(score) + " Question correct!" )
print("You got " + str((score / 5) * 100) + "%." )