# -*- coding: utf-8 -*-
"""
Éditeur de Spyder




def calcul_nb_voisins(Z):
    forme = len(Z) , len(Z[0])
    N= [[0,]*(forme[0]) for i in range(forme[1])]
    for x in range(1,forme[0]-1):
       for y in range(1,forme[1]-1):
           N[x][y]=Z[x-1][y-1] + Z[x][y-1]+ Z[x+1][y-1] + Z[x-1][y] + 0  + Z[x+1][y] + Z[x-1][y+1] + Z[x][y+1] + Z[x+1][y+1]
    return N
    
    
    
def iteration_jeu(Z):
    forme=len(Z),len(Z[0])
    N=calcul_nb_voisins(Z)
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y]==1 and(N[x][y]<2 or N[x][y]>3):
                Z[x][y]=0 #mort de la cellule à la génération suivante par isolement ou par etoufement
            elif Z[x][y]==0 and N[x][y]==3:
                Z[x][y]=1 #naissance de la cellule à la génération suivante
    return Z
    
    

def calcul_nb_voisins_np(Z):
    Z=np.array(Z)
    nb_voisins_np=np.zeros(Z.shape)
    nb_voisins_np[1:-1,1:-1] +=Z[1:-1,:-2] + Z[:-2,:-2]+ Z[:-2,2:] + Z[2:,2:] + Z[2:,:-2] + Z[1:-1,2:] + Z[:-2,1:-1] + Z[2:,1:-1]
    return(nb_voisins_np)
    
    
def iteration_jeu_np(Z):
    forme=len(Z),len(Z[0])
    Z=np.array(Z) # on reprend le même code que précédement avec comme Z une matrice 
    N=calcul_nb_voisins_np(Z) # le nombre de cellule voisines défini précédement pour Z array
    for x in range(1,forme[0]-1):
        for y in range(1,forme[1]-1):
            if Z[x][y]==1 and(N[x][y]<2 or N[x][y]>3):
                Z[x][y]=0 
            elif Z[x][y]==0 and N[x][y]==3:
                Z[x][y]=1 
    return Z
