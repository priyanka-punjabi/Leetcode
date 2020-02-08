class Solution:
    def intersection(self, nums1, nums2):
        res = []
        for ele in range(len(nums1)):
            if nums1[ele] in nums2 and nums1[ele] not in res:
                res.append(nums1[ele])
        return res