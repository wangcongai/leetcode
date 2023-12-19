class Solution:
    def largestRectangleArea(self, inputs: list) -> int:
        n = len(inputs)
        right_p, ans = 0, 0
        for left_p in range(n):
            right_p = left_p
            while right_p <= n-1:
                width = (right_p - left_p + 1)
                height = min(inputs[left_p: right_p+1])
                area = width * height
                ans = max(area, ans)
                right_p += 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    input_heights = [2, 1, 5, 6, 2, 3]
    print(solution.largestRectangleArea(input_heights))