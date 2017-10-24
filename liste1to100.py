#On demande a l'utilisateur de saisir la valeur de number
print("Jusqu'a combien voulez-vous compter ?\n")
number=input()

#On declare la liste vide
liste = []
#On fait tourner la boucle for
for i in range(number):
  liste.append(i+1)

for i in range(len(liste)):
  print liste[i]
