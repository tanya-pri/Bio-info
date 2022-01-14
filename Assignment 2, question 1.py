n = int(input())
k = int(input())
offspring = 0
adults = 1

for i in range(2, n):
    newOffspring = adults*k
    adults += offspring
    offspring = newOffspring


print(offspring + adults)

