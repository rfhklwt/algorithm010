#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Time O(N) for one iteration
        # Space O(1)
        five, ten = 0, 0
        for i in bills:
            # 如果给了5块
            if i == 5:
                five += 1
            # 如果给了10块
            elif i == 10:
                five, ten = five - 1, ten + 1
            # 如果给了20块
            else:
                # 手上有10块
                if ten > 0:
                    five, ten = five - 1, ten - 1
                # 手上没10块
                else:
                    five = five - 3
            if five < 0:
                return False
        return True


# @lc code=end

