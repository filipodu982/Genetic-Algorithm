from random import randint, random
from time import sleep

searchFor = 'filip'                                                             # what string are we looking for
pop = []                                                                        # array storing every member of population
children = []                                                                   # there we append all children
mutationRate = 0.01                                                             # percentage of random mutation in genes
popNum = 200                                                                    # number of members of population
found = False                                                                   # did we find searchFor
generations = 0                                                                 # generations elapsed

# function evaluating how close is 'what' to searchFor
# every letter on a right place adds 1 to the fitness
def calcFitness(what):
    value = 0
    for j in range(len(what)):
        if what[j] == searchFor[j]:
            value += 1
    return (value/float(len(searchFor))*100)                                    # percentage of how close is the string to searchFor

# we make a pool from which parents will be selected
# e.g. if a string has a fitness of 30, it will be added to pool 30 times
# which increases it chances to be picked and reproduced
def createPool(population):
    for i in range(len(population)):
        for j in range(int(fitness[i])):
            pool.append(population[i])

# very important function which makes a child from two parents and adds
# a random mutation to a child
# it picks two arrays, splits them in half and just concatenates them together
def crossover():
    parentA = pool[randint(0, len(pool)-1)]
    parentB = pool[randint(0, len(pool)-1)]
    if parentA == parentB:
        parentB = pool[randint(0, len(pool)-1)]
    child = parentA[0:(len(searchFor)/2)] + parentB[(len(searchFor)/2):len(searchFor)]
    for i in range(len(child)):
        if random() < mutationRate:
            child[i] = chr(randint(97,122))
    return child



# just generting a random population before the main loop
for i in range(popNum):
    buff = []
    for j in range(len(searchFor)):
        buff.append(chr(randint(97,122)))
    pop.append(buff)

# main loop of algorithm
while not found:
    fitness = []
    pool = []

    # appending to fitness array every value of calculated fitness
    for i in range(len(pop)):
        fitness.append(calcFitness(pop[i])+1)
        if ''.join(pop[i]) == searchFor:                                        # if we found searchFof, we print it and how many generations it took to do so
            print ''.join(pop[i])
            print generations
            found = True
            break

    createPool(pop)

    # making a new population
    for i in range(len(pop)):
        pop[i] = crossover()

    # just for show - printing the fittest member of population to see progress
    for i in range(len(fitness)):
        if fitness[i] == max(fitness):
            print ''.join(pop[i])
            break

    generations += 1
    #sleep(0.1) uncomment if you want to see everything clearer
