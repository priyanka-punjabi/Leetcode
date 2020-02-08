import random
class Solution:
    def __init__(self, nums):
        self.original_arr, self.shuffle_arr = [], []
        self.original_arr.extend(nums)
        self.shuffle_arr.extend(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.shuffle_arr = []
        self.shuffle_arr.extend(self.original_arr)
        return self.shuffle_arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        if len(self.shuffle_arr) == 0:
            return []
        for ele in range(len(self.shuffle_arr)):
            idx = random.randint(0, len(nums) - 1)
            temp = self.shuffle_arr[ele]
            self.shuffle_arr[ele] = self.shuffle_arr[idx]
            self.shuffle_arr[idx] = temp
        return self.shuffle_arr

# Your Solution object will be instantiated and called as such:
nums = [1,2,3]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)