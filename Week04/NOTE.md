# Week04总结


## 深入理解二分法
前提条件：
- 目标函数单调性（单调递增或者递减）
- 存在上下界（bounded）
- 能够通过索引访问（index accessible）

时间复杂度：O(logn)

代码模板：
```Python
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

> 如何识别二分查找？
每次需要查找集合中的索引或元素时，都应该考虑二分查找。如果集合是无序的，我们可以总是在应用二分查找之前先对其进行排序。

**二分查找一般由三个主要部分组成：**

1. 预处理 -- 如果集合未排序，则进行排序。

2. 二分查找 -- 使用循环或递归在每次比较后将查找空间划分为两半。

3. 后处理 -- 在剩余空间中确定可行的候选者。

#### 2 个二分查找模板

> **模板#1**
```Python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
```
模板 #1 是二分查找的最基础和最基本的形式。这是一个标准的二分查找模板。模板 #1 用于查找可以通过访问数组中的单个索引来确定的元素或条件。

**关键属性**
- 二分查找的最基础和最基本的形式。
- 查找条件可以在不与元素的两侧进行比较的情况下确定（或使用它周围的特定元素）。
- 不需要后处理，因为每一步中，你都在检查是否找到了元素。如果到达末尾，则知道未找到该元素。

> 初始条件：left = 0, right = length-1 <br>
> 终止：left > right <br>
> 向左查找：right = mid-1 <br>
> 向右查找：left = mid+1 <br>

> **[x 的平方根](https://leetcode-cn.com/problems/sqrtx/)** <br>
> 计算并返回 x 的平方根，其中 x 是非负整数。 <br>
> 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 <br>
代码如下：
```Python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
```
这里的一个注意点是返回的为什么是left - 1呢，因为整个循环，left都是不断靠近x的，假如$\sqrt{x}$不是整数，那么当循环运行到到left < $\sqrt{x}$ < right$~$(比如2 < 2.82 < 3)。此时的left就是x的开根号的整数值了。之后它会再加一，就会越过$\sqrt{x}$，因此，最后的返回就应该是left - 1。
#### 训练题目:
#### [guess-number-higher-or-lower](https://leetcode-cn.com/problems/guess-number-higher-or-lower/)
#### [search-in-rotated-sorted-array](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

> **模板#2**
```Python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if left != len(nums) and nums[left] == target:
        return left
    return -1
```
模板 #2 是二分查找的高级模板。它用于查找需要访问数组中当前索引及其直接右邻居索引的元素或条件。

**关键属性**
- 一种实现二分查找的高级方法。
- 查找条件需要访问元素的直接右邻居。
- 使用元素的右邻居来确定是否满足条件，并决定是向左还是向右。
- 保证查找空间在每一步中至少有 2 个元素。
- 需要进行后处理。 当你剩下 1 个元素时，循环 / 递归结束。 需要评估剩余元素是否符合条件。
> 初始条件：left = 0, right = length <br>
> 终止：left == right <br>
> 向左查找：right = mid <br>
> 向右查找：left = mid+1 <br>


> **[第一个错误的版本](https://leetcode-cn.com/problems/first-bad-version/)** <br>
> 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。 <br>
> 假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。 <br>
> 你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
代码如下：
```Python
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n + 1
        while left < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid
        return left
```
可以想象有这样的数组[True, True, ..., False, False]。当你确定mid的位置是True的时候，那么答案肯定在mid的右边，所以left = mid + 1；而当你确定mid的位置是False的时候，答案却不一定在mid的左边，因为有可能当前的位置就是第一个False出现的位置，故right = mid。当left == right的时候，就说明这个位置就是第一个Fasle的位置。

> **[在排序数组中查找元素的第一个和最后一个位置](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/)** <br>
> 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 <br>
> 你的算法时间复杂度必须是 O(log n) 级别。 <br>
> 如果数组中不存在目标值，返回 [-1, -1]。 <br>
代码如下：
```Python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(n):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] == n:
                    right = mid
                elif nums[mid] < n:
                    left = mid + 1
                else:
                    right = mid
            return left
        first = search(target)
        return [first, search(target + 1) - 1] if target in nums[first: first + 1] else [-1, -1]
```
这道题我们把问题分成两步，第一步对于给定target，如何求出它的最左边界；第二步，对于给定target，如何求出它的最右边界。首先，在探索最左边界的时候，当mid等于target的时候，把right收缩到mid值，因为此时的mid 值可能是最左边界，也可能不是，无论哪种情况，我们都需要把边界收缩到mid的左边；当mid小于target的时候，mid肯定不会是最左边界，把left收缩到mid + 1；当mid 大于target的时候，把right收缩到mid（这里不收缩到mid - 1是因为可能mid - 1 < target < mid，而我们希望在找不到target的时候把位置定位到比target大的数的最左边界）。<br>
而对于第二步，我们可以把求某个数的最右边界变化为求比某个数大的那个数的最左边界。这样一来就可以采用递归的思路去解。<br>
>另外，最后一句采用target in nums[first: first + 1]而不是target == nums[first]是为了防止越界查找这一情况。

#### 训练题目:
#### [find-peak-element](https://leetcode-cn.com/problems/find-peak-element/)
#### [find-minimum-in-rotated-sorted-array](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)


> 题目：使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
分析：查找中间无序的地方，其实也就是查找半有序数组的最小值，故代码如下：
```Python
class Solution:
    def findNoneOrder(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
```

**参考链接：**
https://leetcode-cn.com/explore/learn/card/binary-search/212/template-analysis/847/