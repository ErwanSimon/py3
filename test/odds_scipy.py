import scipy
import scipy.stats as stats
import numpy as np

#table = df.groupby(level="Cancer").sum().values
#print(table)

#>>> array([[  840, 51663],
#           [   32,  5053]])

a = np.array([[840, 51663],[32, 5053]])

print(a)

#oddsratio, pvalue = stats.fisher_exact(table)
oddsratio, pvalue = stats.fisher_exact(a)
print("OddsR: ", oddsratio, "p-Value:", pvalue)

#>>> OddsR:  2.56743220487 p-Value: 2.72418938361e-09

# puis calcul simple d'un intervalle de confiance à 95%
