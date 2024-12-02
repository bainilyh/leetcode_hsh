#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, trace = [], []
        def dfs(n, start, k):
            if len(trace) == k:
                res.append(list(trace))
                return
            for i in range(start, n + 1):
                trace.append(i)
                dfs(n, i + 1, k)
                trace.pop()
        dfs(n, 1, k)
        return res
        
# @lc code=end

