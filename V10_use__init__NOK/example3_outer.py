# example3_outer.py
import os
import sys

fpath = os.path.join(os.path.dirname(__file__), "utils")
sys.path.append(fpath)

# print()
# print("Vour le /utils à la fin du 'sys.path'")
# print(sys.path)
# print()

# ! MARCHER PAS, c'est normal
# voir ./utils/__init__.py
# because even though length.py and others are at the same level as the __init__.py, this is not the level from which init will be called
# voir V11 le contenu de ./utils/__init__.py

# import length
# import upper
# import lower
import utils

txt = "Zoubida"
res_len = length.get_length(txt)
print("The length of the string is : ", res_len)

res_up = upper.to_upper(txt)
print("Uppercase txt               : ", res_up)

res_low = lower.to_lower(txt)
print("Uppercase txt               : ", res_low)
