class Solution:
    def reverseString(self, s) :
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s

x = Solution()
s = ["h","e","l","l","o"]
x.reverseString(s)