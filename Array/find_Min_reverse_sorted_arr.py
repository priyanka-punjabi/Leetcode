class Solution:
    def findMin(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        idx = 0
        flag = True
        if len(nums) > 1:
            while nums[idx] <= nums[idx + 1]:
                idx += 1
                if idx == len(nums) - 1:
                    flag = False
                    break
        if flag:
            nums = nums[idx + 1:] + nums[:idx + 1]
        return nums[0]

x = Solution()
nums = []
print(x.findMin(nums))