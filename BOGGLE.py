##########TP1 BOGGLE
##########WENG YAOHONG/YE YUYAN
##########06/12/2016

##########Définition des fcts###################################################

####etape 1#######
def intiLettres():
    '''retourne une liste de 16 listes contenant chacune les six lettres d'un dé'''
    les16des=[
    ['E', 'T', 'U', 'K', 'N', 'O'],
    ['E', 'V', 'G', 'T', 'I', 'N'],
    ['D', 'E', 'C', 'A', 'M', 'P'],
    ['I', 'E', 'L', 'R', 'U', 'W'],
    ['E', 'H', 'I', 'F', 'S', 'E'],
    ['R', 'E', 'C', 'A', 'L', 'S'],
    ['E', 'N', 'T', 'D', 'O', 'S'],
    ['O', 'F', 'X', 'R', 'I', 'A'],
    ['N', 'A', 'V', 'E', 'D', 'Z'],
    ['E', 'I', 'O', 'A', 'T', 'A'],
    ['G', 'L', 'E', 'N', 'Y', 'U'],
    ['B', 'M', 'A', 'Q', 'J', 'O'],
    ['T', 'L', 'I', 'B', 'R', 'A'],
    ['S', 'P', 'U', 'L', 'T', 'E'],
    ['A', 'I', 'M', 'S', 'O', 'R'],
    ['E', 'N', 'H', 'R', 'I', 'S']]
    return les16des

import random

def nouvelleGrille(les16des):
    '''retourne une liste de 4 listes contenant chacune 4 lettres'''

    #####Les buts de créer ces variables:
    grille=[]
    '''grille: une liste de taille 4 x 4 contenant 16 lettres  tirés et placés bien par hasard'''
    grilleI=[]
    '''grilleI: une liste intermédiaire'''
    l=[]
    '''l: une liste cotient 16 entiers différents qui sont tirés par hasard'''
    
    for t in les16des:
        k=random.randint(0,5)
        grilleI.append(t[k])
        
    while len(l)<16:
        e=random.randint(0,15)
        while e in l:
            e=random.randint(0,15)
        l.append(e)
        
    for i in range(4):
        ligne=[]
        for j in range(4):
            ligne.append(grilleI[l[4*i+j]])
        grille.append(ligne)
    return grille

def afficherJeu(grille):
    '''affiche la grille du jeu :4 x4 lettres et les N° de lignes et colonnes.'''
    case="{:2}"
    print()
    print("GRILLE DU JEU")
    print("  ","1","2","3","4")
    for i in range(4):
        print(i+1,end="  ")
        for j in range(4):
            print(case.format(grille[i][j]),end="")
        print()


###etape 2#####
        
import copy
def vérification1(grille,mot):
    grilleTempo=copy.deepcopy(grille)
    ver=True
    #####creer une liste grilleS contenant 16 lettres de grilleTempo###
    grilleS=[]
    for k in range(4):
        grilleS.extend(grilleTempo[k])
    ###verifier le nb d'occurences des lettres####    
    for h in mot:
        if grilleS.count(h)<mot.count(h):
           print("Non,toutes les lettres n'y sont pas")
           ver=False
           break
    ####les lettres n’appartenant pas au mot sont remplacée par '_'#### 
    if ver==True:   
        for i in range(4):
            for j in range(4):
               if grilleTempo[i][j] not in mot:
                   grilleTempo[i][j]='_'
    afficherJeu(grilleTempo)               
    return grilleTempo


###etape3####

import time

def JouerUnePartieBoggle():
    les16des=intiLettres()
    grille=nouvelleGrille(les16des)
    afficherJeu(grille)
    t=0
    score=0
    print("Vous avez 30s.")
    while t<=30:
        now=time.time()
        mot=input("Proposez un mot(en majuscules):")
        et=time.time()
        t+=(et-now)
        grilleTempo=vérification1(grille,mot)
        if grille!=grilleTempo:
            score+=1

    if t>30:
        print("Time's up! Dans cette partie tu gagnes ",score,"points.")
        return score
    else:
        print("Cette fois-ci tu gagnes totallement",score,"points.")
        return score





##########Programme principale##################################################
print("Boggle","version 0.1")
orde=input("start=S,quit=Q:")

if orde=="S":
    scoreT=JouerUnePartieBoggle()
    nbPartie=1
    rejouer=input("Voulez-vous rejouer une partie?(Tapez 'T' pour rejouer,'F'pour quitter)")
    while rejouer=='T':
        scoreT+=JouerUnePartieDeBoggle()
        nbPartie+=1
        print("Après ",nbPartie," vous avez gagné",scoreT,"score(s).")
        rejouer=input("Voulez-vous rejouer une partie?(Tapez 'T' pour rejouer,'F'pour quitter)")
    
elif orde=="Q":            
    print("Goodbye!")
else:
    print("I don't understand...")
