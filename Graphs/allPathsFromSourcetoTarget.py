class Solution:
    def allPathsSourceTarget(self, graph):
        N = len(graph)
        def solve(node):
            if node == (N - 1):
                return [[N - 1]]
            ans = []
            for neighbour in graph[node]:
                for path in solve(neighbour):
                    ans.append([node] + path)
            return ans
        return solve(0)

input = [[1,2], [3], [3], []]
obj = Solution()
print(obj.allPathsSourceTarget(input))