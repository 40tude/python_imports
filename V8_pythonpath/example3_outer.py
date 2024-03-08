# example3_outer.py


# Faut modifier le PYTHOPATH avant
# Aller dans le répertoire où se trouve example3_outer.py
# ! $env:PYTHONPATH = "$pwd/utils"
# La variable d'environnement n'est modifiée que le temps de la session
import length


txt = "Hello Zoubida"
res_len = length.get_length(txt)
print("The length of the string is: ", res_len)
