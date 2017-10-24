#On demande a l'utilisateur le nombre de chiffre
def ask():
  print("Jusqu'a combien voulez-vous compter ?\n")
  num=input()
  return num

#on creer le dictionnaire avec les nombres
def count(number):
  dico = {} #declarer le dictionnaire vide avant de le remplir
  for i in range(1,number+1,+1):
    if i%2==1:
      dico[i] = "est impair"
    else:
      dico[i] = "est pair"
  return dico

#on affiche les membres du dictionnaire en indiquant s'ils sont pair ou impair
def afficherpairimpair(dico):
  for alcool in dico.keys(): #on parcourt le dictionnaire en utilisant les cles ici alcool est la cle
    print alcool , dico[alcool]


########## MAIN ##########


number = ask()
dico = count(number)
afficherpairimpair(dico)
