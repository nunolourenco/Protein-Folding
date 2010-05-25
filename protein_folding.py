from commons import *
from fitness_function import fitness_function
from mutation import monte_carlo_mutation
from crossover import crossover
from pull_move_mutation import pull_moves_mutation
from operator import itemgetter



population = []


def display_results(total_statitic,parameters):
    num_runs = 1
    results_gen = zip(*total_statitic)
    best = [min([ind[0] for ind in gen]) for gen in results_gen]
    averages = [sum([ind[1] for ind in gen])/float(num_runs) for gen in results_gen]
    # Show
    ylabel('Fitness')
    xlabel('Generation')
    titulo = 'Protein Folding Problem: %d Runs' % num_runs
    title(titulo)
    axis= [0,parameters["number_generations"],0,parameters["protein"]]
    p1 = plot(best,'r-o',label="Best")
    p2 = plot(averages,'g-s',label="Average")
    legend(loc=2)
    show()
    

def evaluate_ind(protein,ind):
    return fitness_function(protein,ind[0])
    


def ga(parameters):
    statistic = []
    n_progenitors = parameters["pop_size"] / 2 
    num_gen = parameters["number_generations"]
    #generate the initial population
    population = [(generate_ind(len(parameters["protein"])),0) for i in range(parameters["pop_size"])]
    #print population
    #evaluate the quality of the initial population
    population = [(ind[0],evaluate_ind(parameters["protein"],ind)) for ind in population]
    population.sort(key=itemgetter(1)) # minimization
    while num_gen:
        print  parameters["number_generations"] - num_gen
        
        #calculate the population statistics
        average_quality = sum([ind[1] for ind in population])/ float(len(population))
        best_quality = population[0][1]
        statistic.append((best_quality,average_quality))
        
        
        
        
        #select n_progenitors using the stockastic universal selection
        parents = stockastic_universal_selection(population,n_progenitors)
        
        offsprings = [crossover(parameters["protein"],parents) for i in range(n_progenitors)]
        
        
        #apply individual mutations
        new_population = []
        for ind in offsprings:
            new_ind = ind
            if random() < parameters["mut_prob"]:
                if parameters["mutation_type"] == "pull_moves":
                    new_ind = pull_moves_mutation(parameters["protein"],ind,parameters["mut_prob"])
                else:
                    new_ind = monte_carlo_mutation(parameters["protein"],ind)
            new_population.append(new_ind)
            
        new_population.sort(key=itemgetter(1))
        
        elite_size = int(round((parameters["survivors_perc"]) * parameters["pop_size"]))
        print elite_size
        survivors_size = int(parameters["pop_size"] - elite_size)
        #population to the next generation
        population = population[:elite_size] + new_population[:survivors_size]
        
        #evaluates and sorts the new population
        population = [(ind[0],evaluate_ind(parameters["protein"],ind)) for ind in population]
        population.sort(key=itemgetter(1)) # minimization
        print population[0][0], population[0][1]      
        
        num_gen -= 1        
    return statistic
    
    
#This function is not working properly
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
		total =pop[index][1] / float(total_fitness)
		while total < val:
			index += 1
			total += pop[index][1] / float(total_fitness)
		mate_pool.append(pop[index])
	return mate_pool
    
    
    

def generate_ind(size):
    ind = [(0,0)]
    current_size = 1
    directions.values() 
    ind = create_ind(ind,current_size,size)
    if len(ind) < size:
        print "There was an error while generating an individual"
        raw_input()
    return ind
    
    
    
def create_ind(ind,current_size,total_size):
    if current_size < total_size:    
        available_directions = deepcopy(directions.values())
          
        while len(available_directions) > 0:
            next_dir = choice(available_directions)
            available_directions.remove(next_dir)
            new_point = (lambda previous_pos,new_dir: (previous_pos[0] + new_dir[0], previous_pos[1] + new_dir[1])) (ind[-1],next_dir)
            if new_point not in ind:
                ind.append(new_point)
                current_size += 1
                ind = create_ind(ind,current_size,total_size)
            if len(ind) == total_size:
                break
            
        else:
            return ind[:-1]
                
        
    return ind
    
    

if __name__ == "__main__":
    parameters = {  "protein" : "BWBWWBBWBWWBWBBWWBWB",
                    "pop_size" : 200,
                    "mut_prob": 0.15,
                    "number_generations" : 500,
                    "survivors_perc" : 0.005,
                    "mutation_type" : "pull_moves"
                 }
    display_results([ga(parameters)],parameters)
#Protein size 20: BWBWWBBWBWWBWBBWWBWB
#Protein size 24: BBWWBWWBWWBWWBWWBWWBWWBB