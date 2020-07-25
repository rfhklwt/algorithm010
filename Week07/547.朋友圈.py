#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 一共就len(M)个同学，一开始大家都是分开的
        n = len(M)
        p = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self._union(p, i, j)
        return len(set([self._parent(p, i) for i in range(n)]))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p1] = p2
    def _parent(self, p, i):
        root = i
        #即还没找到root
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            i, p[i] = p[i], root
        return root



# @lc code=end
