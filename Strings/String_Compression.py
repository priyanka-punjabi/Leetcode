class Solution:
    def compress(self, chars) :
        new_string = ''
        curr = chars[0]
        cnt = 1
        for ele in range(1, len(chars)):
            if chars[ele] == curr:
                cnt += 1
            else:
                if cnt > 1:
                    new_string += curr + str(cnt)
                else:
                    new_string += curr
                curr = chars[ele]
                cnt = 1
        if cnt > 1:
            new_string += curr + str(cnt)
        else:
            new_string += curr
        chars.clear()
        chars.extend(list(new_string))
        return len(new_string)


x = Solution()
chars = ["a","a","a","b","b","a","a"]
print(x.compress(chars))