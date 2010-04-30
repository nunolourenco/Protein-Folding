from commons import *
from fitness_function import *
from mutation import *
from operator import itemgetter




population = []

def evaluate_ind(protein,ind):
    #print ind
    return fitness_function(protein,ind[0])
    


def ga(parameters):
    n_progenitors = parameters["pop_size"] / 2
    num_gen = parameters["number_generations"]
    #generate the initial population
    population = [(generate_ind(len(parameters["protein"])),0) for i in range(parameters["pop_size"])]
    print population
    #evaluate the quality of the initial population
    population = [(ind[0],evaluate_ind(parameters["protein"],ind)) for ind in population]
    while num_gen:
        # #select n_progenitors using the stockastic universal selection
        #         parents = stockastic_universal_selection(population,n_progenitors)
        #         for i in range(n_progenitors + 1):
        #           parents.append(population[i])
        #         offsprings = []
        #         #apply individual mutations
        #         for ind in parents:
        #             new_ind = ind
        #             if random() < parameters["mut_prob"]:
        #                 new_ind = monte_carlo_mutation(parameters["protein"],ind)
        #             offsprings.append(new_ind)
        #         
        #         #this code is just temporary
        #       if parameters["pop_size"] % 2 == 0:
        #           population = parents[:-1] + offsprings[:-1]
        #       else:
        #           population = parents[:] + offsprings[:-1]
        #       
        #         #print len(population)
        #         #print population
        #         population = [(ind[0],evaluate_ind(parameters["protein"],ind)) for ind in population]
        #         population.sort(key=itemgetter(1)) # minimization
        print population[0][0], population[0][1]      
        
        num_gen -= 1
    print "pimbas"
        
    

def stockastic_universal_selection(population,numb):
	""" Stochastic Universal Sampling."""
	pop = population[:]
	pop.sort(key=itemgetter(1))
	total_fitness = sum([indiv[1] for indiv in pop])
	value = uniform(0,1.0/numb)
	pointers = [ value + i * (1.0/numb) for i in range(numb)]
	mate_pool = []
	for j in range(numb):
		val = pointers[j]
		index = 0
		total =pop[index][1] / float(total_fitness + 0.00001)
		while total < val:
			index += 1
			total += pop[index][1] / float(total_fitness + 0.00001)
			mate_pool.append(pop[index])
	return mate_pool
    
    
    

def generate_ind(size):
    ind = [(0,0)]
    current_size = 1
    directions.values() 
    ind = create_ind(ind,current_size,size)
    return ind
    
    
    
def create_ind(ind,current_size,total_size):
    if current_size < total_size:    
        available_directions = directions.values()
          
        while len(available_directions) > 0:
            next_dir = choice(available_directions)
            available_directions.remove(next_dir)
            new_point = (lambda previous_pos,new_dir: (previous_pos[0] + new_dir[0], previous_pos[1] + new_dir[1])) (ind[-1],next_dir)
            if new_point not in ind:
                ind.append(new_point)
                current_size += 1
                ind = create_ind(ind,current_size,total_size)
                break
        
    return ind
    




#THIS STILL HAS ONE PROBLEM: CICLES :O
# def generate_ind(size):
#     print "1"
#     ind = [(0,0)]
#     previous_direction = (-1,-1)
#     for j in range(1,size):
#         previous_pos = ind[j-1]
#         while 1:
#             directions_copy = directions.values()
#             if(previous_direction != (-1,-1)):
#                 directions_copy.remove(previous_direction)
#             raw_input()
#             new_dir = choice(directions_copy)
#             new_point = (lambda previous_pos,new_dir: (previous_pos[0] + new_dir[0], previous_pos[1] + new_dir[1])) (previous_pos,new_dir)
#             #print "new_dir" + str(new_dir)
#             #print "ind " + str(ind)
#             #raw_input()
#             if new_point not in ind:
#                 previous_direction = new_dir
#                 ind.append(new_point)
#                 break
#     return ind
    
    
    
    

if __name__ == "__main__":
    parameters = {  "protein" : "BWBWWBBWBWWBWBBWWBWB",
                    "pop_size" : 20,
                    "mut_prob": 0.1,
                    "number_generations" : 2
                 }
    
    ga(parameters)
    