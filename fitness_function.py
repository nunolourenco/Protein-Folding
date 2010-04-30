from commons import *

def fitness_function(protein,positions):
    fitness = 0
    #searches for index of B amino acids
    b_indexes = [index for index in range(len(protein)) if protein[index] == "B"]
    #print b_indexes
    for i in range(len(b_indexes)):
        for k in range(i + 1, len(b_indexes)):
            #print "i %d" % i
            #print "k %d" % k
            #print "b_indexes[k] = %d" % b_indexes[k]
            #print positions[b_indexes[i]]
            #print positions[b_indexes[k]]
            diff = ((lambda t1,t2: (t1[0] - t2[0],t1[1] - t2[1])) (positions[b_indexes[i]], positions[b_indexes[k]]))
            if diff in directions.values() and b_indexes[k] - b_indexes[i] > 1:
                fitness -= 1
            
    return fitness





#pos = [(0,0),(0,1),(1,1),(1,2),(0,2),(0,1),(-1,1),(-1,2),(-2,2),(-2,3),(-3,3),(-3,2),(-3,1),(-2,1),(-2,0),(-3,0),(-3,-1),(-2,-1),(-1,-1),(-1,0)]

#print fitness_function("BWBWWBBWBWWBWBBWWBWB",pos)