import random

def perform_crossover(parent1, parent2):
    # Select random crossover points
    crossover_point1 = int(random.random() * len(parent1))
    crossover_point2 = int(random.random() * len(parent1))
    
    # Ensure the first crossover point is before the second crossover point
    start_point = min(crossover_point1, crossover_point2)
    end_point = max(crossover_point1, crossover_point2)

    print("Start Point: {}\tEnd Point: {}".format(start_point, end_point))
    
    # Perform crossover between the parents
    offspring1 = parent1[:start_point] + parent2[start_point:end_point] + parent1[end_point:]
    offspring2 = parent2[:start_point] + parent1[start_point:end_point] + parent2[end_point:]
    
    return offspring1, offspring2


def main():
    parent1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    parent2 = ['a', '0', 'b', 'c', 'd', 'e', 'f', 'g']

    for i in range(3):
        print("Iteration", i + 1)
        
        # Perform crossover
        offspring1, offspring2 = perform_crossover(parent1, parent2)

        # Print the resulting offspring
        print("Offspring 1:", offspring1)
        print("Offspring 2:", offspring2)

        print("\n")


if __name__ == '__main__':
    main()
