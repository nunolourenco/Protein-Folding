from commons import *
from fitness_function import *


def pull_moves_mutation(ind,mut_prob):
    ind_to_mut = deepcopy(ind[0])
    #reverse the list so that we start mutating in the last am, as the algorithm says
    ind_to_mut.reverse()
    #we start in the second am, because in the first one the is no previous am, and we stop at the last - 1 because in the last one there is no i + 1
    for i in range(1,len(ind_to_mut) - 1):
        l_pos = find_l_pos(i, ind_to_mut)
        print l_pos
        
        c_pos = find_c_pos(l_pos)
        print c_pos
        if c_pos == ind_to_mut[i-1]:
            ind_to_mut[i] = l_pos
        else:
            ind_to_mut[i] = l_pos
            ind_to_mut[i - 1] = c_pos
            ind_to_mut = repair_conformation(i,ind_to_mut)
    
    ind_to_mut.reverse()
    return ind_to_mut
    
    
def find_l_pos(i,ind):
    possible_l_pos = ["R","L"]
    while len(possible_l_pos) > 0 :
        l_pos_dir = choice(possible_l_pos)
        possible_l_pos.remove(l_pos_dir)
        l_pos = (lambda pos1,direction: (pos1[0] + direction[0], pos1[1] + direction[1])) (ind[i+1],directions[l_pos_dir])
        if l_pos in ind:
            continue
        else:
            break
    return l_pos
    
def find_c_pos(l_pos):
    return (lambda pos1,pos2: (pos1[0] + pos2[0], pos1[1] + pos2[1])) (l_pos,directions["U"])


def repair_conformation(current_am,conformation):
    j = current_am - 2
    while j > 0:
        conformation[j] = conformation[j + 2]
        j -= 1
    
    return conformation
        
    



pos = [(0,0),(0,1),(1,1)]

print pull_moves_mutation((pos,0),0.2)