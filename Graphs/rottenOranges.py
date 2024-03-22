'''
994. Rotting Oranges
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Time complexity: O(rows * cols) -> each cell is visited at least once
Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue
'''
class Solution:
    def orangesRotting(self, grid):
        rotten = []
        fresh = 0
        adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Adjacent Neighbors
        rows = len(grid)
        cols = len(grid[0])

        # Get all rotten oranges and count of the fresh oranges
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0

        # Iterate until all rotten oranges are traversed or no fresh oranges are left
        while len(rotten) > 0 and fresh > 0:

            # Increment the minute
            minutes += 1

            # In the current minute, for each rotten orange, check it's neighboring orange
            for _ in range(len(rotten)):
                rot = rotten.pop(0)
                for adj in adjacent:
                    newx, newy = rot[0] + adj[0], rot[1] + adj[1]

                    # Skip if newx or newy is out of range of the grid (-1 or n/m)
                    if newx < 0 or newx == rows or newy < 0 or newy == cols:
                        continue

                    # Skip if the newx,newy cell is already rotten or has no oranges
                    if grid[newx][newy] == 0 or grid[newx][newy] == 2:
                        continue

                    # If newx,newy is a fresh orange, mark it as rotten, add it to rotten list and update fresh count
                    grid[newx][newy] = 2
                    rotten.append((newx, newy))
                    fresh -= 1

        if fresh > 0:
            return -1
        return minutes

input = [[2,1,1],[1,1,0],[0,1,1]]
obj = Solution()
print(obj.orangesRotting(input))