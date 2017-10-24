#On demande a l'utilisateur de saisir la valeur de number
print("Jusqu'a combien voulez-vous compter ?\n")
number=input()

#On fait tourner la boucle for
for i in range(number):
  print i+1

#Pour une boucle while il est necessaire de declarer un compteur en amont et de ne pas oublier de l'incrementer a chaque fin d'iteration de boucle avec j+=1
j=0
while(j<number):
  print (j+1)
  j+=1
