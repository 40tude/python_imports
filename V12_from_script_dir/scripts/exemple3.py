# scripts/example3.py
import os
import sys

# Before importing utils package, we must make sure utils's parent directory (project root) is accessible to the Python interpreter.
# It will be imprudent to assume it will happen by default, mainly because we are now one level inside the project root directory
# Indeed, we are running the script from scripts/example3.py
# The sys.path will have ....python_imports\\V12_from_script_dir\\scripts at index 0.
# voir os.pardir : give the path to the parent directory using dot notation ".."
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(PROJECT_ROOT)

print()
print("Vour le /utils à la fin du 'sys.path'")
print(sys.path)
print()


import utils

print(utils.get_length("Hello"))
