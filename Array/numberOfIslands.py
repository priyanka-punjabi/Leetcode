def dfs(grid, r, c):
    nr = len(grid)
    nc = len(grid[0])

    if r < 0 or r >= nr or c < 0 or c >= nc or grid[r][c] == 0:
        return

    grid[r][c] = 0
    dfs(grid, r - 1, c)
    dfs(grid, r + 1, c)
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)


def numIslands(grid):
    if len(grid) == 0:
        return 0
    nr = len(grid)
    nc = len(grid[0])
    num_islands = 0
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == 1:
                num_islands += 1
                dfs(grid, i, j)
    return num_islands


input = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
input2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
input3 = []
print(numIslands(input3))
