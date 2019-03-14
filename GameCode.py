#This is an Adventure game devloped my Adriana Pitt.
#It is based in the future, where cybernetic implants and modifications have taken over.
#This is a DECISION based game. Your Decisionw will affect the outcome you experience.
healthPoint = 0

charClass = int(input("Please choose which class you wish to use: \n Press 1 for Tank \n Press 2 for Rouge \n Press 3 for Assassin ")) 
if charClass == 1:
                healthPoint = healthPoint + 150
elif charClass == 2:
                healthPoint = healthPoint + 100
elif charClass == 3:
                healthPoint = healthPoint + 60

print(healthPoint)
