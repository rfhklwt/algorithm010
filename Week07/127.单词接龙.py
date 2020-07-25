#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
class Solution:
    import collections
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        LUT = collections.defaultdict(list)
        L = len(beginWord)
        for word in wordList:
            for i in range(L):
                LUT[word[:i] + '*' + word[i + 1:]] += word,

        front, back, visited = {beginWord}, {endWord}, {beginWord, endWord}
        step = 1
        while front:
            step += 1
            # 把下一层所有节点都放到next_set里面
            next_set = set()
            for node in front:
                for i in range(L):
                    new = node[:i] + '*' + node[i + 1:]
                    for word in LUT[new]:
                        if word in back:
                            return step
                        if word not in visited:
                            next_set.add(word)
                            visited.add(word)
            front = next_set
            if len(front) > len(back):
                front, back = back, front
        return 0
# @lc code=end
