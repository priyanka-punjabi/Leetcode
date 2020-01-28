class Solution:
    def balancedStringSplit(self, s):
        balance = 0
        charCount = 0
        for i in range(len(s)):
            if s[i] == 'R':
                charCount += 1
            else:
                charCount -= 1
            if charCount == 0:
                balance += 1
        return balance

x = Solution()
s = 'RLRRLLRLRL'
print(x.balancedStringSplit(s))