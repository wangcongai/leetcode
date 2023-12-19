from typing import List


class Solution:
    def print_matrix(self, grid):
        for row in grid:
            print(row)

    def dfs(self, grid, r, c):
        # 进入深度遍历，首先将矩阵该元素置0
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        # 上下左右4个方向
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            # 判断边界条件，如果方向之一满足连同要求，则向下搜索
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        # number of rows
        nr = len(grid)
        if nr == 0:
            return 0
        # number of columns
        nc = len(grid[0])

        num_islands = 0
        # 逐行
        for r in range(nr):
            # 逐列
            for c in range(nc):
                # 如果矩阵元素为1，那么就检查元素上下左右（DFS）
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c)

        return num_islands


if __name__ == '__main__':
    grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]

    solution = Solution()
    solution.print_matrix(grid)

    print("联通岛屿数量为：", solution.numIslands(grid=grid))