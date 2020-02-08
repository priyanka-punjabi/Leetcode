class Solution:
    def sortArrayByParity(self, A) :
        even, odd = [], []
        for ele in range(len(A)):
            if A[ele] % 2 == 0:
                even.append(A[ele])
            else:
                odd.append(A[ele])
        A.clear()
        A.extend(even)
        A.extend(odd)
        return A