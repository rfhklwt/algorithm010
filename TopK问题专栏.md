# TopK问题专栏
## 题目描述
* 给定一个未排序的数组，求最大（或者最小）的k个数
## 思路：
* 排序 - O(nlogn)
* 堆排序 - O(nlogK)
* 快排思想 - O(n) (**重点**)

> 这道题在面试中是高频的高频，必须做到闭着眼睛都能写出来。其中堆排序和快排思想是最重要的

## 例题分析
[1. 最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

## 解法一 - 堆排序
* 利用大顶堆来解决，创建一个k个元素的大顶堆hp，接着每次把数组剩余的元素依次放进hp里面，保持hp的个数为k，这样每次从hp里弹出去的就一定是堆中最大的。这样子一次遍历下来，最小的k个元素就一定会在hp里面
* 但是python里面的heapq模块是小顶堆，因此我们可以对数组进行取负值，最后输出结果再取一次负值就能得到我们想要的结果了

```python
class Solution:
    import heapq
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # python是小根堆，所以等价于找最大的k个数
        if k == 0: return []
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for x in arr[k:]:
            if hp[0] < -x:
                heapq.heapreplace(hp, -x)
        return [-x for x in hp]
```

解法二 - 快排思想
> 值得注意的是当遇到极端情况，即nums是顺序数组与倒序数组，此时递归树画出来是链表，时间复杂度是 O(N^2)，特别差，因此，我们会采用随机初始化pivot的元素，这样一来平均复杂度就会是O(n)了
```python
class Solution:
    import random
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0: return []
        n = len(arr)
        left, right = 0, n - 1
        while left <= right:
            index = self.__partition(left, right, arr)
            if index == k:
                return arr[:k]
            elif index < k:
                left = index + 1
            else:
                right = index - 1
        # 还是没找到
        return arr
    def __partition(self, left, right, nums):
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]
        pivot, mark = nums[left], left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[left], nums[mark] = nums[mark], nums[left]
        return mark
```
[2. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

## 解法一 - 堆排序
* 利用大顶堆来解决，创建一个k个元素的大顶堆hp，接着每次把数组剩余的元素依次放进hp里面，保持hp的个数为k，这样每次从hp里弹出去的就一定是堆中最大的。这样子一次遍历下来，最小的k个元素就一定会在hp里面
* 但是python里面的heapq模块是小顶堆，因此我们可以对数组进行取负值，最后输出结果再取一次负值就能得到我们想要的结果了

```python
class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = nums[:k]
        heapq.heapify(hp)
        for x in nums[k:]:
            if x > hp[0]:
                heapq.heapreplace(hp, x)
        return hp[0]
```

解法二 - 快排思想
```python
class Solution:
    import random
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target = n - k
        left, right = 0, n - 1
        while left <= right:
            index = self.__partition(left, right, nums)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            else:
                right = index - 1
    def __partition(self, left, right, nums):
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]
        pivot, mark = nums[left], left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[left], nums[mark] = nums[mark], nums[left]
        return mark
```
