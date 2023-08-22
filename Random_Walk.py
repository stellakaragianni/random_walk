import random
import math
import matplotlib.pyplot as plt


def random_walk(steps):
    x, y = 0, 0
    for a in range(steps):
        # Generate random step (up,down,right,left)
        step = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += step[0]
        y += step[1]

    #Euclidean distance formula to measure distance
    distance = math.sqrt(x**2 + y**2)
    return distance

#Num of steps for each iteration
num_steps = [10, 100, 1000, 10000]

for steps in num_steps:
    distances = []
    
    for i in range(100):  #Repeat the experiment 100 times
        distance = random_walk(steps)
        distances.append(distance)

    min_distance = min(distances)
    max_distance = max(distances)
    med_distance = (max_distance + min_distance)/2

    print("Steps: ",steps, "\nMin Distance: ", min_distance, "\nMax Distance:", max_distance, "\nMedium Distance: ", med_distance, "\n")

#Plotting the diagram of distance for 10 steps
steps = 10
distances = []

for j in range(100):
    distance = random_walk(steps)
    distances.append(distance)

plt.plot(distances)
plt.title(f'Distance Diagram for {steps} Steps')
plt.show()
