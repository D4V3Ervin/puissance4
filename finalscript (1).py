import time

grille = [[0 for x in range(7)] for y in range(6)]
def Spawntab(grille):
    for i in grille:
            print(i)

player1 = 1
player2 = 2

win1 = 'Félicitation, le joueur 1 a remporté la partie, avec une magnifique ligne de 1 horizontale !'
win2 = 'Félicitation, le joueur 2 a remporté la partie, avec une magnifique ligne de 2 horizontale !'
win3 = 'Félicitation, le joueur 1 a remporté la partie, avec une magnifique ligne de 1 verticale !'
win4 = 'Félicitation, le joueur 2 a remporté la partie, avec une magnifique ligne de 2 verticale !'
win5 = 'Félicitation, le joueur 1 a remporté la partie, avec une magnifique ligne de 1 en diagonale !'
win6 = 'Félicitation, le joueur 2 a remporté la partie, avec une magnifique ligne de 2 en diagonale !'
win7 = 'Match nul, bravo à vous deux !'

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
    print('Bien, à toi, deuxième joueur !')
    time.sleep(1)
    column = 5
    while column >= 0 and column >= 5:
        line = int(input("Alors ? (Si vous avez déja placé un pion et que ce message apparait, c'est que l'emplacement du jeton est mauvais ! "))
        if line >6 or line <0:
            print("Cette ligne n'est pas correcte !")
        if grille[column][line] == 0 and column == 5:
            grille[column][line] = player2
            break
        elif grille[column][line] == 1 and grille[column-1][line] == 0 :
            grille[column-1][line] = player2
            break
        elif grille[column][line] == 1 and grille[column-1][line] == 1  and  grille[column-2][line] == 0 :
            grille[column-2][line] = player2
            break
        elif grille[column][line] == 1 and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] == 0:
            grille[column-3][line] = player2
            break
        elif grille[column][line] == 1 and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] ==1 and grille[column-4][line] == 0:
            grille[column-4][line] = player2
            break
        elif grille[column][line] == 1 and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] ==1 and grille[column-4][line] == 1 and grille[column-5][line] == 0:
            grille[column-5][line] = player2
            break
    Spawntab(grille)
