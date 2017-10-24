import os
import random

def damier(case):
  print ('\n')
  print '	o-------------------o-------------------o-------------------o-------------------o-------------------o-------------------o-------------------o'
  print '	|        10         |        11         |        12         |        13         |        14         |        15         |        16         |'
  print '	|',case[10][0],'|',case[11][0],'|',case[12][0],'|',case[13][0],'|',case[14][0],'|',case[15][0],'|',case[16][0],'|'
  print '	|',case[10][1],'|',case[11][1],'|',case[12][1],'|',case[13][1],'|',case[14][1],'|',case[15][1],'|',case[16][1],'|'
  print '	|',case[10][2],'|',case[11][2],'|',case[12][2],'|',case[13][2],'|',case[14][2],'|',case[15][2],'|',case[16][2],'|'
  print '	|',case[10][3],'|',case[11][3],'|',case[12][3],'|',case[13][3],'|',case[14][3],'|',case[15][3],'|',case[16][3],'|'
  print '	|',case[10][4],'|',case[11][4],'|',case[12][4],'|',case[13][4],'|',case[14][4],'|',case[15][4],'|',case[16][4],'|'
  print '	|',case[10][5],'|',case[11][5],'|',case[12][5],'|',case[13][5],'|',case[14][5],'|',case[15][5],'|',case[16][5],'|'
  print '	|',case[10][6],'|',case[11][6],'|',case[12][6],'|',case[13][6],'|',case[14][6],'|',case[15][6],'|',case[16][6],'|'
  print '	|',case[10][7],'|',case[11][7],'|',case[12][7],'|',case[13][7],'|',case[14][7],'|',case[15][7],'|',case[16][7],'|'
  print '	o-------------------o###################o###################o###################o###################o###################o-------------------o'
  print '	|         9         #        26         |        27         |        28         |        29         |        30         #        17         |'
  print '	|',case[9][0],'#',case[26][0],'|',case[27][0],'|',case[28][0],'|',case[29][0],'|                   #',case[17][0],'|'
  print '	|',case[9][1],'#',case[26][1],'|',case[27][1],'|',case[28][1],'|',case[29][1],'|',case[30][0],'#',case[17][1],'|'
  print '	|',case[9][2],'#',case[26][2],'|',case[27][2],'|',case[28][2],'|',case[29][2],'|',case[30][1],'#',case[17][2],'|'
  print '	|',case[9][3],'#',case[26][3],'|',case[27][3],'|',case[28][3],'|',case[29][3],'|',case[30][2],'#',case[17][3],'|'
  print '	|',case[9][4],'#',case[26][4],'|',case[27][4],'|',case[28][4],'|',case[29][4],'|',case[30][3],'#',case[17][4],'|'
  print '	|',case[9][5],'#',case[26][5],'|',case[27][5],'|',case[28][5],'|',case[29][5],'|                   #',case[17][5],'|'
  print '	|',case[9][6],'#',case[26][6],'|',case[27][6],'|',case[28][6],'|',case[29][6],'|         B         #',case[17][6],'|'
  print '	|',case[9][7],'#',case[26][7],'|',case[27][7],'|',case[28][7],'|',case[29][7],'|         R         #',case[17][7],'|'
  print '	o-------------------o-------------------o###################o###################o###################o         A         o-------------------o'
  print '	|         8         #        25         #                                                           |         V         #        18         |'
  print '	|',case[8][0],'#',case[25][0],'#                                                           |         O         #',case[18][0],'|'
  print '	|',case[8][1],'#',case[25][1],'#                                                           |                   #',case[18][1],'|'
  print '	|',case[8][2],'#',case[25][2],'#                  Si tu es encore en vie                   |',case[30][4],'#',case[18][2],'|'
  print '	|',case[8][3],'#',case[25][3],'#                                                           |',case[30][5],'#',case[18][3],'|'
  print '	|',case[8][4],'#',case[25][4],'#                 Retournes a la case START                 |',case[30][6],'#',case[18][4],'|'
  print '	|',case[8][5],'#',case[25][5],'#                                                           |',case[30][7],'#',case[18][5],'|'
  print '	|',case[8][6],'#',case[25][6],'#                                                           |                   #',case[18][6],'|'
  print '	|',case[8][7],'#',case[25][7],'#                                                           |                   #',case[18][7],'|'
  print '	o-------------------o-------------------o###################o###################o###################o###################o-------------------o'
  print '	|         7         #        24         |        23         |        22         |        21         |        20         |        19         |'
  print '	|',case[7][0],'#',case[24][0],'|',case[23][0],'|',case[22][0],'|',case[21][0],'|',case[20][0],'|',case[19][0],'|'
  print '	|',case[7][1],'#',case[24][1],'|',case[23][1],'|',case[22][1],'|',case[21][1],'|',case[20][1],'|',case[19][1],'|'
  print '	|',case[7][2],'#',case[24][2],'|',case[23][2],'|',case[21][2],'|',case[21][2],'|',case[20][2],'|',case[19][2],'|'
  print '	|',case[7][3],'#',case[24][3],'|',case[23][3],'|',case[21][3],'|',case[21][3],'|',case[20][3],'|',case[19][3],'|'
  print '	|',case[7][4],'#',case[24][4],'|',case[23][4],'|',case[21][4],'|',case[21][4],'|',case[20][4],'|',case[19][4],'|'
  print '	|',case[7][5],'#',case[24][5],'|',case[23][5],'|',case[21][5],'|',case[21][5],'|',case[20][5],'|',case[19][5],'|'
  print '	|',case[7][6],'#',case[24][6],'|',case[23][6],'|',case[21][6],'|',case[21][6],'|',case[20][6],'|',case[19][6],'|'
  print '	|',case[7][7],'#',case[24][7],'|',case[23][7],'|',case[21][7],'|',case[21][7],'|',case[20][7],'|',case[19][7],'|'
  print '	o-------------------o###################o###################o###################o###################o###################o-------------------o'
  print '	|         6         |         5         |         4         |         3         |         2         |         1         |       START       |'
  print '	|',case[6][0],'|',case[5][0],'|',case[4][0],'|',case[3][0],'|',case[2][0],'|',case[1][0],'|',case[0][0],'|'
  print '	|',case[6][1],'|',case[5][1],'|',case[4][1],'|',case[3][1],'|',case[2][1],'|',case[1][1],'|',case[0][1],'|'
  print '	|',case[6][2],'|',case[5][2],'|',case[4][2],'|',case[3][2],'|',case[2][2],'|',case[1][2],'|',case[0][2],'|'
  print '	|',case[6][3],'|',case[5][3],'|',case[4][3],'|',case[3][3],'|',case[2][3],'|',case[1][3],'|',case[0][3],'|'
  print '	|',case[6][4],'|',case[5][4],'|',case[4][4],'|',case[3][4],'|',case[2][4],'|',case[1][4],'|',case[0][4],'|'
  print '	|',case[6][5],'|',case[5][5],'|',case[4][5],'|',case[3][5],'|',case[2][5],'|',case[1][5],'|',case[0][5],'|'
  print '	|',case[6][6],'|',case[5][6],'|',case[4][6],'|',case[3][6],'|',case[2][6],'|',case[1][6],'|',case[0][6],'|'
  print '	|',case[6][7],'|',case[5][7],'|',case[4][7],'|',case[3][7],'|',case[2][7],'|',case[1][7],'|',case[0][7],'|'
  print '	o-------------------o-------------------o-------------------o-------------------o-------------------o-------------------o-------------------o'
  print ('\n')

