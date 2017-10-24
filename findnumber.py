import random

guess = random.randint(1,10)
print("Donnez un nombre")
nb=input()
cpt=1
while(nb!=guess):
  if (nb<guess):
    print("Looser, c'est plus")
  else:
    print("Looser, c'est moins")
  print("Donnez un nombre")
  nb=input()
  cpt+=1
print"Bravo, vous avez trouvez en", cpt, "coups"
