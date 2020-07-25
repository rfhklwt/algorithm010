#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not len(grid):
            return 0
        m, n = len(grid), len(grid[0])
        p = [i for i in range(m * n + 1)]
        is_water = False
        for i in range(m):
            for j in range(n):
                # 假如是陆地，那么查询它的右边和下边
                if grid[i][j] == '1':
                    if i + 1 < m and grid[i + 1][j] == '1':
                        self._union(p, i * n + j, (i + 1) * n + j)
                    if j + 1 < n and grid[i][j + 1] == '1':
                        self._union(p, i * n + j, i * n + j + 1)
                # 假如是水域，全部都链接到一个虚拟的点
                elif grid[i][j] == '0':
                    # 假如真的有水域，让is_water为True
                    is_water = True
                    self._union(p, m * n, i * n + j)
        if is_water:
            return len(set(self._parent(p, i) for i in range(m * n))) - 1
        else:
            return len(set(self._parent(p, i) for i in range(m * n)))


    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p2] = p1


    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            i, p[i] = p[i], root
        return root

# @lc code=end
