# Week07总结

Trie数代码模板：
```Python
# Python
class Trie(object):

	def __init__(self):
		self.root = {}
		self.end_of_word = "#"

	def insert(self, word):
		node = self.root
		for char in word:
			node = node.setdefault(char, {})
		node[self.end_of_word] = self.end_of_word

	def search(self, word):
		node = self.root
		for char in word:
			if char not in node:
				return False
			node = node[char]
		return self.end_of_word in node

	def startsWith(self, prefix):
		node = self.root
		for char in prefix:
			if char not in node:
				return False
			node = node[char]
		return True
```

## [Word Search II](https://leetcode-cn.com/problems/word-search-ii/)
```Python
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
```

> 时间复杂度分析
假设单词的最大长度为L,那么从一个单元格开始，最初最多可以探索4个方向，最坏的情况下假定所有方向都是有效的，在接下来的search中最多只会有3个方向可以探索（因为不能重复使用）。因此在search期间，最多遍历$4\cdot3^{L - 1}$。因此总的时间复杂度应该是$O(h * w * 4 * 3 ^ {L - 1})$，其中h和w分别是board的长和宽。
> 空间复杂度分析
算法消耗的主要空间是我们构建的 Trie 数据结构。在最坏的情况下，如果单词之间没有前缀重叠，则 Trie 将拥有与所有单词的字母一样多的节点。故为O(N)