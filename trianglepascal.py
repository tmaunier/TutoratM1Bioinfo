def creer(nb):
  triangle = [[1]]
  for i in range(1 , nb+1 , +1):
    liste = [1]
    for j in range(1 , i , +1):
      liste.append(triangle[i-1][j-1]+triangle[i-1][j])
    liste.append(1)
    triangle.append(liste)
  return triangle

def afficher(triangle):
  for i in range(len(triangle)):
    print triangle[i]

########## MAIN ##########

print ("Quel profondeur pour votre triangle de pascal ?")
nb = input()
triangle = creer(nb)
afficher(triangle)
