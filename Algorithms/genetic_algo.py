import random

GENE = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789!@#$%^&*()_+=-{][":;'}?><,./]'''
POPULATION_SIZE = 100
TARGET = "Email: raohuraira331.rb@gmail.com Reg: L1F20BSCS0838, my name is huraira"

class GENETIC_ALGO(object):
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculateFitness()

    def calculateFitness(self):
        global TARGET
        fitness = 0
        for gs, gt in zip(self.chromosome, TARGET):
            if gs != gt: fitness += 1
        return fitness
    
    @classmethod
    def createGnome(self):
        global TARGET
        gnome_len = len(TARGET)
        return [self.mutateGene() for _ in range(gnome_len)]
    
    @classmethod
    def mutateGene(self):
        global GENE
        gene = random.choice(GENE)
        return gene
    
    def mate(self, gene):
        child_chromosome = []
        for gs, gt in zip(self.chromosome, gene.chromosome):
            prob = random.random()
            if prob <= 0.45:
                child_chromosome.append(gs)
            elif prob <= 0.95:
                child_chromosome.append(gt)
            else:
                child_chromosome.append(self.mutateGene())
        return GENETIC_ALGO(child_chromosome)
    
def main():
    global POPULATION_SIZE
    generation = 1
    population = []
    found = False

    for _ in range(POPULATION_SIZE):
        chromosome = GENETIC_ALGO.createGnome()
        population.append(GENETIC_ALGO(chromosome))

    while not found:
        # sort pop
        population = sorted(population, key= lambda x:x.fitness)

        if population[0].fitness <= 0:
            found = True
            break

        new_generation = []
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        s = int((90 * POPULATION_SIZE) / 100)

        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation
        print("Generation: {}\tString: {}\tFitness: {}".format(
            generation,
            "".join(population[0].chromosome),
            population[0].fitness))
        generation += 1
    
    print("Generation: {}\tString: {}\tFitness: {}".format(
            generation,
            "".join(population[0].chromosome),
            population[0].fitness))

if __name__ == '__main__':
    main()
