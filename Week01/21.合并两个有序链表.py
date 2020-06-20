#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = self
        p1, p2 = l1, l2
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                prev.next, prev, l1 = l1, l1, l1.next
            else:
                prev.next, prev, l2 = l2, l2, l2.next
        if l1 is None:
            prev.next = l2
        elif l2 is None:
            prev.next = l1
        return self.next


# @lc code=end

