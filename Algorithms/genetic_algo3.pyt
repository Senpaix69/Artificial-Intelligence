import random


def fitnessP1(P1):
    return abs(sum(P1) - 36)

def fitnessP2(X):
    fit = 1
    for i in X:
        fit *= i
    return abs(fit - 360)


def crossover(p1, p2):
    ind = random.randint(0, len(p1) - 1)
    new_gen1 = p1.copy()
    new_gen2 = p2.copy()
    new_gen1[ind], new_gen2[ind] = new_gen2[ind], new_gen1[ind]
    return new_gen1, new_gen2


pile1 = [[1, 2, 3, 4, 5]]
pile2 = [[6, 7, 8, 9, 10]]

for i in range(6):
    pile1 = sorted(pile1, key=fitnessP1, reverse=True)
    pile2 = sorted(pile2, key=fitnessP2)

    print("Iteration", i + 1)

    newGen1, newGen2 = crossover(pile1[0], pile2[0])
    print("Offspring1:", newGen1)
    print("Offspring2:", newGen2)
    fit1 = fitnessP1(newGen1)
    fit2 = fitnessP2(newGen2)
    print("Fitness Pile1:", fit1)
    print("Fitness Pile2:", fit2)
    print()

    pile1.append(newGen1)
    pile2.append(newGen2)


print("All Piles1: ", pile1)
print("All Piles2: ", pile2)
    
