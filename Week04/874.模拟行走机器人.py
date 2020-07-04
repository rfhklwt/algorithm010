#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # T = O(M + N)
        # S = O(N)
        i, j, MAX, d = 0, 0, 0, 0
        move = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        obstacles = set(map(tuple, obstacles))
        for command in commands:
            if command == -2:
                d = (d + 1) % 4
            elif command == -1:
                d = (d - 1) % 4
            else:
                dx, dy = move[d]
                while command and (i + dx, j + dy) not in obstacles:
                    i += dx
                    j += dy
                    command -= 1
                MAX = max(MAX, i ** 2 + j ** 2)
        return MAX

# @lc code=end

