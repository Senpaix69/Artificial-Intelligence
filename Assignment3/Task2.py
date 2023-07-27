import random

objects = [1, 2, 3, 4, 5, 6, 7]
profit = [5, 10, 15, 7, 8, 9, 4]
weight = [1, 3, 5, 4, 1, 3, 2]
max_knapsack_size = 15

population_size = 6
num_iterations = 3


def generate_random_solution():
    solution = []
    for _ in range(len(objects)):
        solution.append(random.choice([0, 1]))
    return solution


def calculate_fitness(solution):
    total_profit = 0
    total_weight = 0
    for i in range(len(objects)):
        if solution[i] == 1:
            total_profit += profit[i]
            total_weight += weight[i]
    if total_weight > max_knapsack_size:
        total_profit = 0
    return total_profit


def rank_selection(population):
    sorted_population = sorted(
        population, key=lambda x: calculate_fitness(x), reverse=True)
    rank_probabilities = [i / len(population)
                          for i in range(1, len(population) + 1)]
    parent_pairs = []
    for _ in range(len(population) // 2):
        parent1 = random.choices(
            sorted_population, weights=rank_probabilities)[0]
        parent2 = random.choices(
            sorted_population, weights=rank_probabilities)[0]
        parent_pairs.append((parent1, parent2))
    return parent_pairs


def uniform_crossover(parent1, parent2):
    offspring1 = []
    offspring2 = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            offspring1.append(parent1[i])
            offspring2.append(parent2[i])
        else:
            offspring1.append(parent2[i])
            offspring2.append(parent1[i])
    return offspring1, offspring2


def mutate_chromosome(chromosome, mutation_rate):
    mutated_chromosome = []
    for gene in chromosome:
        if random.random() < mutation_rate:
            mutated_gene = 1 - gene
            mutated_chromosome.append(mutated_gene)
        else:
            mutated_chromosome.append(gene)
    return mutated_chromosome


population = []
all_populations = []

# Initial population
for _ in range(population_size):
    solution = generate_random_solution()
    population.append(solution)
all_populations.append(population)

# Evolution iterations
for iteration in range(num_iterations):
    print(f"Iteration {iteration + 1}")
    print("---------------")

    print("\nFitness of each solution:")
    for solution in population:
        fitness = calculate_fitness(solution)
        print("Solution:", solution, "Fitness:", fitness)

    parent_pairs = rank_selection(population)

    offspring_population = []
    for parent1, parent2 in parent_pairs:
        offspring1, offspring2 = uniform_crossover(parent1, parent2)
        offspring_population.append(offspring1)
        offspring_population.append(offspring2)

    mutated_offspring_population = []
    mutation_rate = 0.1

    for offspring in offspring_population:
        mutated_offspring = mutate_chromosome(offspring, mutation_rate)
        mutated_offspring_population.append(mutated_offspring)

    population = mutated_offspring_population
    all_populations.append(population)

    print("\nOffspring (After Mutation):")
    for mutated_offspring in population:
        print(mutated_offspring)

    print("\n-------------------------\n")

best_solution = max(all_populations[-1], key=calculate_fitness)
max_fitness = calculate_fitness(best_solution)

print("Solution (Chromosome with Maximum Fitness):", best_solution)
print("Maximum Fitness Value:", max_fitness)
