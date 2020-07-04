#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution:
    import collections
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # bfs
        # T = O(M * N)
        # M是单词的长度，N是单词表中单词的总数
        if endWord not in wordList:
            return []
        # 生成查找表
        LUT = collections.defaultdict(list)
        L = len(endWord)
        for word in wordList:
            for i in range(L):
                LUT[word[:i] + '*' + word[i + 1:]].append(word)

        queue = collections.deque()
        queue.append((beginWord, [beginWord]))
        res = []

        visited = set()

        while queue:
            new_visited = set()
            # 对于每一层所有的结点
            for _ in range(len(queue)):
                node, path = queue.popleft()
                # 如果该结点是endWord,把path放到res
                if node == endWord:
                    res.append(path)
                #对于该层的某个结点，其下一层的结点数量是，每个字母位置都会变化，但是能变化的数量由LUT来决定，
                # 所以这里用2层循环，第一层是每个字母位置的变化，第二层是可以变化的数量
                for i in range(L):
                    new = node[:i] + '*' + node[i + 1:]
                    for word in LUT[new]:
                        # 结点从来没出现过
                        if word not in visited:
                            # 存入该层的new_visited里
                            new_visited.add(word)
                            # 满足要求的放到queue，即是存入下一层的结点
                            queue.append((word, path + [word]))
            # 这里把上一层的所有结点都放到visited
            visited |= new_visited
        return res



# @lc code=end

