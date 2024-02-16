import deffinition
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

num_pop = 500
num_genes = 100

plot_fitness = []
plot_gen = []

generation = 1
population = []
found = False

for x in range(num_pop):  # initialize first population
    empty_chromosome = deffinition.create_crom()
    population.append(empty_chromosome)

while not found:

    # sort list with lowest finest first
    population = deffinition.sort_strings_by_fitness(population)

    if generation == num_genes:  # break the while loop condition
        found = True
        break

    new_generation = deffinition.create_offspring(population)

    population = new_generation

    plot_fitness.append(deffinition.cal_volume_fitness(population[0]))
    plot_gen.append(generation)

    generation = generation + 1

fig, ax = plt.subplots()
ax.plot(plot_gen, plot_fitness)
# Change x-axis and y-axis tick spacing
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=5))  # x-axis ticks at multiples of 2
ax.yaxis.set_major_locator(ticker.MultipleLocator(base=0.1))  # y-axis ticks at multiples of 0.5
plt.xlabel("Generations")
plt.ylabel("Price pr m^3")

plt.grid()
plt.show()
print("Box dimensjons x y z: ", population[0])
print("Gen: ", generation)
print("BOX volume m^3: ", deffinition.cal_volume(population[0]) / 1000000)  # cm^3 to m^3
print("BOX price: ", deffinition.cal_fitness(population[0]) / 10000)
