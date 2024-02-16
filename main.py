import deffinition
import matplotlib.pyplot as plt

num_pop = 100
num_genes = 50
Best_cost_val = float('inf')
Best_cost = []
plot_fitness = []
plot_gen = []
generation = 1
population = []
found = False

for x in range(num_pop):  # initialize first population
    empty_chromosome = deffinition.create_crom()
    population.append(empty_chromosome)

while not found:

    population = deffinition.sort_strings_by_fitness(population)  # sort list with lowest finest first
    if Best_cost_val > deffinition.cal_volume_fitness(population[0]):
        Best_cost_val = deffinition.cal_volume_fitness(population[0])

    Best_cost.append(Best_cost_val)

    if generation == num_genes:  # break the while loop condition
        found = True
        break

    new_generation = deffinition.create_offspring(population)  # generate the new population

    population = new_generation  # save the new population for next generation.

    generation = generation + 1
    plot_fitness.append(deffinition.cal_volume_fitness(population[0]))  # save the plot data
    plot_gen.append(generation)  # save the plot data

# Plot the findings
fig, ax = plt.subplots()
ax.plot(Best_cost)

plt.xlabel("Generations")
plt.ylabel("Price pr m^3")
plt.grid()
plt.show()
# Print the results
print("Box dimensjons x y z: ", population[0])  # in cm
print("Gen: ", generation)
print("BOX volume m^3: ", deffinition.cal_volume(population[0]) / 1000000)  # cm^3 to m^3
print("BOX price: ", deffinition.cal_fitness(population[0]) / 10000)  # Price
print("Price pr volum: ", deffinition.cal_volume_fitness(population[0]))  # Price
