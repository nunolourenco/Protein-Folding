from random import *
from math import *
from copy import deepcopy
directions = {"U": (0,1),
              "D": (0,-1),
              "R": (1,0),
              "L": (-1,0)}

inverted_dir_dict = {(0,1):"U",
         (0,-1):"D",
         (1,0):"R",
         (-1,0):"L"}