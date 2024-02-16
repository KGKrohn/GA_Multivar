import numpy as np
import random

x_wall_price_sqr_cm = 0.6
y_wall_price_sqr_cm = 0.8
flat_price_sqr_cm = 0.1


mutation_rate = 0.002
var_min = 1
var_max = 1000


def create_genes():#make the gene
    number = random.randint(1, 1000)
    return number


def create_crom(): # create the chromosome
    x = create_genes()
    y = create_genes()
    z = create_genes()
    vec = [x, y, z]
    return vec


def cal_fitness(box_dim): # calculate the price of the walls of the box
    fitness = ((box_dim[0] * box_dim[1] * flat_price_sqr_cm) * 2  # x * y * roof/floor
               + (box_dim[0] * box_dim[2] * x_wall_price_sqr_cm) * 2  # x * z * xWall
               + (box_dim[2] * box_dim[2] * y_wall_price_sqr_cm) * 2)  # y * z * yWall
    return fitness


def cal_volume(box_dim): # calculate the volume
    fitness = box_dim[0] * box_dim[1] * box_dim[2]
    return fitness


def cal_volume_fitness(box_dim):# calculate the Price pr volume fitness
    fitness = cal_fitness(box_dim)/(cal_volume(box_dim))#fitness/vl\olum?? isteden
    return fitness


def crossover(parent1, parent2): # Uniform crossover implementation
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2


def mutation(child): # add the mutation to the variable
    mutated_child = child.copy()
    for i in range(len(mutated_child)):
        if random.random() < mutation_rate:
            mutated_child[i] = random.randint(var_min, var_max)
    return mutated_child


def create_offspring(population): # Make the new population.
    new_generation = []
    while len(new_generation) < len(population):
        parent1 = random.choice(population[:10])
        parent2 = random.choice(population[:10])
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        new_generation.append(child1)
        new_generation.append(child2)
    return new_generation


def sort_strings_by_fitness(list_of_lists): #sort the list based on the best price to volume metric.
    return sorted(list_of_lists, key=lambda x: cal_volume_fitness(x))

