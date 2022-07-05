import knapsackWithRepetition
import knapsack

print ("Example from slides:")
print ("With repetition:")
print (knapsackWithRepetition.knapsack(10, [8, 6, 3], [20, 15, 8]))
print ("Without repetition:")
print (knapsack.knapsack(10, [8, 6, 3], [20, 15, 8]))
#print (knapsack.knapsack(100, [8, 6, 3], [20, 15, 8]))

print ("Example from textbook:")
print ("With repetition:")
print (knapsackWithRepetition.knapsack(10, [6, 3, 4, 2], [30, 14, 16, 9]))
print ("Without repetition:")
print (knapsack.knapsack(10, [6, 3, 4, 2], [30, 14, 16, 9]))
#print (knapsack.knapsack(100, [6, 3, 4, 2], [30, 14, 16, 9]))
