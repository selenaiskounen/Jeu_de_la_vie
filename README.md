# Jeu de la vie

L'exemple le plus connu d'un automate cellulaire est le jeu de la vie, mis au point en 1970 par le mathématicien John Horton Conway. Ce jeu est à 0 joueur, il ne necessite donc aucune intervention de la part humaine. Cependant on aimerait observerson évolution et pour cela on va intéragir avec ce jeu en créant une configuration initiale. Le jeu de la vie se modélise de la manière suivante:
        
   1/ Les cellules du jeu ne peuvent prendre qu'un seul état: vivant (1) ou mort (0)
   
   2/ Chaque cellule intéragit avec ses huits cellules voisines.
       
   Dans ce TP, on se propose de définir des fonctions qui nous permetterons de calculer le nombre de callules voisines (nb_cellules_voisines) ainsi qu'une fonction qui permettera de calculer ce nombre à la génération suivante (itération_jeu). Enfin, une fonction qui décrit l'état du jeu après un nombre choisi d'itérations.
       
