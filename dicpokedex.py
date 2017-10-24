#creation des pokemons et ajout dans le dictionnaire
def saisiepokemon(pokedex):
  print("Saisissez le nom de votre pokemon")
  name = raw_input()
  print("Saisissez le type de votre pokemon")
  typ = raw_input()
  print("Saisissez les PV de votre pokemon")
  pv = input()
  pokedex[name] = [typ,pv]
  return pokedex

#affiche un seul pokemon
def afficherpokemon(pokedex,i):
  print i , "de type" , pokedex[i][0] , "avec" , pokedex[i][1] , "PV"

#afficher tout le pokedex
def afficherpokedex(pokedex):
  for i in pokedex.keys(): #utilisation d'une boucle pour parcourir tout le dictionnaire
    afficherpokemon(pokedex,i) #appel de la fonction affichant un pokemon

def affichertype(pokedex):
  print("Saisissez le type que vous souhaitez")
  typ = raw_input()
  for i in pokedex.keys():
    if pokedex[i][0]==typ:
      afficherpokemon(pokedex,i)

#affiche le(s) pokemon(s) avec le plus de PV dans le pokedex
def affichermaxPV(pokedex):
  maxi=0
  for i in pokedex.keys(): #on parcourt le dictionnaire
    if pokedex[i][1]>maxi: #on teste si le PV du pokemon visite est superieur a maxi
      maxi=pokedex[i][1] #on change la valeur maxi si on trouve un pokemon avec plus de PV
  print "Les pokemons avec le plus de PV sont : "
  for i in pokedex.keys(): #on parcourt a nouveau le dictionnaire pour cette fois afficher tout les pokemons ayant le max de PV c'est a dire maxi
    if pokedex[i][1] == maxi:
      afficherpokemon(pokedex,i)

#on fait la moyenne des PV du pokedex
def affichermeanPV(pokedex):
  mean=0
  for i in pokedex.keys():
    mean+=pokedex[i][1]
  mean/=len(pokedex)
  print "La moeynne des PV des pokemons est de" , mean

#ecrire les donnees dans un fichier txt
def write(pokedex):
  print("Donnez un nom de fichier (ne pas oublier l'extension .txt)")
  nom=raw_input()
  fic=open(nom,'w') #on ouvre le fichier en mode ecriture ('w')
  for i in pokedex.keys():
    fic.write(i)
    fic.write('\n')
    fic.write(pokedex[i][0])
    fic.write('\n')
    fic.write(str(pokedex[i][1]))#str est necessaire pour accepter les poids
    fic.write('\n')
  fic.close()

#lire les donnees d un fichier txt
def read(pokedex):
  print ("Quel fichier voulez-vous utiliser?")
  nom_fichier=raw_input()
  fic=open(nom_fichier,'r')
  name=fic.readline()
  while name!='':
    name=name.strip()#elimine le saut de ligne pour passer a la suite
    typ=fic.readline()
    typ=typ.strip()#elimine le saut de ligne pour passer a la suite
    PV=fic.readline()
    PV=PV.strip()#elimine le saut de ligne pour passer a la suite
    PV=int(PV)#les pv sont des chiffres il faut donc le specifier avec int()
    pokedex[name]=[typ,PV]
    name=fic.readline()
  fic.close()
  return pokedex

def menu():
  print "---------- MENU ----------"
  print "Saisir 1 pour ajouter un pokemon"
  print "Saisir 2 pour afficher tout le pokedex"
  print "Saisir 3 pour afficher les pokemons d'un meme type"
  print "Saisir 4 pour afficher les pokemons avec le plus de PV"
  print "Saisir 5 pour afficher la moyenne des PV des pokemons"
  print "Saisir 6 pour sauvegarder votre pokedex"
  print "Saisir 7 pour recuperer un pokedex depuis un fichier txt"
  print "Saisir 0 pour sortir"
  nb=input()
  return nb


########## MAIN ##########

pokedex = {} #declarer le dictionnaire vide pour mieux le remplir

loop = True
while loop:
  nb=menu()
  print'\n'
  if nb==1:
    pokedex = saisiepokemon(pokedex)
    print'\n'	
  elif nb==2:
    afficherpokedex(pokedex)
    print'\n'
  elif nb==3:
    affichertype(pokedex)
    print'\n'
  elif nb==4:
    affichermaxPV(pokedex)
    print'\n'
  elif nb==5:
    affichermeanPV(pokedex)
    print'\n'
  elif nb==6:
    write(pokedex)
    print'\n'
  elif nb==7:
    read(pokedex)
    print'\n'
  elif nb==0:
    exit()
