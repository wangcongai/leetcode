class Solution(object):
    def center_spread(self,s,size,left,right):
        """中心扩散寻找回文字符串
        :param s: 字符串
        :param size: 字符串的长度
        :param left: 开始寻找左边的位置
        :param right: 开始寻找右边的位置
        :return: 回文字符串,回文字符串的长度
        """
        i = left
        j = right
        #保证在寻找的过程中不发生越界,而且左右两个字符要相等
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i+1:j],j-i-1

    def longestPalindrome(self,s):
        size = len(s)
        if size < 2:
            return s
        s_palindrome = s[0]
        max_len = 0
        for i in range(size):
            #当回文字符串是奇数的时候
            odd_palindrome,odd_len = self.center_spread(s,size,i,i)
            #当回文字符串是偶数的时候
            even_palindrom,even_len = self.center_spread(s,size,i,i+1)
            #获取最长的回文字符串
            cur_palindrome = odd_palindrome if odd_len > even_len else even_palindrom
            #更新最长的回文字符串
            if len(cur_palindrome) > max_len:
                s_palindrome = cur_palindrome
                max_len = len(cur_palindrome)

        return s_palindrome


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("babad"))