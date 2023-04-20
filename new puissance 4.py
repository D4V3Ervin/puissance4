import time



def spawntab():
    a = [0, 0, 0, 0 ,0 , 0, 0]
    b = [0, 0, 0, 0 ,0 , 0, 0]
    c = [0, 0, 0, 0 ,0 , 0, 0]
    d = [0, 0, 0, 0 ,0 , 0, 0]
    e = [0, 0, 0, 0 ,0 , 0, 0]
    f = [0, 0, 0, 0 ,0 , 0, 0]
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)



#ligne 
a = [0, 0, 0, 0 ,0 , 0, 0]
b = [0, 0, 0, 0 ,0 , 0, 0]
c = [0, 0, 0, 0 ,0 , 0, 0]
d = [0, 0, 0, 0 ,0 , 0, 0]
e = [0, 0, 0, 0 ,0 , 0, 0]
f = [0, 0, 0, 0 ,0 , 0, 0]

#colonne
A = a[0] and b[0] and c[0] and d[0] and e[0] and f[0] 
B = a[1] and b[1] and c[1] and d[1] and e[1] and f[1]
C = a[2] and b[2] and c[2] and d[2] and e[2] and f[2]
D = a[3] and b[3] and c[3] and d[3] and e[3] and f[3]
E = a[4] and b[4] and c[4] and d[4] and e[4] and f[4]
F = a[5] and b[5] and c[5] and d[5] and e[5] and f[5]
G = a[6] and b[6] and c[6] and d[6] and e[6] and f[6]
# Faire comme dans excel
def test():
    a = [0, 0, 0, 0 ,0 , 0, 0]
    b = [0, 0, 0, 0 ,0 , 0, 0]
    c = [0, 0, 0, 0 ,0 , 0, 0]
    d = [0, 0, 0, 0 ,0 , 0, 0]
    e = [0, 0, 0, 0 ,0 , 0, 0]
    f = [0, 0, 0, 0 ,0 , 0, 0]
    A = a[0], b[0], c[0], d[0], e[0], f[0] 
    B = a[1], b[1], c[1], d[1], e[1], f[1]
    C = a[2], b[2], c[2], d[2], e[2], f[2]
    D = a[3], b[3], c[3], d[3], e[3], f[3]
    E = a[4], b[4], c[4], d[4], e[4], f[4]
    F = a[5], b[5], c[5], d[5], e[5], f[5]
    G = a[6], b[6], c[6], d[6], e[6], f[6]
    return A
def partie():
    
    print('Bienvenue dans cette partie de puissance 4 version python, mes chers joueurs 1 et 2 !')
    time.sleep(3)
    print('Le propriétaire de ce pc sera le joueur 1, et son jeton sera défini comme un "1"!')
    time.sleep(1)
    print('Le second joueur, lui, aura droit à un magnifique "2" !! ')
    time.sleep(1)
    a = str(input('Compris ?(Répondez Oui/Non)'))
    if a == "Oui" or "oui":
        print('Bien, alors commençons !')
    elif a == "Non" or "Nan" or "non" or "nan":
        print('Eh bien, tant pis pour vous, on commence !')
    elif a == "Quel est le sens de la vie ?":
        print("Je suis pas prof moi, Google existe !")
    time.sleep(4)
    print('Commençons sans plus tarder ! Joueur 1, par quelle colonne allez vous commencer ?')
    spawntab()
    line = int(input('joueur 1'))
    col= 5




    
