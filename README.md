# Self Modifying Python

A simple project to demonstrate a means to randomly change an abstract syntax tree representing a simple python program.

To generate an initial set of programs, run the `generate.py` script.  This will fill the `dynamic_files` directory will pickled copies of simple, tree based python programs. 

To run a loop that will select, modify, and reevaluate some of these files, run the `selfmod.py` script.

The `tree_components.py` file contains the elements that make up the generated AST's, and the methods that generate and modify them.  