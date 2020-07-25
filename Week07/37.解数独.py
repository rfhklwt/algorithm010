#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        row, col, box = collections.defaultdict(set), collections.defaultdict(
            set), collections.defaultdict(set)
        seen = collections.deque()

        # 首先把所有的row, col, box和seen都初始化好, 待填入的空格加入到seen中
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    seen.append((i, j))
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i // 3, j // 3)].add(board[i][j])

        # 深度优先搜索
        def dfs():
            # Terminator
            if not seen:
                return True
            r, c = seen[0]
            t = (r // 3, c // 3)
            for num in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                # 不造成冲突
                if num not in row[r] and num not in col[c] and num not in box[t]:
                    board[r][c] = num
                    row[r].add(num)
                    col[c].add(num)
                    box[t].add(num)
                    seen.popleft()
                    if dfs():
                        return True
                    else:
                        # 回溯，撤回操作
                        board[r][c] = '.'
                        row[r].discard(num)
                        col[c].discard(num)
                        box[t].discard(num)
                        seen.appendleft((r, c))
            return False
        dfs()
# @lc code=end