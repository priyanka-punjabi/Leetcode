class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = ''
        temp_str = ''
        for char in s:
            if char != ' ':
                temp_str += char
            else:
                temp_str = temp_str[::-1]
                new_str += temp_str + ' '
                temp_str = ''
        if temp_str != '':
            temp_str = temp_str[::-1]
            new_str += temp_str
        return new_str.strip()

x = Solution()
S = "Let's take LeetCode contest abc "
print(x.reverseWords(S))