#on ajoute un compte a la banque
def ajoutercompte(nom,montant):
  print("Donnez le nom du titulaire du compte")
  name = raw_input()
  nom.append(name) #on ajoute le nom du titulaire dans la liste nom
  print("Donnez le montant du compte")
  money = input()
  montant.append(money) #on ajoute le montant du compte a la liste montant
  return nom, montant

#on affiche un seul compte en banque
def affichercompte(nom,montant):
  print "Donnez le nom du titulaire"
  name = raw_input()
  for i in range(len(nom)):
    if nom[i]==name:
      print nom[i] , ":" , montant[i]
      return
  print "Desole nous n'avons pas trouve de compte"
  

#on affiche tout les comptes en banque
def afficherbanque(nom,montant):
  for i in range(len(nom)): #on fait une boucle pour parcourir toute les listes
    print nom[i] , ":" , montant[i]

#on affiche la moyenne des comptes en banque
def affichermoyenne(montant):
  mean = 0.0
  for i in range(len(montant)): #on parcourt les listes
    mean += montant[i] #on ajoute a mean le montant de chaque compte
  print "Moyenne :" , mean/len(montant) #on fait la moyenne et on affiche le resultat

#on retire 10% de chaque compte pour les ajouter au notre
def voler(montant):
  for i in range(len(montant)): #on parcourt le dictionnaire
    money = montant[i]*0.1 #on calcule les 10%
    montant[i] -= money #on retire les 10%
    montant[0] += money #on s'ajoute les 10%
  print "Votre compte est desormais de" , montant[0] , "\n" #jackpot sans effort

def menu():
  print "---------- MENU ----------"
  print "Saisir 1 pour ajouter un compte"
  print "Saisir 2 pour afficher un compte en banque"
  print "Saisir 3 pour afficher tous les comptes en banque"
  print "Saisir 4 pour afficher la moyenne des comptes en banque"
  print "Saisir 5 pour simuler une banqueroute et preleve 10% sur chaque compte en banque"
  print "Saisir 0 pour sortir"
  nb=input()
  return nb


########## MAIN ##########

nom = ["Moi"]
montant = [0]
loop = True
while loop:
  nb=menu()
  print'\n'
  if nb==1:
    ajoutercompte(nom,montant)
    print'\n'	
  elif nb==2:
    affichercompte(nom,montant)
    print'\n'
  elif nb==3:
    afficherbanque(nom,montant)
    print'\n'
  elif nb==4:
    affichermoyenne(montant)
    print'\n'
  elif nb==5:
    voler(montant)
  elif nb==0:
    exit()
