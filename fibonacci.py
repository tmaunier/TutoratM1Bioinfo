def creersuite(nb):
  fibo = [0,1]
  for i in range(2,nb+1):
    fibo.append(fibo[i-2]+fibo[i-1])
  return fibo

def afficher(nb,fibo):
  if nb>=len(fibo):
    fibo = ajouter(nb,fibo)
  print "U" , nb , " = " , fibo[nb]

def ajouter(nb,fibo):
  for i in range(len(fibo),nb+1):
    fibo.append(fibo[i-2]+fibo[i-1])
  return fibo


########## MAIN ##########

print ("Quel element de la suite voulez-vous ? [0 pour quitter]")
nb = input()
fibo = creersuite(nb)
while(nb!=0):
  afficher(nb,fibo)
  print ("Quel element de la suite voulez-vous ? [0 pour quitter]")
  nb = input()
