#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] 矩形区域不超过 K 的最大数值和
#

# @lc code=start
class Solution:
    import bisect
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        # 左边界
        for left in range(col):
            # 初始化nums（这个nums就是我们后面要用来求接近K的）
            nums = [0] * row
            # 右边界
            for right in range(left, col):
                for i in range(row):
                    nums[i] += matrix[i][right]
                # 在left, right为边界下的矩阵(在这里已经降维成1维的nums了)，
                # 下面这段求不超过k的最大数值和（跟前面我们讲的如出一辙）
                # 用来存cum的array（已排序）
                array = [0]
                cum = 0
                for num in nums:
                    cum += num
                    loc = bisect.bisect_left(array, cum - k)
                    if loc < len(array):
                        res = max(res, cum - array[loc])
                    bisect.insort(array, cum)
        return res


# @lc code=end

