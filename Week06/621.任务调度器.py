#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_num = list(collections.Counter(tasks).values())
        # 同类型最多任务的个数
        row = max(task_num)
        # 最多任务个数有多少
        last_col = task_num.count(row)
        return max(len(tasks), (row - 1) * (n + 1) + last_col)


# @lc code=end

