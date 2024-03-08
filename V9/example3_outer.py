# example3_outer.py
import os
import sys

# The order of imports is important
fpath = os.path.join(os.path.dirname(__file__), "utils")
sys.path.append(fpath)

print()
print("Voir le /utils à la fin du 'sys.path'")
print(sys.path)
print()
import length
import upper
import lower

txt = "Zoubida"
res_len = length.get_length(txt)
print("The length of the string is : ", res_len)

res_up = upper.to_upper(txt)
print("Uppercase txt               : ", res_up)

res_low = lower.to_lower(txt)
print("Uppercase txt               : ", res_low)
