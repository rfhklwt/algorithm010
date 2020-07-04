#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            nums = matrix[mid // n][mid % n]
            if nums == target:
                return True
            elif nums < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end

