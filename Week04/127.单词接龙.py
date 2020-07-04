#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    import collections
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        LUT = collections.defaultdict(list)
        L = len(endWord)
        for word in wordList:
            for i in range(L):
                LUT[word[:i] + '*' + word[i + 1:]].append(word)
        queue = collections.deque()
        queue.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)
        while queue:
            node, step = queue.popleft()
            if node == endWord:
                return step
            for i in range(L):
                new = node[:i] + '*' + node[i + 1:]
                for word in LUT[new]:
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, step + 1))
        return 0
# @lc code=end

