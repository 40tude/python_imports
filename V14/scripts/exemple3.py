# scripts/example3.py
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
print()
print(PROJECT_ROOT)

sys.path.append(PROJECT_ROOT)
print()
print(sys.path)
import utils


# voir utils/__init__.py
# où on a ajouté example1/yolo()

print(utils.get_length("Hello"))
utils.yolo(42)
