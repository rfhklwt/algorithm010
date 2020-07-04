#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        m, n = len(board), len(board[0])
        dir = [(-1, -1), (0, -1), (1, -1),
               (-1, 0), (1, 0),
               (-1, 1), (0, 1), (1, 1)]
        # 起始点(i, j)放进去dfs
        self.dfs(board, m, n, i, j, dir)
        return board

    def dfs(self, board, m, n, i, j, dir):
        # 当前方块不空，结束递归
        if board[i][j] != 'E':
            return
        mine_count = 0
        # 计算方块周围雷的数量
        for d in dir:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':
                mine_count += 1
        # 假如方块旁边有雷，返回雷的数量
        if mine_count:
            board[i][j] = str(mine_count)
            return
        # 假如雷的数量为0，返回B，然后对身边的方块再递归
        else:
            board[i][j] = 'B'
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n:
                    self.dfs(board, m, n, ni, nj, dir)

# @lc code=end

