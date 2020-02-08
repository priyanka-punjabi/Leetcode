import sys


class Solution:
    def myAtoi(self, str) :
        print(sys.maxsize)
        str = str.strip(' ')
        res = ''
        maxint = 2147483648;
        if str[0].isdigit() or str[0] == '-' or str[0] == '+':
            for ele in range(len(str)):
                if (str[ele] == '-') and ele == 0:
                    res = '-'
                    continue
                if str[ele].isdigit():
                    res += str[ele]
                else:
                    if res != '' and int(res) <= sys.maxsize:
                        return int(res)
                    else:
                        return 0
        if res != '' and int(res) <= sys.maxsize - 1:
            return int(res)
        else:
            return 0


x = Solution()
str = "-91283472332"
print(x.myAtoi(str))