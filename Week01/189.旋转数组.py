#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. 暴力法：逐一旋转, Time = O(n*k), Space = O(1)
        # for i in range(k):
        #    pre = nums[-1]
        #    for j in range(len(nums)):
        #        nums[j], pre = pre, nums[j]
        # 2. Space = O(n)

        # n = len(nums)
        # step = k % n
        # back = nums[0: n - k]
        # front = nums[n - k: n]
        # nums[:] = front + back

        # 3. Space = O(1)
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]



# @lc code=end

