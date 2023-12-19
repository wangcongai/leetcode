from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # left = [−1,0,−1,−1,3,4,5,3]
        # right = [2,2,3,8,7,7,7,8]
        left, right = [0] * n, [0] * n

        # 构建一个从左到右的栈，存贮的是矩形Index，保证这些栈里的矩阵，高度单调递增
        mono_stack = list()
        for i in range(n):
            # 逐个删除栈顶元素，保证栈顶元素的高小于i矩形的高
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            # 将栈顶元素作为i矩形的左侧最大延伸Index
            left[i] = mono_stack[-1] if mono_stack else -1
            # 将i矩形index存入栈（保证了矩阵高度单调递增）
            mono_stack.append(i)

        # 构建一个从右到左的栈，存贮的是矩形Index，保证这些栈里的矩阵，高度单调递增
        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        # 矩阵面积：左右Indext列表的元素相减，作为宽。最后求max（核心逻辑还是暴力解法思想：固定高，求最大宽）
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans


if __name__ == '__main__':
    solution = Solution()
    # input_heights = [2, 1, 5, 6, 2, 3]
    input_heights = [6, 7, 5, 2, 4, 5, 9, 3]
    print(solution.largestRectangleArea(input_heights))