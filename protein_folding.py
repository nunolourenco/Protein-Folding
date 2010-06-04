from commons import *
from fitness_function import fitness_function
from mutation import monte_carlo_mutation
from crossover import crossover
from pull_move_mutation import pull_moves_mutation
from operator import itemgetter
import cPickle



population = []


def display_results(total_statitic,parameters,display=1):
    num_runs = parameters["num_runs"]
    results_gen = zip(*total_statitic)
    best = [min([ind[0] for ind in gen]) for gen in results_gen]
    averages = [sum([ind[1] for ind in gen])/float(num_runs) for gen in results_gen]
    # if display == 1:
    #         # Show
    #         ylabel('Fitness')
    #         xlabel('Generation')
    #         titulo = 'Protein Folding Problem: %d Runs' % num_runs
    #         title(titulo)
    #         axis= [0,parameters["number_generations"],0,parameters["protein"]]
    #         p1 = plot(best,'r-o',label="Best")
    #         p2 = plot(averages,'g-s',label="Average")
    #         legend(loc=2)
    #         show()
    return best
    

def evaluate_ind(protein,ind):
    return fitness_function(protein,ind[0])
    


def ga(parameters):
    statistic = []
    population = []
    n_progenitors = parameters["pop_size"] / 2 
    num_gen = parameters["number_generations"]
    #generate the initial population
    if parameters["load_population"] == 1:
        population = load_population()
    else: 
        population = [(generate_ind(len(parameters["protein"])),0) for i in range(parameters["pop_size"])]
    #evaluate the quality of the initial population
    population = [(ind[0],evaluate_ind(parameters["protein"],ind)) for ind in population]
    population.sort(key=itemgetter(1)) # minimization
    while num_gen:
        #print  parameters["number_generations"] - num_gen
        
        #calculate the population statistics
        average_quality = sum([ind[1] for ind in population])/ float(len(population))
        best_quality = population[0][1]
        statistic.append((best_quality,average_quality))
        
        #select n_progenitors using the stockastic universal selection
        if random() < parameters["xover_prob"]:
            parents = stockastic_universal_selection(population,n_progenitors)
        
            offsprings = [crossover(parameters["protein"],parents) for i in range(n_progenitors)]
        else:
            offsprings = population
        
        
        #apply individual mutations
        new_population = []
        for ind in offsprings:
            new_ind = ind
            if random() < parameters["mut_prob"]:
                if parameters["mutation_type"] == "pull_moves":
                    #print "pull_moves"
                    new_ind = pull_moves_mutation(parameters["protein"],ind,parameters["mut_prob"])
                else:
                    #print "monte_carlo"
                    new_ind = monte_carlo_mutation(parameters["protein"],ind)
            new_population.append(new_ind)
            
        new_population.sort(key=itemgetter(1))
        
        elite_size = int(round((parameters["survivors_perc"]) * parameters["pop_size"]))
        survivors_size = int(parameters["pop_size"] - elite_size)
        #population to the next generation
        population = population[:elite_size] + new_population[:survivors_size]
        
        #evaluates and sorts the new population
        population = [(ind[0],evaluate_ind(parameters["protein"],ind)) for ind in population]
        population.sort(key=itemgetter(1)) # minimization
        #print population[0][0], population[0][1]      
        
        num_gen -= 1    
    #print population[0][0], population[0][1]    
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
    
    
def generate_population(parameters):
    size = len(parameters["protein"])
    population = [(generate_ind(len(parameters["protein"])),0) for i in range(parameters["pop_size"])]
    path = "populations/" + parameters["protein"] + ".bin"
    f = open(path,"wb")
    cPickle.dump(population,f)
    print population
    

def load_population():
    path = "populations/" + parameters["protein"] + ".bin"
    f = open(path,"rb")
    population = cPickle.load(f)
    return population
    
    

if __name__ == "__main__":
    #0.05,0.10,0.15,0.20
    mutation_values = [0.05,0.10,0.15,0.20]
    best_by_runs = []
    run = 0
    count_mut = 0
    parameters = {  "protein" : "BWBWWBBWBWWBWBBWWBWB",
                    "pop_size" : 200,
                    "mut_prob": 0.05,
                    "number_generations" : 500,
                    "survivors_perc" : 0.05,
                    "mutation_type" : "pull_moves",
                    "xover_prob" : 0.90,
                    "num_runs" : 30,
                    "show_graph" : 0,
                    "generate_population" : 0,
                    "load_population" : 0
                 }
    if parameters["generate_population"] :
        generate_population(parameters)
    else:
        while count_mut < len(mutation_values) :
            
            
            parameters["mut_prob"] = mutation_values[count_mut]
            run = 0
            best_by_runs = []
            parameters["mutation_type"] = "pull_moves"
            print "Pull Moves"
            while run < parameters["num_runs"]:
                print "Run %d" % run
                statistics = [ga(parameters)]
                best_by_runs.append(min(display_results(statistics,parameters,parameters["show_graph"])))
                run += 1
            create_files(best_by_runs,parameters)
            
            
            #run algorithm to monte carlo
            run = 0
            best_by_runs = []
            parameters["mutation_type"] = "monte_carlo"
            print "Monte Carlo"
            while run < parameters["num_runs"]:
                print "Run %d" % run
                statistics = [ga(parameters)]
                best_by_runs.append(min(display_results(statistics,parameters,parameters["show_graph"])))
                run += 1
            create_files(best_by_runs,parameters)
            count_mut += 1

#Protein size 20: BWBWWBBWBWWBWBBWWBWB
#Protein size 24: BBWWBWWBWWBWWBWWBWWBWWBB
#Protein size 25: WWBWWBBWWWWBBWWWWBBWWWWBB
