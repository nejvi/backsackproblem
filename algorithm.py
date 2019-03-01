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
    generation_solution = []

    sack = None
    total_fitness_of_generation = 0

    def __init__(self, sack, items):
        self.sack = sack
        self.items = items

    def performAlgorithm(self):
        self.maximum_generations = self.population_size

        self.generatePopulation()

        self.evaluateFitness()
        print("\n Fitness: ")
        for i in range(0, self.population_size-1):
            print(i+1, "-", self.fitness[i])
        
        while(self.maximum_generations>= 0):
            self.evaluateFitness()
            
            for i in range(0, int(self.population_size-1/2)):
                if(self.population_size % 2 == 1):
                    self.next_gen.append(self.generation_solution[self.generation_counter -1])
                
                gene1 = self.selectGene()
                gene2 = self.selectGene()

                self.crossoverGenes(gene1, gene2)

            self.evaluateFitness()

            for i in range(0, self.population_size-1):
                print("#",i+1, " ", self.next_gen[i])
                self.population[i] = self.next_gen[i]
                # self.population.insert(i, self.next_gen[i])
            
            print("\n Fitness: ")
            for m in range(0, self.population_size-1):
                print(m+1, " - ", self.fitness[m])
            
            self.next_gen.clear()
            self.fitness.clear()

            print("Crossover occurred ", self.crossover_count, " times.")
            print("Cloning occurred ", self.clone_count, " times.")
            
            if(self.clone_count==0):
                print("Mutation did not occur \n")
            else:
                print("Mutation did occur \n")
            
            self.maximum_generations -= 1

    def selectGene(self):
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
            which_gene = random.random()

            if(which_gene <= 0.5):
                mut_gene = self.next_gen[len(self.next_gen) - 1]
                mut_point = random.randint(0, len(self.items)-2)
                
                if(mut_gene[mut_point:mut_point + 1] == "1"):
                    new_mut_gene = mut_gene[0:mut_point] + "0" + mut_gene[mut_point + 1]
                    self.next_gen[len(self.next_gen)-1] = new_mut_gene
                
                if(mut_gene[mut_point:mut_point + 1] == "0"):
                    new_mut_gene = mut_gene[0:mut_point] + "1" + mut_gene[mut_point + 1]
                    self.next_gen[len(self.next_gen)-1] = new_mut_gene
                    # self.next_gen.insert(len(self.next_gen)-1, new_mut_gene)
            
            if(which_gene > 0.5):
                mut_gene = self.next_gen[len(self.next_gen) - 2]
                mut_point = random.randint(0, len(self.items)-2)

                if(mut_gene[mut_point:mut_point + 1] == "1"):
                    new_mut_gene = mut_gene[0:mut_point] + "0" + mut_gene[mut_point + 1]
                    self.next_gen[len(self.next_gen)-1] = new_mut_gene 

                if(mut_gene[mut_point:mut_point + 1] == "0"):
                    new_mut_gene = mut_gene[0:mut_point] + "1" + mut_gene[mut_point + 1]
                    self.next_gen[len(self.next_gen)-2] = new_mut_gene

    def crossoverGenes(self, gene1, gene2):
        new_gene1 = ""
        new_gene2 = ""

        rand = random.random()
        if(rand <= self.prob_crossover):
            self.crossover_count += 1
            cross_point = random.randint(0, len(self.items)-2)
            # cross_point = random.uniform(1, len(self.items))

            new_gene1 = self.population[gene1][0:cross_point] + self.population[gene2][cross_point]
            new_gene2 = self.population[gene2][0:cross_point] + self.population[gene1][cross_point]

            # self.next_gen.extend((new_gene1, new_gene2))
        else:
            self.clone_count += 1
            # self.next_gen.extend((self.population[gene1], self.population[gene2]))

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

        for i in range(0, self.population_size-1):
            total_weight = 0
            total_value = 0
            fitness_value = 0
            diff = 0
            for j in range(0, self.sack.sack_items_count-1):
                if (self.population[i][j] == '1'):
                    item = self.items[j]
                    total_weight += item.weight
                    total_value += item.value

            diff = self.sack.max_capacity - total_weight
            if (diff >= 0):
                fitness_value = total_value
            
            self.fitness.append(fitness_value)
            if(fitness_value>fitest):
                fitest = fitness_value
                fitest_index = i

            self.total_fitness_of_generation += fitness_value

        print("Total Generation Fitness : ", self.total_fitness_of_generation)
        print("The fittest chromosome of this generation is ", self.population[fitest_index])
        print(" And its fitness is ", self.fitness[fitest_index])
            
        self.generation_solution.append(self.population[fitest_index])
