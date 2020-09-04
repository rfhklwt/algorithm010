# Dijkstra问题专栏
## 概念解释
关于Dijksta的解释，可以移步[这里](https://www.bilibili.com/video/BV1mt411i7DX?from=search&seid=16987134798760117436)
## 模板
```python
def dijkstra(graph, start, end):
    # 创建一个优先队列
    pq = [(0, start)]
    # 已经访问过的点
    seen = {}
    while pq:
        distance, node = heapq.heappop(pq)
        # 找到了终点
        if node == end:
            return distance
        if node in seen: continue
        # 把当前点设置为已访问
        seen.add(node)
        for nei, d in graph[node]:
            heapq.heappush(pq, (distance + d, nei))

```
### [LC 743. Network Delay Time](https://leetcode-cn.com/problems/network-delay-time/)
```python
class Solution:
    from collections import defaultdict
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        pq = [(0, K)]
        # seen里面存源点到每一个结点的最短路径
        seen = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node not in seen:
                seen[node] = d
                for nei, d2 in graph[node]:
                    heapq.heappush(pq, (d + d2, nei))
        return max(seen.values()) if len(seen) == N else -1
```

### [LC 787. Cheapest Flights Within K Stops](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops/)
```python
class Solution:
    from collections import defaultdict
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        pq = [(0, 0, src)]
        while pq:
            cost, step, node = heapq.heappop(pq)
            if node == dst:
                return cost
            if step <= K:
                for nei, paid in graph[node]:
                    heapq.heappush(pq, (cost + paid, step + 1, nei))
        return -1
```
#### 细节分析
* 这里之所以不加seen是因为，有可能得到的最小的价值是不满足题意的，即得到了最小价值，但是经过的中转站是大于k的，这时候就需要类似回溯那样，重新遍历之前遍历过的值，因此不能加seen
* 另外，由于题目已经表明航班没有重复，且不存在环路，因此可以不必担心没有seen带来的问题。
### [LintC 788. Maze II](https://www.lintcode.com/problem/the-maze-ii/description)
>* 在迷宫中有一个球，里面有空的空间和墙壁。球可以通过滚上，下，左或右移动，但它不会停止滚动直到撞到墙上。当球停止时，它可以选择下一个方向。<br>
>* 给定球的起始位置，目标和迷宫，找到最短距离的球在终点停留。距离是由球从起始位置(被排除)到目的地(包括)所走过的空空间的数量来定义的。如果球不能停在目的地，返回-1。<br>
>* 迷宫由二维数组表示。1表示墙和0表示空的空间。你可以假设迷宫的边界都是墙。开始和目标坐标用行和列索引表示。

```python
import heapq


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """


    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        if not m or not n:
            return -1
        pq = [(0, start[0], start[1])]
        seen = set()
        while pq:
            d, i, j = heapq.heappop(pq)
            # 遇到终点就可以返回
            if [i, j] == destination:
                return d
            # 跳过已经检索的点
            if (i, j) in seen: continue
            seen.add((i, j))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i, j
                l = 0
                while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                    x += dx
                    y += dy
                    l += 1
                heapq.heappush(pq, (d + l, x, y))
        return -1
```

### [LC 407. Trapping Rain Water II](https://leetcode-cn.com/problems/swim-in-rising-water/)
```python
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        pq = [(grid[0][0], 0, 0)]
        res = grid[0][0]
        seen = set()
        while pq:
            d, i, j = heapq.heappop(pq)
            res = max(res, d)
            if (i, j) == (N - 1, N - 1):
                return res
            if (i, j) in seen: continue
            seen.add((i, j))
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < N and 0 <= y < N:
                    heapq.heappush(pq, (grid[x][y], x, y))
```
### [](https://leetcode-cn.com/problems/trapping-rain-water-ii/)