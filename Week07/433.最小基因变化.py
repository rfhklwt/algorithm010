#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    import collections
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 双向bfs首先要检查end是不是在bank里面，不然会出问题
        bank = set(bank)
        if end not in bank: return -1
        LUT = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        front, back = {start}, {end}
        step = 0
        while front:
            step += 1
            new_set = set()
            for node in front:
                for i, c in enumerate(node):
                    for char in LUT[c]:
                        new = node[:i] + char + node[i + 1:]
                        if new in back:
                            return step
                        if new in bank:
                            new_set.add(new)
                            bank.discard(new)
            front = new_set
            if len(front) > len(back):
                front, back = back, front
        return -1

# @lc code=end
