# example3_outer.py
import os
import sys

# fpath = os.path.join(os.path.dirname(__file__), "utils")
# sys.path.append(fpath)

# # voir ./utils/__init__.py
# # Now we have converted our utils directory into a package
# import utils

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
print()
print(PROJECT_ROOT)

sys.path.append(PROJECT_ROOT)
print()
print(sys.path)
import utils


txt = "Zoubida"
res_len = utils.get_length(txt)
print("The length of the string is : ", res_len)

res_up = utils.to_upper(txt)
print("Uppercase txt               : ", res_up)

res_low = utils.to_lower(txt)
print("Uppercase txt               : ", res_low)

utils.yolo(56)
