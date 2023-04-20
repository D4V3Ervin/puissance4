import time

grille = [[0 for x in range(7)] for y in range(6)]
def Spawntab(grille):
    for i in grille:
            print(i)

player1 = 1
player2 = 2

def partie():
    print('Bienvenue dans cette partie de puissance 4 version python, mes chers joueurs 1 et 2 !')
    time.sleep(3)
    print('Le propriétaire de ce pc sera le joueur 1, et son pion sera défini comme un "1"!')
    time.sleep(1)
    print('Le second joueur, lui, aura droit à un magnifique "2" !! ')
    time.sleep(1)
    a = str(input('Compris ?(Répondez Oui/Non)'))
    if a == "Oui":
        print('Bien, alors commençons !')
    elif a == "Non":
        print('Eh bien, tant pis pour vous, on commence !')
    elif a == "Quel est le sens de la vie ?":
        print("Je suis pas prof moi, Google existe !")
    time.sleep(4)
    print('Commençons sans plus tarder ! Joueur 1, par quelle colonne allez vous commencer ?')
    line = int(input('Alors ?'))
    column = 5
    grille[column][line] = player1
    Spawntab(grille)