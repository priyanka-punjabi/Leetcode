from _collections import defaultdict
class Solution:
    def firstUniqChar(self, s) :
        chardict = defaultdict()
        for char in range(len(s)):
            if s[char] not in chardict:
                chardict[s[char]] = []
            chardict[s[char]].append(char)
        for k,v in chardict.items():
            if len(v) == 1:
                return v[0]
        return -1


x = Solution()
s = 'leetcode'
print(x.firstUniqChar(s))