from random import *
from math import *
#import matplotlib
#from pylab import *
from copy import deepcopy
import os
directions = {"U": (0,1),
              "D": (0,-1),
              "R": (1,0),
              "L": (-1,0)}

inverted_dir_dict = {(0,1):"U",
         (0,-1):"D",
         (1,0):"R",
         (-1,0):"L"}
         

def create_files(best_by_runs,parameters):
    dir_name = parameters["mutation_type"] + "_" + str(parameters["mut_prob"])
    files_in_dir = os.listdir(".")
    if dir_name not in files_in_dir:
        os.mkdir(dir_name)
    file_fitness = open(dir_name + "/" + dir_name + "_results_by_run.txt","w")
    file_parameters = open(dir_name + "/parameters.txt","w")
    for value in best_by_runs:
        file_fitness.write(str(value) + "\n")
    for key in parameters:
        file_parameters.write(str(key) + " : " + str(parameters[key]) + "\n")
        
    file_fitness.close()
    file_parameters.close()