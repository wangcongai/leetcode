class Solution(object):
    def validate_palindrome(self,s,left,right):
        """判断字符串是否为回文字符串
        :param s:
        :param left:
        :param right:
        :return:
        """
        if len(s) < right and left < 0:
            assert("s length must greater than right,left must greater than or equal to zero")
        while left < right:
            #回文字符串左边和右边字符相等
            if s[left] != s[right]:
                return False
            #移动左边和右边的指针
            left += 1
            right -= 1
        return True

    def longestPalindrome(self,s):
        s_len = len(s)
        if s_len < 2:
            return s
        #用来记录回文字符串
        palindrome_s = s[0]
        #记录回文字符串长度
        max_len = 1
        #遍历字符串中的所有子串
        for i in range(s_len-1):
            for j in range(i+1,s_len):
                if j-i+1 > max_len and self.validate_palindrome(s,i,j):
                    palindrome_s = s[i:j+1]
                    max_len = j - i + 1

        return palindrome_s


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("babad"))