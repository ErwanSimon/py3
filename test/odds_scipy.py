#!/usr/bin/env python3
# coding: utf-8
import math

import numpy as np

import scipy
import scipy.stats as stats

# (lecture du fichier CSV)


# INTERVALLES DE CONFIANCE
# calcul simple d'un intervalle de confiance à 95%


moyenne = 38.9
ecart_type = 13.28
effectif = 797 # echantillon effectivement mesuree , c.à.d sans les NA !

intervalle_inf = moyenne - 1.96 * ecart_type / math.sqrt(effectif)
intervalle_sup = moyenne + 1.96 * ecart_type / math.sqrt(effectif)

print("intervalle inferieur : ", intervalle_inf, "intervalle superieur : ", intervalle_sup)

# Score de relations croisées - étude cas-témoins
# Odds-Ratio

a = np.array([[840, 51663],[32, 5053]])
oddsratio, pvalue = stats.fisher_exact(a)
print("OddsR: ", oddsratio, "p-Value:", pvalue)
#>>> OddsR:  2.56743220487 p-Value: 2.72418938361e-09

# ecriture du ficher dataframe avec des entiers
np.savetxt("calcul_oddsratio.csv", a, delimiter=';',fmt='%d')

