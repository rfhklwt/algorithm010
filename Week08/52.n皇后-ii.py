#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        if n < 1: return 0
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count
    def DFS(self, n, row, col, pie, na):
        # terminator
        if row >= n:
            self.count += 1
        else:
            # 我们用1来表示空位，用0来表示已经被占据
            bits = ~(col | pie | na) & ((1 << n) - 1)
            # 当bits都为0就表示被占据满了
            while bits:
                # 取最低的1(这一步相当于for i in range(n)并且还同时去除了那些不符合条件的i)
                p = bits & -bits
                # 在p位置上放入皇后，所以变为0
                bits &= bits - 1
                # 下探一层
                self.DFS(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)

# @lc code=end

