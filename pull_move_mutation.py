from commons import *
from math import sqrt
from fitness_function import *


def pull_moves_mutation(ind,mut_prob):
    ind_to_mut = deepcopy(ind[0])
    
    #we start applying the mutation from the end of the protein untill we reach the element 1, as the algorithm instructs 
    for i in range(len(ind_to_mut) - 2,0,-1):
        print i
        if i == 1:
            print "am to mut = %d" % i
            l_pos = find_l_pos(i, ind_to_mut)
            #if l_pos in ind_to_mut:
            #    continue
            c_pos = find_c_pos(l_pos)
            if c_pos == ind_to_mut[i-1]:
                ind_to_mut[i] = l_pos
            elif c_pos not in ind_to_mut:
                ind_to_mut[i] = l_pos
                ind_to_mut[i - 1] = c_pos
                ind_to_mut = repair_conformation(i,ind_to_mut,ind[0])
            print ind_to_mut
    if check_ind_validity(ind_to_mut) == False:
        return (ind[0],0)
    return (ind_to_mut,0)
    
def check_ind_validity(ind):
    for i in range(len(ind)):
        if ind[i] in ind[i + 1: ]:
            print "Invalid conformation"
            return False
    #if there is two am which are separeted for more than on adjacente position, we have an invalid conformation
    for i in ind:
        for k in ind:
            if distance_between_am(i,k) > 1:
                return False
                
    return True
    
def find_l_pos(i,ind):
    l_pos = (lambda pos1,direction: (pos1[0] + direction[0], pos1[1] + direction[1])) (ind[i+1],directions["R"])
    if l_pos in ind:
        print "Bad Conformation. Going to try in the other direction"
        l_pos = (lambda pos1,direction: (pos1[0] + direction[0], pos1[1] + direction[1])) (ind[i+1],directions["L"])
    print l_pos
    return l_pos
    
def find_c_pos(l_pos):
    return (lambda pos1,pos2: (pos1[0] + pos2[0], pos1[1] + pos2[1])) (l_pos,directions["U"])


def repair_conformation(current_am,new_conformation,old_conformation):
    print "new_conformation ",
    print new_conformation
    print "old_conformation ",
    print old_conformation
    j = current_am - 2
    while j > 1 and not can_terminate(new_conformation, j):
        new_conformation[j] = old_conformation[j + 2]
        j -= 1
    return new_conformation
        
def can_terminate(conformation,current_am):
    if distance_between_am(conformation[current_am],conformation[current_am + 1]) == 1:
        return True
    else:
        return False


    
def distance_between_am(am1,am2):
    distance_vector = (lambda p1,p2: (p1[0] - p2[0],p1[1] - p2[1])) (am1,am2)
    distance_vector_modulus = sqrt(distance_vector[0] ** 2 + distance_vector[1] ** 2)
    return distance_vector_modulus

teste1 = [(0,0),(0,1),(1,1)]
teste2 = [(0,0),(0,1),(0,2),(1,2),(1,3),(2,3),(2,2),(2,1),(2,0)]
#print pull_moves_mutation((teste1,0),0.2)
print pull_moves_mutation((teste2,0),1)