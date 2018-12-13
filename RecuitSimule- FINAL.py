#!/usr/bin/env python
# coding: utf-8

# # TP Metaheuristique d'optimisation pour l'optimisation difficile
# ### Enseignant Dr. P. Siarry
# ##### Compte rendu rédgier par Andric LEO et Jassim EL AKROUCH
# ##### Université Paris-Est-Creteil

# #### Configuration initial du problème des placements de composants

''' importation des librairies'''
import numpy as np                # Permet d'effectuer les calculs mathematiques en 2 dimensions de type array.
import scipy as sc                # Permet d'effectuer les operation scientifique
import matplotlib as plt          # Permet d'effectuer les plots 
import random                     # Permet d'effectuer des operations aléatoire
import math                       # Permet d'effectuer des operation standard mathematique

# Classe comportenant tout les methodes permettant d'atteindre l'objectif
class Composant(object):          # Création de la classe Composant
    def __init__(self, numeroID): # definition de la premiere methode initial (constructeur)
        self.numeroID = numeroID  # On assigne un numero pour chaque composants
        self.listcon=[]           # Creation d'une liste qui contiendra la liste des connections
        self.x=0                  # position initial en x 
        self.y=0                  # position initial en y
        
    def connctionx(self):         # Methode conctionx permettant de voir les composants connecter
        for i in range(0,len(self.listcon)):   # boucle parcourant la longueur de la liste
            print("les composants connecte a:", self.numeroID, "sont:", self.listcon[i].numeroID) # affichage des composants voisins
            print(self.listcon[i].numeroID)

    def permutation(self,compo,mat):  # Méthodes permettant de permuter deux composants de la matrice
        tempx=self.x                  # On a créé une variable temporaire en x qui contiendra les position ordonné en x ([x][y])
        tempy=self.y                  # On a créé une variable temporaire en y qui contiendra les position ordonné en y ([x][y])
        self.x=compo.x                # On deplace maintenant les valeurs qu'on a stocker dans tempx et tempy dans compo.x 
        self.y=compo.y                # On deplace maintenant les valeurs qu'on a stocker dans tempy et tempy dans compo.y 
        compo.x=tempx                 # On deplace maintenant les valeur de tempx dans la compo.x
        compo.y=tempy                 # On deplace maintenant les valeur de tempy dans la compo.y
        mat[self.x][self.y]=self      # permet l'affiche des composant dans la matrice apres permutattions
        mat[compo.x][compo.y]=compo   # permet l'affiche des composant dans la matrice apres permutattions
        print

    def distance(self, composant):    # Méthodes permettant de calculer la distance entre deux composants
        val = 0                       # Initialisation de la valeur = 0 (la distance finale)
        step = 5                      # distance entre deux voisins
        dxy = ((np.abs(self.x-composant.x))+(np.abs(self.y-composant.y))) # valeur absolue de la distance entre deux voisins
        val = step*dxy                # Valeur final de la distance en comprenant le distance entre voisins (le pas)
        #print("la distance entre les deux composants: ", val)
        return val

    ''' distance a partir d'un composant '''
    def distanceComposant(self):      # Méthodes permettant de calculer la distance générer a partir d'un composant
        distTotal=0                   # Initialisation de la distance total = 0
        for i in self.listcon:        # Boucle parcourant la liste de connexion
            distTotal += self.distance(i) # on trouve le distance total d'un composant et ces voisins
        #print("longueur generer par ce comosant:", self.numeroID)
        #print(distTotal)
        return distTotal 
    

def afficher(mat):                   # Méthode permettant l'affichage en 2D.
    for i in range(0,5):
        for j in range(0,5):
            print(mat[i][j].numeroID, end= "\t")
        print("", end= "\n") 
        
def longueurtotal(mat):              # Méthode permettant de trouver la longueur total dans le graph.
    longueurTotal = 0                # Initialisation de la variable longueur total = 0
    for i in range(0,5):             
        for j in range(0,5):
            longueurTotal+= mat[i][j].distanceComposant()  # 
        longueurTotal2 = longueurTotal/2
    print("longueur total du graph: ")
    print(longueurTotal2)
    return longueurTotal2
    
def matAlea(mat):                   # Méthode permettant de trouver la matrice aleatoire
    mat1d = mat.ravel()             # Fonctionnalité permettant de modifier la matrice en 1D pour modifier
    random.shuffle(mat1d)           # Permet de mettre les composant dans le désordre
    desordreComposant =(mat1d.reshape(5,5))   # on remet la matrice en 2D avec la methode .reshape()
    for i in range(0,5):                      # et on affiche la matrice
        for j in range(0,5):
            mat[i][j].x = i
            mat[i][j].y = j 
    mat2=mat
    return mat2
    
def proba(err,t):                  # Méthode permettant de calculer la probabilité
    random3 = random.random()       # On générer une varaible float aléatoire entre 0 et 1 
    if random3<np.exp(-err/t):     # Condition: si la valeur aleatoire est plus petite que l'exponentiel(-err/to) alors
        return True                 # On accepte la transformation
    else:                           # sinon
        return False                # on accepte pas et on continue de permutter.

#Creation de composant
tableau = []
tab =[]

