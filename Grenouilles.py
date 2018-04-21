def menu():
    print()
    print("Voici le menu:")
    print()
    print("a:jeu 'trouvez-moi'*")
    print("b:jeu 'trouvez-moi' Version 2**")
    print("c:jeu de conjecture tcheque")
    print("d:jeu de decompostion")
    print("e:jeu de chercher premier")
    print("f:le jeu des grenouilles ****")
    print()
    print("q:quitter")



##question 3
def initJeu(lst,nb):
    '''pour creer une liste lst avec nb pions'''
    lst=['x' for i in range(nb)]+['_']+['o' for j in range(nb)]
    return lst


##question 4
def affichage(lst):
    '''afficher la liste obtenue''' 
    print('x->   <-o')
    print()
    for i in range(len(lst)):
        print(lst[i],end=' ')
    print()
    for i in range(len(lst)):
        print(i,end=' ')



##question 5
def estGagne(lst,nb):
    '''C'est une fct booleenne qui retourne vrai si le jeu est gagne,et faux sinon'''
    gagne=False
    lstGagne=['o' for i in range(nb)]+['_']+['x' for j in range(nb)]
    if lst==lstGagne:
        gagne=True
        
    return gagne


##question 8
def estBloque(lst):
    bloque=False
    w=lst.index('_')   
    if (w>1 and w<len(lst)-2 and ''.join(lst[w-2:w+3])=="oo_xx") or (w==1 and ''.join(lst[:4])=="o_xx") or (w==len(lst)-2 and ''.join(lst[len(lst)-4:])=="oo_x") or (w==0 and ''.join(lst[:3])=="_xx") or (w==len(lst)-1 and ''.join(lst[len(lst)-3:])=="oo_"):
        bloque=True    
        
    return bloque



##question 2 et 7
def jeuGrenou(lst,nb):
    '''Efectuer le jeu des grenouilles avec un nombre nb de pions.
    algorithme:
    Creer une liste contenant 2n+1 elements dont les premiers n sont represente par 'x' ,
    les derniers n presente par 'o' et le pion au milieu '-'.
    pour 'x' choisi
    si le premier element a gauche est vide, on echange les deux
    si le dexieme a gauche est vide, on echange les deux
    si non l'element ne deplace pas

    idem pour 'o' deplace avec opposite direction

    les fonctions utilisees:
    initJeu(lst,nb):pour creer une liste lst avec nb pions
    affichage(lst):afficher la liste obtenue
    estGagne(lst,nb):C'est une fct booleenne qui retourne vrai si le jeu est gagne,et faux sinon
    

    les variables
    nb: nombre entiere de pions choix par l'utilisateur 
    lst: une liste qui contient 2nb+1 elements
    pst:la position choisi par l'utilisateur
    w:l'index de'x'.'''
    
    print('~ Jeu des grenouilles~')
    while estGagne(lst,nb)==False and estBloque(lst)==False :
        affichage(lst)
        print()
        pst=int(input("entrez le numero de pion à jouer:"))
        w=lst.index('_')
        if ((pst==w-1 or pst==w-2) and lst[pst]=='x') or ((pst==w+1 or pst==w+2) and lst[pst]=='o'):
            lst[pst],lst[w]=lst[w],lst[pst]
    affichage(lst)
    print()
    if estGagne(lst,nb)==True :
        print('Bravo!')
    elif estBloque(lst)==True:
        print('Perdu,reessaye encore!')
    
#####PROGRAMME PRINCIPALE#############
menu()
choix=input("Entrez votre choix:")
while choix!="q":
    if choix=="g":
        lst=[]
        nb=int(input("Entrez le nb de pions(>=1): "))
        lst=initJeu(lst,nb)
        jeuGrenou(lst,nb)



    menu()
    choix=input("Entrez votre choix:")

    
print("Au revoir")

##
'''lst=[]
nb=int(input("Entrez le nb de pions(>=1): "))
lst=initJeu(lst,nb)
jeuGrenou(nb)'''

