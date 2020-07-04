#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_island += 1
                    self.dfs(grid, i, j)
        return num_island


    def dfs(self, grid, x, y):
        mx, my = len(grid), len(grid[0])
        grid[x][y] = 0
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= i < mx and 0 <= j < my and grid[i][j] == '1':
                self.dfs(grid, i, j)


# @lc code=end

