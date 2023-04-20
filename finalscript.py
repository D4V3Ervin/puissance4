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
#jusque la, aucune erreur
    def win_conditions():
        if grille[column][line] == grille[column][line+1] == grille[column][line+2] == grille[column][line+3] == 1:
            return win1
        elif grille[column][line] == grille[column][line+1] == grille[column][line+2] == grille[column][line+3] == 2:
            return win2
            #partie horizontale ^
        elif grille[column][line] == grille[column+1][line] == grille[column+2][line] == grille[column+3][line] == 1:
            return win3
        elif grille[column][line] == grille[column+1][line] == grille[column+2][line] == grille[column+3][line] == 2:
            return win4
            #partie verticale ^
        elif grille[column][line] == grille[column+1][line+1] == grille[column+2][line+2] == grille[column+3][line+3] == 1:
            return win5
        elif grille[column][line] == grille[column+1][line+1] == grille[column+2][line+2] == grille[column+3][line+3] == 2:
            return win6
            #partie en diagonale ^
        elif grille[0][0] == grille[0][1] == grille[0][2] == grille[0][3] == grille[0][4] == grille[0][5] == grille[0][6] == 1 or 2:
            return win7
        else:
            return "Prochain tour !"
        
    while column >= 0 and column >= 5 and win_conditions() != win1 or win2 or win3 or win4 or win5 or win6 or win7:
        time.sleep(2)
        line = int(input(" Joueur 1, sélectionnez votre colonne !(Si vous avez déja placé un pion ce tour-si et que ce message apparait, c'est que la colonne choisie est remplie ! "))
        if line >6 or line <0:
            print("Cette ligne n'est pas correcte !")
        elif grille[column][line] == 0 and column == 5:
            grille[column][line] = player1
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 0 :
            grille[column-1][line] = player1
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 1  and  grille[column-2][line] == 0 :
            grille[column-2][line] = player1
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] == 0:
            grille[column-3][line] = player1
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] ==1 and grille[column-4][line] == 0:
            grille[column-4][line] = player1
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] ==1 and grille[column-4][line] == 1 and grille[column-5][line] == 0:
            grille[column-5][line] = player1
        win_conditions()
        time.sleep(2)
        line = int(input(" Quelle colonne choisissez vous, joueur 2 ?(Si vous avez déja placé un pion ce tour-si et que ce message apparait, c'est que la colonne choisie est remplie ! "))
        if line >6 or line <0:
            print("Cette ligne n'est pas correcte !")
        elif grille[column][line] == 0 and column == 5:
            grille[column][line] = player2
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 0 :
            grille[column-1][line] = player2
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 1  and  grille[column-2][line] == 0 :
            grille[column-2][line] = player2
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] == 0:
            grille[column-3][line] = player2
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] ==1 and grille[column-4][line] == 0:
            grille[column-4][line] = player2
        elif grille[column][line] == (1 or 2) and grille[column-1][line] == 1  and  grille[column-2][line] == 1 and grille[column-3][line] ==1 and grille[column-4][line] == 1 and grille[column-5][line] == 0:
            grille[column-5][line] = player2
        win_conditions()
    time.sleep(2)
    print("Merci d'avoir utilisé ce puissance 4 v.Python !")
    time.sleep(1)
    print("Et n'oubliez pas de faire ctrl+A et relancer le programme pour refresh !")
    #adapter la boucle avec les 1 et les 2, et bien mettre des trucs comme au dessus si la ligne est au dessus de 6 ou en dessous de 0!
    #et revoir les win_condition, adapter le tour du player 2 dans la boucle puis réfléchir à comment finir le programme
    
    
    



#mettre les conditions de win au début ?
#win condition == s'inspirer du code de mon IA, 
#à la fin du programme, faudra reset le tableau avec grille = [[0 for x in range(6)] for y in range(7)]

  # Faire comme dans excel : que le si la case c'est un zéro, elle devient un 1, et si celle dans dessous est un 0, la première case devient
    #un zéro et celle d'en dessous un 1, et ainsi de suite (boucle)
#drop_piece_player1(column)
    # Faire comme dans excel : que le si la case c'est un zéro, elle devient un 1, et si celle dans dessous est un 0, la première case devient
    #un zéro et celle d'en dessous un 1, et ainsi de suite (boucle)

    #vérifier ligne et colonne et REGARDER COURS TABLEAU si j'ai pas fait de connerie
    #fAIRE TEST AVEC AUTRE TAB
    #déja un truc pas mal mais il manque un truc (fonction column_determine)
    #faut définir l'histoire avec la colonne qui se met automatiquement au plus bas possible (la première ligne qui a une case libre)