# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 并查集的做法
        if not board: return []
        m, n = len(board), len(board[0])
        p = [i for i in range(m * n + 1)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        self._union(p, m * n, i * n + j)
                    else:
                        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                                self._union(p, i * n + j, ni * n + nj)
        for i in range(m):
            for j in range(n):
                if self._parent(p, i * n + j) == self._parent(p, m * n):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

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