def createplayers():
  players = []
  print ('Combien de participant(e)s dans cette partie ? (Max 8)')
  nbplayers = input()
  while (nbplayers>8 or nbplayers <= 0):
    print ('Reponse invalide, veuillez reessayer')
    print ('Combien de participant(e)s dans cette partie ? (Max 8)')
    nbplayers = input()
  for i in range(nbplayers):
    print 'Donnez le nom du joueur' , i+1
    nom = raw_input()
    while (len(nom)>17):
      print ('Les noms de plus de 17 caracteres ne sont pas autorises')
      print 'Donnez le nom du joueur' , i+1
      nom = raw_input()
    for j in range(len(nom),17):
      nom += " "
    temp = [nom,0]
    players.append(temp)
  for i in range(nbplayers,8):
    temp = ["                 ",0]
    players.append(temp)
  return players

def createcase():
  case = []
  for i in range(32):
    case.append([])
    for j in range(8):
      case[i].append("                 ")
  return case

def modifiercase(players):
  case = createcase()
  for i in range (len(players)):
    num = int(players[i][1])
    nom = players[i][0]
    case[num][i] = nom
  return case

def lancede():
  de = random.randint(1,6)
  return de

def transformnom(nom):
  chaine = nom.replace(" ","")
  return chaine

def avance(caseplayer,de):
  caseplayer += de
  if caseplayer > 30 :
    caseplayer = 30 - (caseplayer-30)
  return caseplayer

