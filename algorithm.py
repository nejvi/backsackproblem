import Abstract
import random

random.seed()

class Algorithm(object):
    generation_counter = 1
    maximum_generations = 0
    population_size = 5
    prob_mutation = 0.4
    prob_crossover = 0.6
    clone_count = 0
    crossover_count = 0

    population = []
    items = []
    fitness = []
    next_gen = []

    sack = None
    total_fitness_of_generation = 0

    def __init__(self, sack, items):
        self.sack = sack
        self.items = items

    def selectGene(self):
        print('test')
        rand = random.uniform(0, self.total_fitness_of_generation)
        
        for i in range(0,self.population_size):
            if(rand <= self.fitness[i]): 
                return i
            rand -= self.fitness[i]
        
        return 0

    def mutateGen(self):
        if(random.random() <= self.prob_mutation):
            mut_gene = ""
            new_mut_gene = ""
            mut_point = 0
    
    def crossoverGenes(self, gene1, gene2):
        new_gene1 = ""
        new_gene2 = ""

        rand = random.random()
        if(rand <= self.prob_crossover):
            self.crossover_count += 1
            cross_point = random.uniform(1, self.items.len)

            new_gene1 = self.population[gene1][0:cross_point] + self.population[gene2][cross_point]
            new_gene2 = self.population[gene2][0:cross_point] + self.population[gene1][cross_point]

            self.next_gen.append(new_gene1, new_gene2)
        else:
            self.clone_count += 1
            self.next_gen.append(self.population[gene1], self.population[gene2])

        self.mutateGen()

    def generatePopulation(self):
        
        for i in range(0, self.population_size):
            gene = ""

            for j in range(0, self.sack.sack_items_count):
                if (random.random() > 0.5):
                    gene += "1"
                else: gene += "0"

        self.population.append(gene)
    
    def evaluateFitness(self):

        self.total_fitness_of_generation = 0
        fitest = 0
        fitest_index = 0

        for i in range(0, self.population_size):
            total_weight = 0
            total_value = 0
            fitness_value = 0
            diff = 0

            for j in range(0, self.sack.sack_items_count):
                if (self.population[j] == '1'):
                    item = self.items[j]
                    total_weight += item.weight
                    total_value += item.value

            diff = self.sack.capacity - total_weight
            if (diff >= 0):
                fitness_value = total_value
            
            self.fitness.append(fitness_value)
            if(fitness_value>fitest):
                fitest = fitness_value
                fitest_index = j

            self.total_fitness_of_generation += fitness_value
