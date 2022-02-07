# auteur : erwan.simon@inserm.fr
#date de premiere modification : 7.02.2022

#!/usr/bin/env python3

import math

def fibo(n):
    #le nombre d'or 1.618033 est solution de l'équation F(X)=(X-1)(X+1)-X = X*X -X - 1 = 0
    # 0 1 2 3 5 8 13 21 (suite de Fibonacci où n(k) = n(k-1) + n(k-2), avec 1 < k < n)
    
    compteur = 1
    a = 1
    b = 2
    tmp = 0
    while compteur < n :
        tmp = b
        b = a + b
        a = tmp

        compteur = compteur + 1

    return(b/a) 
  
  # la fonction math.pow utilise le second argument comme exposant, le premier argument étant l'indice)
   pow(fibo(100),2) - fibo(100) - 1
    gold = fibo(100) # le nombre d'or (n/ref: liber abaci de Léonard de Pise)
