#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 假如矩阵是一维的，之间返回0
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # 当前位置必须是1，不然就不构成正方形了
                if matrix[i][j] == '1':
                    # 假如位于第一行或第一列，正方形就只能是1
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        # 求面积
        return maxSide ** 2

# @lc code=end