#---------------------------------------------------------------------------------------------------------jusque la, aucune erreur---------------------------------------------------------------------------
    for i in range(20):
        time.sleep(2)
        column = 5
        line = int(input(" Joueur 1, sélectionnez votre colonne !(Si vous avez déja placé un pion ce tour-si et que ce message apparait, c'est que la colonne choisie est remplie ! "))
        if (grille[0][line] == 1 or grille[0][line] ==2):
            print("Cette colonne est pas correcte !")
        elif line >6 or line <0:
            print("Cette ligne n'est pas correcte !")
        elif grille[column][line] == 0 and column == 5:  #(A1 or A2) and A3
            grille[column][line] = player1
        elif (grille[column][line] == 1 or grille[column][line] ==2) and grille[column-1][line] == 0 :
            grille[column-1][line] = player1
        elif (grille[column][line] == 1 or grille[column][line] == 2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2) and  grille[column-2][line] == 0 :
            grille[column-2][line] = player1
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2)  and  (grille[column-2][line] == 1 or grille[column-2][line] == 2)and grille[column-3][line] == 0:
            grille[column-3][line] = player1
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] ==2)  and  (grille[column-2][line] == 1 or grille[column-2][line]==2) and (grille[column-3][line] ==1 or grille[column-3][line]==2) and grille[column-4][line] == 0:
            grille[column-4][line] = player1
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2)  and  (grille[column-2][line] == 1 or grille[column-2][line] == 2) and (grille[column-3][line] ==1 or grille[column-3][line] == 2) and (grille[column-4][line] == 1 or grille[column-4][line] == 2) and grille[column-5][line] == 0:
            grille[column-5][line] = player1
        #~wincondition
        print('Prochain tour !')
        if (grille[column][0] == player1 or grille[column][1] == player1 or grille[column][2] == player1 or grille[column][3] == player1) and grille[column][line+1] == player1 and grille[column][line+2] == player1 and grille[column][line+3] ==  player1:
            print(win1)
            break 
        elif grille[column][line]*grille[column+1][line]*grille[column+2][line]*grille[column+3][line] == 1:
            print(win3)
            break
            #partie verticale ^
        elif grille[column][line]*grille[column+1][line+1]*grille[column+2][line+2]*grille[column+3][line+3] == 1:
            print(win5)
            break
            #partie en diagonale ^
        elif grille[0][0] == grille[0][1] and grille[0][1] == grille[0][2] and grille[0][2] == grille[0][3] and grille[0][3] == grille[0][4] and grille[0][4] == grille[0][5] and grille[0][5]  and grille[0][5] == grille[0][6] and grille[0][6] == 1 or grille[0][6] == 2:
            print(win7)
            break
        Spawntab(grille)
        time.sleep(2)
        column = 5
        line = int(input(" Quelle colonne choisissez vous, joueur 2 ?(Si vous avez déja placé un pion ce tour-si et que ce message apparait, c'est que la colonne choisie est remplie ! "))
        if (grille[0][line] == 1 or grille[0][line] ==2):
            print("Cette colonne est pas correcte !")
        elif line >6 or line <0:
            print("Cette ligne n'est pas correcte !")
        elif grille[column][line] == 0 and column == 5:  #(A1 or A2) and A3
            grille[column][line] = player2
        elif (grille[column][line] == 1 or grille[column][line] ==2) and grille[column-1][line] == 0 :
            grille[column-1][line] = player2
        elif (grille[column][line] == 1 or grille[column][line] == 2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2) and  grille[column-2][line] == 0 :
            grille[column-2][line] = player2
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2)  and  (grille[column-2][line] == 1 or grille[column-2][line] == 2)and grille[column-3][line] == 0:
            grille[column-3][line] = player2
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] ==2)  and  (grille[column-2][line] == 1 or grille[column-2][line]==2) and (grille[column-3][line] ==1 or grille[column-3][line]==2) and grille[column-4][line] == 0:
            grille[column-4][line] = player2
        elif (grille[column][line] == 1 or grille[column][line] ==2) and (grille[column-1][line] == 1 or grille[column-1][line] == 2)  and  (grille[column-2][line] == 1 or grille[column-2][line] == 2) and (grille[column-3][line] ==1 or grille[column-3][line] == 2) and (grille[column-4][line] == 1 or grille[column-4][line] == 2) and grille[column-5][line] == 0:
            grille[column-5][line] = player2
        print('Prochain tour !')
        if grille[column][line] == grille[column][line+1] == grille[column][line+2] == grille[column][line+3] == 2:
            print(win2)
            break
            #partie horizontale ^ 
        elif grille[column][line]*grille[column+1][line]*grille[column+2][line]*grille[column+3][line] == 16: #ou 2?#
            print(win4)
            break
            #partie verticale ^
        elif grille[column][line]*grille[column+1][line+1]*grille[column+2][line+2]*grille[column+3][line+3] == 16:
            print(win6)
            break
            #partie en diagonale ^
        elif grille[0][0] == grille[0][1] and grille[0][1] == grille[0][2] and grille[0][2] == grille[0][3] and grille[0][3] == grille[0][4] and grille[0][4] == grille[0][5] and grille[0][5]  and grille[0][5] == grille[0][6] and grille[0][6] == 1 or grille[0][6] == 2:
            print(win7)
            break
        Spawntab(grille)
    time.sleep(2)
    print("Merci d'avoir utilisé ce puissance 4 v.Python !")
    time.sleep(1)
    print("Et n'oubliez pas de faire ctrl+A et relancer le programme pour refresh !")


#soit 0 1 2 3

#aaaaaaaaah ok ptet c'est car comme c'est des conditions, si ça en trouve une, et bah sa skip les autres