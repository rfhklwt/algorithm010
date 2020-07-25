#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in row[i]:
                        row[i].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in col[j]:
                        col[j].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in box[(i // 3, j // 3)]:
                        box[(i // 3, j // 3)].add(board[i][j])
                    else:
                        return False
        return True
# @lc code=end
