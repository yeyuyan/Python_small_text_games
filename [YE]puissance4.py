

####NOM PRENOM:YE Yuyan###################################
####DATE:20/05/2016#######################################

####DM2：JEU:PUISSANCE 4!#################################


#########definition des fonctions########################
import random


def quatrePions(ligne,gagne):
    '''test si il y a 4 pions successives de meme type'''
    if 'OOOO' in ligne:
        gagne=True
        print("Bravo!Vous avez gagne!!")
    if 'XXXX' in ligne:
        gagne=True
        print("L'ordinateur a gagne!!Vous avez perdu.")
    return gagne



            
def testGagne(grille):
    '''teste si le jouyeur ou l'ordinateur gagne et retourne True sioui ou False sinon'''
    gagne=False

    ###verifier gagner horizontalement####
    for i in range(6):
        ligne=''.join(grille[i])
        gagne=quatrePions(ligne,gagne)


    ###verifier gagner verticalement###
    for j in range(7):
        l=[grille[k][j] for k in range(6)]
        colonne=''.join(l)
        gagne=quatrePions(colonne,gagne)

    ###verifier gagner diagonalement#####
    
    for somme in range(3,6):
        l2=[grille[n][somme-n] for n in range(6) if somme>=n]
        diag=''.join(l2)
        gagne=quatrePions(diag,gagne)
        
    for somme in range(6,9):
        l3=[grille[l][somme-l] for l in range(6) if l>=somme-6]
        diag1=''.join(l3)
        gagne=quatrePions(diag1,gagne)

    for diff in range(-2,4):
        l4=[grille[m][m+diff] for m in range(6) if m+diff<=6 and m+diff>=0]
        diag2=''.join(l4)
        gagne=quatrePions(diag2,gagne)
    

   
    return gagne



def colPleine(col,grille):
    '''teste si un colonne est plein ou pas'''
    pl=True
    l=[grille[k][col] for k in range(6)]
    if ' ' in l:
        pl=False
    return pl



def grillePleine(grille):
    '''teste si le grille est Pleine.Si oui retournez True.'''
    Pleine=True
    for i in range(6):
        if ' ' in grille[i]:
            Pleine=False
    return Pleine

    

def jeterJeton(col,jeton,grille):
    '''Jeter le jeton dans le grille et retourne le grille a la fin'''
    
    for i in range(6):
        if grille[-i-1][col]==' ':
            grille[-i-1][col]=jeton
            break
    
    return grille



    
def afficheGrille(grille):
    '''affiche le grille'''
    print("joueur:O\nordi:X")
    l=[k for k in range(7)]
    case1="{:4}"
    for k in range(7):
        print(case1.format(l[k]),end='')
    print()
        
    case="|{:3}"
    for i in range(6):
        for j in range(7):
            print(case.format(grille[i][j]),end='')
        print('|')
    print('+','-'*25,'+')
    for k in range(7):
        print(case1.format(l[k]),end='')
    print('\n')
    


