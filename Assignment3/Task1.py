import random


def uniform_crossover(parent1, parent2):
    offspring = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            offspring.append(parent1[i])
        else:
            offspring.append(parent2[i])
    return offspring


def fitness(chromosome):
    a, b, c, d, e, f, g, h = chromosome
    return (a + b) - (c + d) + (e + f) - (g + h)


population = [
    [6, 5, 4, 1, 3, 5, 3, 2],
    [8, 7, 1, 2, 6, 6, 0, 1],
    [2, 3, 9, 2, 1, 2, 8, 5],
    [4, 1, 8, 5, 2, 0, 9, 4]
]

fitness_values = [fitness(chromosome) for chromosome in population]

for i in range(len(population)):
    print("Population: ", population[i], end=' ')
    print("\tFitness: ", fitness_values[i])

sorted_population = [chromosome for chromosome in sorted(
    population, key=fitness, reverse=True)]

print("\nScorted from Best to Least Fitness")
for chromosome in sorted_population:
    print(chromosome)


parent1 = sorted_population[0]
parent3 = sorted_population[2]
offspring = uniform_crossover(parent1, parent3)
print("\nB: Offspring:", offspring)

# generating new chromosome
offspring1 = uniform_crossover(parent1, parent3)
offspring2 = uniform_crossover(parent1, parent3)
offspring3 = uniform_crossover(parent1, parent3)
offspring4 = uniform_crossover(parent1, parent3)
offspring5 = uniform_crossover(parent1, parent3)

new_population = [offspring, offspring1, offspring2,
                  offspring3, offspring4, offspring5]

fitness_values_new = [fitness(chromosome) for chromosome in new_population]

max_fitness_index = fitness_values_new.index(max(fitness_values_new))
solution = new_population[max_fitness_index]

print("\n\nC: New Population:")
for chromosome in new_population:
    print(chromosome)
print("Solution (Maximum Fitness Chromosome): ", solution)
print("Fitness: ", max(fitness_values_new))

if (max(fitness_values) > max(fitness_values_new)):
    print("Could not generate max fitness value")
else:
    print("New Best Fitness: ", max(fitness_values_new))
