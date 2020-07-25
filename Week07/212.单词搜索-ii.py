#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 构建字典树
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True
        # 2. dfs
        def search(i, j, node, pre, visited):
            if '#' in node:
                res.add(pre)
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < h and 0 <= nj < w and (ni, nj) not in visited and board[ni][nj] in node:
                    search(ni, nj, node[board[ni][nj]], pre + board[ni][nj], visited | {(ni, nj)})
        res, h, w = set(), len(board), len(board[0])

        # 3. 遍历整个数组
        for i in range(h):
            for j in range(w):
                if board[i][j] in trie:
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)

# @lc code=end

