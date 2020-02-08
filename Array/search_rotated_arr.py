class Solution:
    def search(self, nums, target):
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else:
                return False
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
        return self.bSearch(nums, 0, len(nums) - 1, target)

    def bSearch(self, nums, start, end, target):
        if end >= start:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                return self.bSearch(nums, start, mid - 1, target)
            else:
                return self.bSearch(nums, mid + 1, end, target)
        else:
            return False



x = Solution()
nums = [1,1,1,1,3]
target = 3
print(x.search(nums, target))