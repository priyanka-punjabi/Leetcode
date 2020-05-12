def twoCitySchedCost(costs):
    costs.sort(key=lambda x: x[0] - x[1])
    total = 0
    n = len(costs) // 2

    for i in range(n):
        total += costs[i][0] + costs[i + n][1]
    return total

if __name__ == '__main__':
    costs = [[10,20],[30,200],[400,50],[30,20],[400,50],[30,20]]
    print(twoCitySchedCost(costs))