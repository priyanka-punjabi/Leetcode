class Solution:
    def transformArray(self, arr) :
        for ele in range(1, len(arr) - 1):
            temp_arr = []
            temp_arr.extend(arr)
            for item in range(1, len(arr) - 1):
                if arr[item] < arr[item - 1] and arr[item] < arr[item + 1]:
                    temp_arr[item] += 1
                elif arr[item] > arr[item - 1] and arr[item] > arr[item + 1]:
                    temp_arr[item] -= 1
            arr.clear()
            arr.extend(temp_arr)
        return arr


x = Solution()
arr = [2, 1, 2, 1, 1, 2, 2, 1]
x.transformArray(arr)