###complement2#########
def jouerOrdi(grille):
    col=random.randint(0,6)
    
    ###trois pions alligne en ligne####
    
    for i in range(1,7):
        ligne=''.join(grille[-i])
        
        for u in range(4):
    
            if (ligne[u:u+4]=='OOO ') or (ligne[u:u+4]=='XXX '):
                
                if (grille[-i+1][u+3]!=' ' and i>=2) or (i==1):
                    col=u+3
                    break
            elif (ligne[u:u+4]==' OOO') or (ligne[u:u+4]==' XXX'):
                
                if (grille[-i+1][u]!=' ' and i>=2) or i==1:
                    col=u
                    break
                
                
    ####trois pions alligne en colonne####
    
    for j in range(7):
        l=[grille[k][j] for k in range(6)]
        colonne=''.join(l)
        for m in range(3):

            if (colonne[m:m+4]==' OOO') or(colonne[m:m+4]==' XXX'):
                col=j
                break
            
    ####trois pions alligne en diagonale###
    
    for r in range (3,6):
        for s in range(0,4):
            if (grille[r][s]=='O' and grille[r-1][s+1]=='O'and grille[r-2][s+2]=='O'and grille[r-3][s+3]==' ')or(grille[r][s]=='X' and grille[r-1][s+1]=='X'and grille[r-2][s+2]=='X'and grille[r-3][s+3]==' '):
                if grille[r-2][s+3]!=' ':
                    col=s+3
                    break
            elif (grille[r][s]==' ' and grille[r-1][s+1]=='O' and grille[r-2][s+2]=='O' and grille[r-3][s+3]=='O')or(grille[r][s]==' ' and grille[r-1][s+1]=='X' and grille[r-2][s+2]=='X' and grille[r-3][s+3]=='X'):
                if grille[r-1][s]!=' ':
                    col=s
                    break

    for p in range(-3,0):
        for q in range(-4,0):
            if (grille[p][q]=='O'and grille[p-1][q-1]=='O'and grille[p-2][q-2]=='O' and grille[p-3][q-3]==' ')or(grille[p][q]=='X'and grille[p-1][q-1]=='X'and grille[p-2][q-2]=='X' and grille[p-3][q-3]==' '):
                if (grille[p-2][q-3]!=' ' and p>=-2)or (p==-3):
                    
                    col=q-3
                    break
            elif (grille[p][q]==' 'and grille[p-1][q-1]=='O' and grille[p-2][q-2]=='O' and grille[p-3][q-3]=='O')or(grille[p][q]==' 'and grille[p-1][q-1]=='X' and grille[p-2][q-2]=='X' and grille[p-3][q-3]=='X'):
                if (grille[p+1][q]!=' ' and p<=-2)or(p==-1):
                    
                    col=q
                    break
            
            
            
    return col
    


###fct principale#######
def puissance4():
    ####algo principal###
    '''initialiser la variable grille
       jeton='O'
       quand le grille n'est pas plein:
           si le joueur ou l'ordi n'ont pas gagne:
                si jeton=='O':
                    col=le nb saisie par joueur
                    quand le col est plein:
                        resaisie un nb
                    jeter le jeton dans le col choisi ds le grille
                    afficher le grille
                    jeton='X'
                sinon:(cad jeton=='x')
                    col choisi par l'ordi aleatoirement
                    quand col est plein:
                        rechoisir un col
                    jeter le jeton dans le col
                    afficher le grille
                    jeton='o'
           sinon(le joueur ou l'ordi gagne):
           sortir la fct'''

    ###initialisation la variable grille###
    
    grille=[[' 'for j in range(7)]for i in range(6)]
    '''une liste 2D dont les <<cases>> contiennent les caracteres' ','X','O'
    qui representent respectivement l'espace et 2 types de pions.
    Au debut la liste contient les espaces pour tous les cases'''


    print("PUISSANCE 4!\n\nLe jeu est gagne lorsque 4 jetons de la meme couleur sont aligne en ligue,en colonne ou en diagonale\n\nChacun a son tour met un jeton dans une colonne.\nC'est vous qui commencez!")
    afficheGrille(grille)
    partieGagne=False
    jeton='O'
    while grillePleine(grille)==False:
        if testGagne(grille)==False:
            if jeton=='O':
                col=int(input("Entrez un numero de la colonne,svp:"))
                while colPleine(col,grille): 
                    col=int(input("Entrez un numero de la colonne,svp:"))
                jeterJeton(col,jeton,grille)
                afficheGrille(grille)
                jeton='X'
            
            else:
                col=jouerOrdi(grille)
                while colPleine(col,grille):
                    col=random.randint(0,6)
                print("L'ordinateur va jouer!\nL'ordinateur a joue en colonne",col)
                jeterJeton(col,jeton,grille)
                afficheGrille(grille)
                jeton='O'
        else:
            partieGagne=True
            return partieGagne
    print("match nul,termine!!")
    return partieGange















 
########programme pricipal###################################
nbGagne=0
joueUnPartie='T'
while joueUnPartie=='T':
    if puissance4()==True:
        nbGagne+=1
    joueUnPartie=input('Vous voulez encore jouer une partie? Saisiez T pour une partie nouvelle et F non')
print("Vous avez gagne",nbGagne,"partie(s)")
