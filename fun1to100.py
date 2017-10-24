#On demande a l'utilisateur le nombre de chiffre
def ask():
  print("Jusqu'a combien voulez-vous compter ?\n")
  num=input()
  return num

#on creer la liste avec les nombres
def count(number):
  liste = [] #declarer la liste vide avant de la remplir
  for i in range(number):
    liste.append(i+1)
  return liste

#on affiche les membres de la liste en indiquant s'ils sont pair ou impair
def afficherpairimpair(liste):
  for i in range(len(liste)): #on parcourt la liste
    if liste[i]%2==1 : #on teste l'element de la liste avec modulo 2 qui donne le reste de la division euclidienne par 2
      print liste[i], " est impair"
    else :
      print liste[i], " est pair"


########## MAIN ##########


number = ask()
liste = count(number)
afficherpairimpair(liste)
