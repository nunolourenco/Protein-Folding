from commons import *
from fitness_function import *

possible_rotations = [90,180,270]
ck = 2
#am stands for amino-acid

#receives
def monte_carlo_mutation(protein,ind):
    mutation_tries = 0 #defines the number of tries to mutate the indivuidual
    conformation_s1 = ind[0]
    conformation_s2 = []
    exists = True
    while exists and mutation_tries != 10:
        #defines the am that on wich the rotation will be applied
        am_pivot = choice(range(len(conformation_s1)))
        rotation_to_apply = choice(possible_rotations)
        #print "pivot = %d" %(am_pivot)
        #print "rotation_to_apply = %d" %(rotation_to_apply)
        for i in range(len(conformation_s1)):
            exists = False
            if i > am_pivot:
                #bring to (0,0) to rotate using am_pivot as reference
                am_to_rotate = (lambda p1,p2: (p1[0] - p2[0], p1[1] - p2[1])) (conformation_s1[i], conformation_s1[am_pivot])
                new_pos = apply_rotation(am_to_rotate,rotation_to_apply)
                #put the point back in the position it belongs
                new_pos = (lambda p1,p2: (p1[0] + p2[0], p1[1] + p2[1])) (new_pos, conformation_s1[am_pivot])
                if new_pos in conformation_s2:
                    #we have to try another rotation
                    mutation_tries += 1
                    exists = True
                    break
                else:
                    conformation_s2.append(new_pos)
            else:
                conformation_s2.append(conformation_s1[i])
        
    if not exists:
        new_ind = (conformation_s2,fitness_function(protein,conformation_s2))
        return check_acceptance(new_ind,ind)
    else:
        return ind
        
#return the new individual, if the criteria is accepted, the old one if not
def check_acceptance(new_ind, old_ind):
    #compare the fitness
    if new_ind[1] <= old_ind[1]:
        return new_ind
    else:
        #gerar um numero aleatoria para ver se podemos aceitar a nova conformacao
        rnd_number = random()
        validation_value = e**((old_ind[1] - new_ind[1]) / ck)
        if rnd_number < validation_value:
            #we accept the conformation
            return new_ind
        else:
            return old_ind
    
    

#applies a counterclockwise rotation
def apply_rotation(pos, angle):
    angle = (angle * pi) / 180
    x = pos[0] * int(cos(angle)) - pos[1] * int(sin(angle))
    y = pos[0] * int(sin(angle)) + pos[1] * int(cos(angle))
    return (x,y)    
    













#am_pivot = 10
#rotation_to_apply = 270
   
#print apply_rotation((0,1),90) 

# pos = [(0,0),(0,1),(1,1),(1,2),(0,2),(0,1),(-1,1),(-1,2),(-2,2),(-2,3),(-3,3),(-3,2),(-3,1),(-2,1),(-2,0),(-3,0),(-3,-1),(-2,-1),(-1,-1),(-1,0)]
# pos1 = [(0,0),(0,1),(1,1),(1,2),(0,2),(0,1),(-1,1),(-1,2),(-2,2),(-2,3),(-3,3),(-3,4),(-3,5),(-4,5),(-4,6),(-3,6),(-3,7),(-4,7),(-5,7),(-5,6)]
# 
# cenas = monte_carlo_mutation("BWBWWBBWBWWBWBBWWBWB",(pos1,-4))
# for i in range(len(pos)):
#     print str(i) + " " + str(pos[i]) + " " + str(cenas[0][i])
# print pos
# print cenas
# print cenas[0] == pos
