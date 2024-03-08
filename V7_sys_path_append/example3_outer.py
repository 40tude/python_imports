# example3_outer.py
import os
import sys

# The order of imports is important
fpath = os.path.join(os.path.dirname(__file__), "utils")
sys.path.append(fpath)

print()
print("Vour le /utils à la fin du 'sys.path'")
print(sys.path)
print()
import length

txt = "Zoubida"
res_len = length.get_length(txt)
print("The length of the string is: ", res_len)
