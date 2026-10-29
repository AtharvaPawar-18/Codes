import heapq

def h(s, goal):
    return sum(abs(i//3 - goal.index(x)//3) +
               abs(i%3 - goal.index(x)%3)
               for i, x in enumerate(s) if x != 0)

def solve(start, goal):
    pq = [(h(start, goal), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, s = heapq.heappop(pq)

        if g != cost[s]:
            continue

        if s == goal:
            path = []
            while s is not None:
                path.append(s)
                s = parent[s]

            path.reverse()
            for step, state in enumerate(path):
                print("\nStep", step)
                print(state[:3])
                print(state[3:6])
                print(state[6:])

            print("Total moves:", len(path) - 1)
            return

        z = s.index(0)

        for d in [-3, 3, -1, 1]:
            j = z + d

            if 0 <= j < 9 and not (d == -1 and z % 3 == 0) \
                          and not (d == 1 and z % 3 == 2):
                t = list(s)
                t[z], t[j] = t[j], t[z]
                t = tuple(t)
                ng = g + 1

                if ng < cost.get(t, float("inf")):
                    cost[t] = ng
                    parent[t] = s
                    heapq.heappush(pq, (ng + h(t, goal), ng, t))

    print("No solution")

start = tuple(map(int, input("Enter initial state: ").split()))
goal = tuple(map(int, input("Enter goal state: ").split()))
solve(start, goal)
