class Solution:
    def addStrings(self, num1, num2) :
        if len(num1) > len(num2):
            diff = len(num1) - len(num2)
            for itr in range(diff):
                num2 = ''.join(('0', num2))
        elif len(num2) > len(num1):
            diff = len(num2) - len(num1)
            for itr in range(diff):
                num1 = ''.join(('0',num1))
        if len(num1) > 0 or len(num2) > 0:
            carry = 0
            sum = ''
            for i in range(len(num1) - 1, -1, -1):
                if carry > 0:
                    temp = int(num1[i]) + int(num2[i]) + carry
                else:
                    temp = int(num1[i]) + int(num2[i])
                if temp > 9:
                    while temp > 9:
                        carry = temp // 10
                        temp = temp % 10
                else:
                    carry = 0
                sum += str(temp)
            if carry > 0:
                sum += str(carry)
            return sum[::-1]



x = Solution()
num2 = '1'
num1 = '9'
print(x.addStrings(num1, num2))