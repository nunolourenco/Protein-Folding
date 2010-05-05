def crossover(protein,parents):
    possible_rotations = [90,180,270]
    is_valid = True
    while is_invalid:
        p1 = choice(parents)
        p2 = choice(parents)
        parent1 = p1[0]
        parent2 = p2[0]
        offspring = []
        cut_point = choice(range(len(protein)))
        rotation_to_apply = choice(possible_rotations)        
        offspring += parent1[:cut_point+1]
        is_invalid = False
        for i in range(cut_point + 1,len(parent1)):
            #bring to (0,0) to rotate using cut_point as reference
            am_to_rotate = (lambda p1,p2: (p1[0] - p2[0], p1[1] - p2[1])) (parent2[i], parent1[cut_point])
            new_pos = apply_rotation(am_to_rotate,rotation_to_apply)
            #put the point back in the position it belongs
            new_pos = (lambda p1,p2: (p1[0] + p2[0], p1[1] + p2[1])) (new_pos, parent1[cut_point])
            if new_pos in offspring:
                is_invalid  = True
                break
            else:
                offspring.append(new_pos)
    new_ind = (offspring,fitness_function(protein,offspring))
    return new_ind
            
            
    
