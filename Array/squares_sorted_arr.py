class Solution:
    def sortedSquares(self, A) :
        temp = []
        temp.extend(A)
        for ele in range(len(A)):
            A[ele] = A[ele] * A[ele]
        for item in range(len(A)):
            for ele in range(len(A) - 1):
                if A[ele] > A[ele + 1]:
                    temp = A[ele]
                    A[ele] = A[ele+1]
                    A[ele+1] = temp
        return A

x = Solution()
A = [-4,-1,0,3,10]
print(x.sortedSquares(A))