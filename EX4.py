
import random

n = int(input("Enter number of cities: "))

dist = []
print("Enter distance matrix:")
for i in range(n):
    dist.append(list(map(int, input().split())))

k = int(input("Enter beam width: "))

def cost(path):
    return sum(dist[path[i]][path[(i + 1) % n]] for i in range(n))

beam = [random.sample(range(n), n)]

for step in range(100):
    candidates = []

    for path in beam:
        for i in range(n):
            for j in range(i + 1, n):
                new = path[:]
                new[i], new[j] = new[j], new[i]
                candidates.append(new)

    candidates = list({tuple(p) for p in candidates})
    candidates.sort(key=cost)
    beam = [list(p) for p in candidates[:k]]

best = min(beam, key=cost)

print("Best tour:", best + [best[0]])
print("Minimum distance:", cost(best))
