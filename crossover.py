from mutation import apply_rotation
from commons import cenas
from fitness_function import *


def crossover(protein,parents):
    possible_rotations = [0,90,180,270]
    is_invalid = True
    while is_invalid:
        is_invalid = False
        p1 = choice(parents)
        p2 = choice(parents)
        parent1 = p1[0]
        parent2 = p2[0]
        offspring = []
        cut_point = choice(range(len(protein)))        
        rotation_to_apply = choice(possible_rotations)
        offspring += parent1[:cut_point+1]
        pivot = offspring[cut_point]
        offspring_tail = remap_parent2_coords(pivot,parent2[cut_point:],rotation_to_apply)
        if offspring_tail == None:
            is_invalid = True
        else:
            for c in offspring_tail:
                if c in offspring:
                    is_invalid = True
                    break
            else:
                offspring += offspring_tail
    new_ind = (offspring,fitness_function(protein,offspring))
    return new_ind
    
def remap_parent2_coords(reference_am,pos_cut_point_parent2,angle_to_rotate):
    remaped_parent = []
    #gets the directons which the amino-acids are arranged
    for i in range(len(pos_cut_point_parent2)-1):
         remaped_parent.append((pos_cut_point_parent2[i+1][0] - pos_cut_point_parent2[i][0],pos_cut_point_parent2[i+1][1] - pos_cut_point_parent2[i][1]))
    
    #applys random_rotation
    for i in range(len(remaped_parent)):
        remaped_parent[i] = apply_rotation(remaped_parent[i],angle_to_rotate)
    
    #puts the new amino-acids configuraton according to the cut_point amino-acid
    temp = [reference_am]
    for i in range(len(remaped_parent)):
        new_pos = (remaped_parent[i][0] + temp[i][0],remaped_parent[i][1] + temp[i][1])
        if(new_pos in temp):
            print "exists"
            return None
        else:
            temp.append(new_pos)
    
    remaped_parent = temp[1:]

    return remaped_parent

    
    
        
    
parent1 = ([(0,0),(1,0),(1,1),(1,2),(0,2),(0,1),(-1,1),(-1,2),(-2,2),(-2,3),(-3,3),(-3,2),(-3,1),(-2,1),(-2,0),(-2,-1),(-3,-1),(-3,-2),(-3,-3),(-2,-3)],0)
parent2 = ([(0,0),(1,0),(1,-1),(1,-2),(1,-3),(1,-4),(0,-4),(-1,-4),(-1,-3),(-1,-2),(-2,-2),(-3,-2),(-3,-3),(-4,-3),(-5,-3),(-5,-2),(-6,-2),(-6,-3),(-6,-4),(-5,-4)],0)
p = "BWBWWBBWBWWBWBBWWBWB"

print crossover(p,[parent1,parent2])
            
            
    
