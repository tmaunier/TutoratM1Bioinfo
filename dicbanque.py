def ajoutercompte(bank):
  print("Donnez le nom du titulaire du compte")
  nom = raw_input()
  print("Donnez le montant du compte")
  money = input()
  bank[nom] = money #la cle est nom et la valeur associee est money
  return bank

#on affiche un seul compte en banque
def affichercompte(bank,nom):
  print nom , ":" , bank[nom] #nom est la cle et bank[nom] retourne le montant du compte associe a la cle

#on affiche tout les comptes en banque
def afficherbanque(bank):
  for cle in bank.keys(): #on fait une boucle pour parcourir toutes les cles du dictionnaire
    affichercompte(bank,cle) #on reutilise la fonction d'avant pour afficher le compte

#on affiche la moyenne des comptes en banque
def affichermoyenne(bank):
  mean = 0.0
  for cle in bank.keys(): #on parcourt le dictionnaire
    mean += bank[cle] #on ajoute a mean le montant de chaque compte associe a chaque cle
  print "Moyenne :" , mean/len(bank) #on fait la moyenne et on affiche le resultat

#on retire 10% de chaque compte pour les ajouter au notre
def voler(bank):
  for cle in bank.keys(): #on parcourt le dictionnaire
    montant = bank[cle]*0.1 #on calcule les 10%
    bank[cle] -= montant #on retire les 10%
    bank["Moi"] += montant #on s'ajoute les 10%
  print "Votre compte est desormais de" , bank["Moi"] #jackpot sans effort
  return bank

def menu():
  print "---------- MENU ----------"
  print "Saisir 1 pour ajouter un compte"
  print "Saisir 2 pour afficher un compte en banque"
  print "Saisir 3 pour afficher tout les comptes en banque"
  print "Saisir 4 pour afficher la moyenne des comptes en banque"
  print "Saisir 5 pour simuler une banqueroute et preleve 10% sur chaque compte en banque"
  print "Saisir 0 pour sortir"
  nb=input()
  return nb


########## MAIN ##########

bank = {"Moi":0} #declarer le dictionnaire
loop = True
while loop:
  nb=menu()
  print'\n'
  if nb==1:
    ajoutercompte(bank)
    print'\n'	
  elif nb==2:
    print ("Donnez le nom du titulaire")
    nom = raw_input()
    if nom in bank.keys():
      affichercompte(bank,nom)
    else:
      print("Desole nous n'avons pas trouver de compte pour ce titulaire")
    print'\n'
  elif nb==3:
    afficherbanque(bank)
    print'\n'
  elif nb==4:
    affichermoyenne(bank)
    print'\n'
  elif nb==5:
    voler(bank)
  elif nb==0:
    exit()
