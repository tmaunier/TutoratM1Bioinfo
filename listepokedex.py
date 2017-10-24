#creation des pokemons et ajout dans la liste
def saisiepokemon(pokedex):
  print("Saisissez le nom de votre pokemon")
  name = raw_input()
  print("Saisissez le type de votre pokemon")
  typ = raw_input()
  print("Saisissez les PV de votre pokemon")
  pv = input()
  print("Saisissez le niveau de votre pokemon")
  level = input()
  pokemon = [name,typ,pv,level]
  pokedex.append(pokemon)
  return pokedex

#affiche un seul pokemon
def afficherpokemon(pokedex,i):
  print pokedex[i][0] , "est de type" , pokedex[i][1] , ", a" , pokedex[i][2] , "PV et est au niveau" , pokedex[i][3] #on affiche tout les elements de la sous-liste

#afficher tout le pokedex
def afficherpokedex(pokedex):
  for i in range(len(pokedex)): #utilisation d'une boucle pour parcourir toute la liste
    afficherpokemon(pokedex,i) #appel de la fonction affichant un pokemon
#afficher tout les pokemons d'un meme type
def affichertype(pokedex):
  print("Saisissez le type que vous souhaitez")
  typ = raw_input()
  for i in range(len(pokedex)):
    if pokedex[i][1]==typ:
      afficherpokemon(pokedex,i)

#affiche le(s) pokemon(s) avec le plus de PV dans le pokedex
def affichermaxPV(pokedex):
  maxi=0
  for i in range(len(pokedex)): #on parcourt la liste
    if pokedex[i][2]>maxi: #on teste si le PV du pokemon visite est superieur a maxi
      maxi=pokedex[i][2] #on change la valeur maxi si on trouve un pokemon avec plus de PV
  print "Les pokemons avec le plus de PV sont : "
  for i in range(len(pokedex)): #on parcourt a nouveau la liste pour cette fois afficher tout les pokemons ayant le max de PV c'est a dire maxi
    if pokedex[i][2] == maxi:
      afficherpokemon(pokedex,i)

#on fait la moyenne des PV du pokedex
def affichermeanPV(pokedex):
  mean=0
  for i in range(len(pokedex)):
    mean+=pokedex[i][2]
  mean/=len(pokedex)
  print "La moeynne des PV des pokemons est de" , mean

#on fait monter d'un niveau un pokemon 
def levelup(pokedex):
  print("Quel est le nom du pokemon ?")
  name = raw_input()
  for i in range(len(pokedex)):
    if name == pokedex[i][0]:
      print("Combien de PV a t il gagne ?")
      gain = input()
      pokedex[i][2]+=gain
      pokedex[i][3]+=1
      return
  print("Desole le pokemon n'a pas ete trouve")

def menu():
  print "---------- MENU ----------"
  print "Saisir 1 pour ajouter un pokemon"
  print "Saisir 2 pour afficher tout le pokedex"
  print "Saisir 3 pour afficher les pokemons d'un meme type"
  print "Saisir 4 pour afficher les pokemons avec le plus de PV"
  print "Saisir 5 pour afficher la moyenne des PV des pokemons"
  print "Saisir 6 pour augmenter d'un niveau un de vos pokemon"
  print "Saisir 0 pour sortir"
  nb=input()
  return nb


########## MAIN ##########

pokedex = [] #declarer la liste vide pour mieux la remplir

nb = 1000
while nb!=0:
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
    levelup(pokedex)
    print'\n'
exit()
