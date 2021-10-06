import random
rondes = 1
verloren = 0
gewonnen = 0

def verschil(gok):
    verschil = abs (n - gok)
    if verschil <= 20 and verschil >= -20:
        print ("Je bent heel warm")
    elif verschil <= 50 and verschil >= -50:
        print ("Je bent warm")
 

while rondes <= 2:
    guesses = 10
    n = random.randint(1, 1000)
    print(n)
    print('Dit is ronde ' + str(rondes))
    while True:
        if guesses == 0:
            verloren += 1
            break
        print('Je hebt nog ' + str(guesses) + ' guesses')
        gok = (int(input ("Raad het getal. ")))
        if gok > n :
            print ("Lager")
            verschil(gok)
        elif gok < n:
            print ("Hoger")
            verschil(gok)
        elif gok == n:
            print ("Geraden")
            gewonnen += 1
            break
        guesses -= 1


    print('\nJe hebt ' + str(gewonnen) + ' gewonnen en zoveel ' + str(verloren) + ' Verloren')
    rondes += 1


