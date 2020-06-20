#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, c in enumerate(nums):
      new_target = target - c
      if new_target in seen:
        return [seen[new_target], i]
      else:
        seen[c] = i

# @lc code=end

