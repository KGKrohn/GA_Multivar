import numpy as np
import random


flat_price_sqr_cm = 0.8
y_wall_price_sqr_cm = 0.5
x_wall_price_sqr_cm = 0.2
mutation_rate = 0.01
var_min = 1
var_max = 5


def create_genes():
    number = random.randint(1, 3)
    return number


def create_crom():
    x = create_genes()
    y = create_genes()
    z = create_genes()
    vec = [x, y, z]
    return vec


def cal_fitness(box_dim):
    fitness = ((box_dim[0] * box_dim[1] * flat_price_sqr_cm) * 2  # x * y * roof/floor
               + (box_dim[0] * box_dim[2] * x_wall_price_sqr_cm) * 2  # x * z * xWall
               + (box_dim[2] * box_dim[2] * y_wall_price_sqr_cm) * 2)  # y * z * yWall
    return fitness


def cal_volume(box_dim):
    fitness = box_dim[0] * box_dim[1] * box_dim[2]
    return fitness


def cal_volume_fitness(box_dim):
    fitness = cal_fitness(box_dim)/(cal_volume(box_dim))#fitness/vl\olum?? isteden
    return fitness


def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2


def mutation(child):
    mutated_child = child.copy()
    for i in range(len(mutated_child)):
        if random.random() < mutation_rate:
            mutated_child[i] += random.randint(var_min, var_max)
    return mutated_child


def create_offspring(population):
    new_generation = []
    while len(new_generation) < len(population):
        parent1 = random.choice(population[:3])
        parent2 = random.choice(population[:4])
        child1, child2 = crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        new_generation.append(child1)
        new_generation.append(child2)
    return new_generation


def sort_strings_by_fitness(list_of_lists):
    return sorted(list_of_lists, key=lambda x: cal_volume_fitness(x))

