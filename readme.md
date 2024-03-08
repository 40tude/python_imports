### read 

* https://medium.com/towards-data-science/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355


* The python interpreter look for the directory containing the module we are importing in ```sys.path``` (see V2/example3.py)
* Once the interpreter is done with the cached modules and the standard library modules ```sys.path``` is the list where it will search for.
* Remember : whenever an import statement is executed, the entire module is run (see V3)
* This where ```if __name__ == '__main__': ``` can help (see V4) 
* Import only what you need (see V5)
* utils directory (see V6, V7_sys_path_append, V8_pythonpath)
  * $env:PYTHONPATH
  * $env:PYTHONPATH = "$pwd/utils"
* V9 sys_path_append but multiple import in example3_outer.py
* V10 use ```utils/__init__.py``` incorrectly
* V11 use ```utils/__init__.py``` with absolute path correctly. Only one ```import utils``` in example3_outer.py and ```utils.get_length(txt)```
* V12 show how to call ```utils.get_length("Hello")``` from ./utils/example3.py
* V13 show how to add the ```yolo()``` from /scripts/example1.py to the utils package and use it in /scripts/example3.py
* V14 use ```PROJECT_ROOT``` in example3_outer.py and /scripts/example3.py
  ```
  PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
  sys.path.append(PROJECT_ROOT)
  import utils
  ```
  



