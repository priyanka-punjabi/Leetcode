from _collections import defaultdict
class Solution:
    def twoSum(self, nums, target) :
        arr = []
        tempDict = defaultdict()
        for ele in range(len(nums)):
            tempDict[ele] = nums[ele]
        for ele in range(len(nums)):
            if (nums[ele] <= target and target >= 0) or (nums[ele] >= target and target < 0):
                diff = target - nums[ele]
                arr.append(ele)

                for k,v in tempDict.items():
                    if v == diff and k != ele:
                        arr.append(k)
                        return arr
            arr = []

x = Solution()
nums = [-3,-1,-3,1,-5]
target = 0
print(x.twoSum(nums, target))