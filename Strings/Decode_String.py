class Solution:
    def decodeString(self, s) :
        intstack = []
        strstack = []
        new_string = ''
        k = ''
        for ele in range(len(s)):
            if s[ele].isdigit():
                k += str(s[ele])
            elif s[ele] == '[':
                intstack.append(int(k))
                strstack.append(new_string)
                new_string = ''
                k = ''
            elif s[ele] == ']':
                temp = new_string
                new_string = strstack.pop()
                itr = intstack.pop()
                for i in range(itr, 0, -1):
                    new_string += temp
            else:
                new_string += s[ele]
        return new_string



x = Solution()
s = '100[leetcode]'
print(x.decodeString(s))