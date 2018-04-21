####DATE: 04/12/2016

#######DEFINITION DES FONFCTIONS#################################################

def motSaisi():
    motSaisi=input("Entrez un mot qui est composé que les lettres d'alphabet:")
    while (not(motSaisi.isalpha())):
        print('False')
        motSaisi=input("Entrez un mot qui est composé que les lettres d'alphabet:")
    return motSaisi


def verifierMot(motInconnu):
    '''la Fonction verifierMot(motInconnu, motSaisi) qui compare le mot caché
motInconnu et le mot saisi par le joueur motSaisi et affiche les symboles « T ,
V, - » si les mots sont différents.
Cette fonction retourne True si les mots sont identiques et False sinon.'''
    mot=motSaisi()
    sortie=""
    if len(motInconnu)==len(mot):
        if motInconnu==mot:
            return True
        else:
            for k in range(len(mot)):
                if motInconnu[k]==mot[k]:
                    sortie=sortie+"T"
                elif mot[k] in motInconnu:
                    sortie+="V"
                else:
                    sortie+="-"
        print(mot)
        print(sortie)
        return False
    else:
        print("Désolé,le mot n'a pas la même longueur.")
        return False

      
def unePartieDeMotus(motInconnu,n):
    '''afin de garantir au joueur n essais pour deviner le mot'''
    for w in range(n):
        print("Essai N°",w+1,"il reste",n-w,"essais")
        chaine="Entrez un mot de "+str(len(motInconnu))+" caractères:"
        if verifierMot(motInconnu):
            print("Vous avez gagné!!!")
            break
        elif w==n-1:
            print("Perdu,le mot Inconnu est:",motInconnu)
        
        
        
        
   



#######PROGRAMME PRINCIPAL########################################"

print("Nous avons besoin d'un mot à deviner.")
motInconnu=motSaisi()
n=int(input("Entrez un nombre d'essai souhaité:"))
unePartieDeMotus(motInconnu,n)






