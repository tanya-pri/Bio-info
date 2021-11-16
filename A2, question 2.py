n = int(input())
m = int(input())
k = 1
offspring = 0
adults = 1

for i in range(2, n):
    newOffspring = adults*k
    adults += offspring
    adults -= i // m
    offspring = newOffspring


print(offspring + adults)