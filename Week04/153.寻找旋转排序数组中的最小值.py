#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            # 地板除, mid更靠近left
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                # 最小值在右半边
                left = mid + 1
            else:
                # 最小值在左半边
                # 中值也可能是最小值，故取到mid处
                right = mid
        return nums[left]




# @lc code=end

