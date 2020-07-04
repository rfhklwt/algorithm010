# Week03总结


### 二分法v1.0版本(后续更新)
前提条件：
- 目标函数单调性（单调递增或者递减）
- 存在上下界（bounded）
- 能够通过索引访问（index accessible）

时间复杂度：O(logn)

代码模板：
```
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        # find the target!!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

> 题目：使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
分析：查找中间无序的地方，其实也就是查找半有序数组的最小值，故代码如下：
```
class Solution:
    def findNoneOrder(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
```