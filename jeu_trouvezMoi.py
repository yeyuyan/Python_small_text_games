######NOM:Ye Yuyan ######NOM: Weng Yaohong
#########date:11/12/2015
#######################################################################
import random
from math import*

def TrouvezMoiVersionSimple():
    '''realise une partie du jeu trouvez moi,
    (nb a deviner dans [0,100],nb d'essais illimites'''
    #nbCache:nombre tire au hasard par le programme
    #nbPropose:nombre propose par le joueur
    
    print()
    print("trouvez moi (version simple)")
    print()
    nbCache=random.randint(1,100)
    nbEssaie=1
    print("Essai no ",nbEssaie,": ")
    nbPropose=int(input("Entrez un nb entre 1 et 100:"))
    
    while nbPropose!=nbCache:
        if nbPropose<nbCache:
            print("trop petit")
        else:
            print("trop grand")
        print()
        nbEssaie+=1
        print("Essai no ",nbEssaie,": ")
        nbPropose=int(input("re-entrez un nb entre 1 et 100:"))
    print()
    print("gagne!!!")

    
    
def TrouvezMoiVersionElaboree(debut=0,fin=100):
    '''realise une partie du jeu trouvez moi,
    (nb a deviner dans un intervalle([0,100]par défaut),nb d'essais limites'''
    #nbCache2:nombre tire au hasard par le programme
    #nbPropose2:nombre propose par le joueur
    
    print()
    print("trouvez moi (version élaborée)")
    print()
    debut=int(input("sasir un nombre pour le debut de l'intervalle:"))
    fin=int(input("saisir un autre nombre pour la fin de l'intervalle:"))
    chaine="Devinez un nb entre"+ str(debut)+"et" +str(fin)+":"
    nbPropose2=float(input(chaine))
    
    partiegagne=False
    nbCache2=random.randint(debut,fin)
    
    while nbPropose2<debut or nbPropose2>fin or int(nbPropose2)!=nbPropose2:
        nbPropose2=int(input(chaine))
        
    fois=int(log(fin-debut,2)+1)
    
    for i in range(fois):
        if nbPropose2<nbCache2:
            print("trop petit")
            print()
            nbPropose2=int(input(chaine))
        elif nbPropose2>nbCache2:
            print("trop grand")
            print()
            nbPropose2=int(input(chaine))
        
        print("gagnez!!!!!!!!!!!!!!!")
        partiegagne=True
        
        break
    return  partiegagne
            
    
            
def menu():
    print()
    print("Voici le menu:")
    print()
    print("a:jeu 'trouvez-moi'version 1")
    print("b:jeu 'trouvez-moi'version 2")

    print("q:quitter")
    print()



#######################################################
menu()
foisGagne=0
y=input("Entrez votre choix:")
while y!="q":
    if y=="a":
        TrouvezMoiVersionSimple()
    if y=="b":
        if TrouvezMoiVersionElaboree()==True:
        print("votre score:",foisGagne+1)
        
    menu()
    y=input("Entrez votre choix:")
print("Au revoir")




