#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.mergeSort(nums)
        return self.count

    def mergeSort(self, ret):
        len_ret = len(ret)
        if len_ret > 1:
            mid = len_ret // 2
            L = ret[:mid]
            R = ret[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            # 左右数组的长度
            len_L, len_R = mid, len_ret - mid
            i = j = 0

            # 求count
            while i < len_L and j < len_R:
                if L[i] > 2 * R[j]:
                    self.count += len_L - i
                    j += 1
                else:
                    i += 1
            # 接下来是标准的归并流程，记得把i,j初始化
            i = j = k = 0
            while i < len_L and j < len_R:
                if L[i] < R[j]:
                    ret[k] = L[i]
                    i += 1
                else:
                    ret[k] = R[j]
                    j += 1
                k += 1
            # 假如还剩下
            while i < len_L:
                ret[k] = L[i]
                i += 1
                k += 1
            while j < len_R:
                ret[k] = R[j]
                j += 1
                k += 1

# @lc code=end