def rules(players, tour):
  print regles[players[tour][1]]
  if players[tour][1] == 0:
    print "BOIS"
  elif players[tour][1] == 1:
    print "Tout le monde boit"
  elif players[tour][1] == 2:
    print "Designe quelqu'un qui doit boire"
  elif players[tour][1] == 3:
    print "Tu as de la chance, bois 1 fois"
  elif players[tour][1] == 4:
    print "La personne a ta gauche boit"
  elif players[tour][1] == 5:
    print "Designe deux joueurs qui doivent boire"
  elif players[tour][1] == 6:
    print "Tout le monde boit sauf toi"
  elif players[tour][1] == 7:
    print "Bois autant de fois que tu as d'oreilles"
  elif players[tour][1] == 8:
    print "Ne fais rien"
  elif players[tour][1] == 9:
    print "Bois et recules de 7 cases"
    players[tour][1] -= 7
  elif players[tour][1] == 10:
    print "Celui ou celle qui a propose de jouer boit 3 fois"
  elif players[tour][1] == 11:
    print "Les filles boivent"
  elif players[tour][1] == 12:
    print "Tout le monde recule d'une case et fait ce qui y est dit"
    for i in range(len(players)):
      if (players[i][0] == "                 "):
        break
      while (players[i][1] == 31 and i < 8):
        i += 1
      players[i][1] -= 1
      if players[i][1] < 0:
        players[i][1] = 0
      players = rules(players,i)
  elif players[tour][1] == 13:
    print "Les joueurs sans permis de conduire boivent"
  elif players[tour][1] == 14:
    print "Bois 3 fois (saisir 1) ou retourne case 8 (saisir 2)"
    rep = input()
    while (rep < 1 or rep > 2):
      print "Erreur de saisie veuillez recommencer (1 ou 2)"
      rep = input()
    if rep == 2:
      players[tour][1] = 8
  elif players[tour][1] == 15:
    de = lancede()
    print "Bois",de,"fois"
  elif players[tour][1] == 16:
    print "Designe 3 joueurs qui doivent boire"
  elif players[tour][1] == 17:
    print "Les joueurs en avance sur toi boivent"
  elif players[tour][1] == 18:
    print "Les mecs boivent"
  elif players[tour][1] == 19:
    print "Tout le monde se vouvoie, celui qui oublie boit"
  elif players[tour][1] == 20:
    print "Designe quelqu'un qui boit 3 fois"
  elif players[tour][1] == 21:
    print "Recules de 10 cases"
    players[tour][1] -= 10
  elif players[tour][1] == 22:
    print "Tout le monde lance le de, ceux qui font 6 retournent a la case depart"
    for i in range(len(players)):
      if (players[i][1] == "                 "):
        break
      while (players[i][1] == 31 and i < 8):
        i += 1
      de = lancede()
      print de
      if de == 6:
        print transformnom(players[i][0]),"retourne a la case depart"
        players[i][1] = 0
  elif players[tour][1] == 23:
    print "Le(s) plus proche de la fin boi(ven)t"
  elif players[tour][1] == 24:
    de = lancede()
    if de < 4:
      print "BOIS"
    else:
      print "Tout le monde boit sauf toi"
  elif players[tour][1] == 25:
    de = lancede()
    print "Bois et recules de",de,"cases"
    players[tour][1] -= de
  elif players[tour][1] == 26:
    print "Racontes une blague, ceux qui rient boivent 2 fois, si personne rit bois 4 fois"
  elif players[tour][1] == 27:
    print "Bois, relances le de qui vaudra double cette fois et fais ce qui y est dit"
    de = lancede()*2
    print de
    players[tour][1] = avance(players[tour][1],de)
    players = rules(players,tour)
  elif players[tour][1] == 28:
    print "Trinques avec celui ou celle qui a propose de jouer"
  elif players[tour][1] == 29:
    print "Bois et recules de 8 cases"
    players[tour][1] -= 8
  elif players[tour][1] == 30:
    print "Bravo tu as gagne\nSaisis 1 si tu veux continuer\nSaisis 2 si tu veux arreter et vider ton verre"
    rep = input()
    while (rep < 1 or rep > 2):
      print "Erreur de saisie veuillez recommencer (1 ou 2)"
      rep = input()
    if rep == 1:
      print "Bravo, tu es courageux.... ou juste inconscient"
      players[tour][1] = 0
    else:
      players[tour][1] = 31
  return players

########## MAIN ##########


regles = ["regle START","regle 1","regle 2","regle 3","regle 4","regle 5","regle 6","regle 7","regle 8","regle 9","regle 10","regle 11","regle 12","regle 13","regle 14","regle 15","regle 16","regle 17","regle 18","regle 19","regle 20","regle 21","regle 22","regle 23","regle 24","regle 25","regle 26","regle 27","regle 28","regle 29","regle 30"]
players = createplayers()
case = createcase()
case = modifiercase(players)
damier(case)
print "Bienvenue dans ce jeu de l'oie un peu particulier, mais fort sympathique.\nPour commencer gentiment... TOUT LE MONDE BOIS"
tour = 0
while(True):
  if tour == 8 or players[tour][0] == "                 ":
    tour = 0
  while (players[tour][1] == 31 and tour < 8):
    tour += 1
    if tour == 8:
      tour = 0
      break
  joueur = transformnom(players[tour][0])
  print joueur , "doit lancer le de (saisissez n'importe quel touche puis entree)"
  temp = raw_input()
  os.system("clear")
  de = lancede()
  print de
  players[tour][1] = avance(players[tour][1],de)
  players = rules(players, tour)
  case = modifiercase(players)
  damier(case)
  tour += 1
