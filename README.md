# Projet-AnNum2 : Organisation des fichiers

- 2 Fichiers à destination de l'utilisateur
    * resolution_dim_multiple : pour résoudre une ED de dimension n>1 et la tracer (pourvu qu'elle s'écrive comme un problème de Cauchy et soit lipschitzienne)
    * erreurs_ordre : quantifie les erreurs entre une estimation et une solution de référence

- 2 Fichiers ne contenant que des fonctions
    * schemas_1d : regroupe les schémas de Euler et RK4
    * traces : contient la fonction chargée de tracer des courbes, de les légender etc...

- 1 Fichier de test
    * test_1d : tests de schemas_1d