C1 = Composant(1)
C2 = Composant(2)
C3 = Composant(3)
C4 = Composant(4)
C5 = Composant(5)
C6 = Composant(6)
C7 = Composant(7)
C8 = Composant(8)
C9 = Composant(9)
C10 = Composant(10)
C11 = Composant(11)
C12 = Composant(12)
C13 = Composant(13)
C14 = Composant(14)
C15 = Composant(15)
C16 = Composant(16)
C17 = Composant(17)
C18 = Composant(18)
C19 = Composant(19)
C20 = Composant(20)
C21 = Composant(21)
C22 = Composant(22)
C23 = Composant(23)
C24 = Composant(24)
C25 = Composant(25)

# On insère les composant dans le tableau[]
tableau.append(C1)
tableau.append(C2)
tableau.append(C3)
tableau.append(C4)
tableau.append(C5)
tableau.append(C6)
tableau.append(C7)
tableau.append(C8)
tableau.append(C9)
tableau.append(C10)
tableau.append(C11)
tableau.append(C12)
tableau.append(C13)
tableau.append(C14)
tableau.append(C15)
tableau.append(C16)
tableau.append(C17)
tableau.append(C18)
tableau.append(C19)
tableau.append(C20)
tableau.append(C21)
tableau.append(C22)
tableau.append(C23)
tableau.append(C24)
tableau.append(C25)

tab = np.array(tableau)       #creation d'une nouvelle matrice et on met tout dedant '''
mat = np.reshape(tab, (5, 5)) # on demensionne la matrice en 2D '''
#print(mat, end= "\t")

# savoir qui est connnecter à qui
#C6.connctionx();
#C8.connctionx();
#C12.connctionx();
#C22.connctionx();
#C15.connctionx();
#C9.connctionx();

''' les liens du tableau '''
for i in range(0,5):
    for j in range(0,5):
        if i!= 0:
            mat[i][j].listcon.append(mat[i-1][j])
        if j != 0:
            mat[i][j].listcon.append(mat[i][j-1])
        if i != 4:
            mat[i][j].listcon.append(mat[i+1][j])
        if j != 4:
            mat[i][j].listcon.append(mat[i][j+1])
            
for i in range(0,5):
    for j in range(0,5):
        mat[i][j].x = i
        mat[i][j].y = j

# Affiche les composants dans l'ordre
#afficher(mat)
afficher(mat)
longueurtotal(mat)

### TEST du code 
## matrice dans l'ordre

#'''Permutation entre deux composant'''
#C2.permutation(C25,mat)

#'''Distance entre deux composant'''
#C1.distance(C2) # distance entre C1 et C2 = 5
#print("distance entre les composants:")
#C1.distance(C5) # C1 -> C5 (distance = 20)

#''' distance totale a partir d'un composant'''
#C1.distanceComposant()

### Test du code 
## matrice désordonner

mat=matAlea(mat)
longueurtotal(mat)

# Affiche les composants dans le désordre
afficher(mat)


# ## Algorithme du recruit simulé

# ##### 1. temperature initial elevé

tempinit = longueurtotal(mat)


# #### - 2. modification élémentaire
# ##### variation d'energie dE 
# ##### - 2.1 -  100 transformation elementaires pur chaque transfo, on évolue dE
# ##### - 2.2 -  calcule de la moyenne des valeurs absolues de dE -> <|dE|> = absdE
# ##### temperature initial t0, ici on l'appelera tempInit
# ##### tempInit déduit de [e(-absdE/tempInit) = tau0]
# ##### tau0 -> tau initial d'acception des perturbation dégradant. 0 < tau0 < 1
# ##### tau0 dépend de la qualité de la configuration initiale.

# Initialisation de dE
dE = 0
tau0 = 0.88

#fixation de la temperature initial

for i in range(0,100):
    ei = longueurtotal(mat)
    #permutation des composant desordonné avec r1 et r2
    random1 = random.choice(tableau)
    random2 = random.choice(tableau)
    random1.permutation(random2, mat)
    ej = longueurtotal(mat) # nouvelle
    dE += ej - ei
    
dE = np.abs((dE)/100)
t0 = (-dE/np.log(tau0))
print("dE: ", dE, " tau0: ", t0)

### Equilibre thermodynamic

#Initialisation
N = 25
sysfiger =0

while sysfiger < 4:
    Na = 0
    Ne = 0
    Nacc = 0 
    
    while Ne<(100*N) and Na<(12*N):
        ei = longueurtotal(mat)
        #permutation des composant desordonné avec r1 et r2
        random1 = random.choice(tableau)
        random2 = random.choice(tableau)
        random1.permutation(random2, mat)
        ej = longueurtotal(mat) 
        
        dE = ej - ei
        
        # Regle d'acceptation
        if dE <= 0:
            Na+=1
            Ne+=1    
        else:
            if proba(dE, t0):
                Nacc+=1
                Na+=1
                Ne+=1
            else:
                Ne+=1
                random1.permutation(random2, mat)
                
            tau0=(0.9*tau0)
        
    if Nacc==0:
        sysfiger+=1

afficher(mat)
print("longueur totals des connections:", longueurtotal(mat))
afficher(mat) # affiche de la matrice apres l'application de l'algorithme


