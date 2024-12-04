#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, trace = [], []
        def dfs(n, left, right):
            if left == right == n:
                res.append(''.join(trace))
            if left < n:
                for i in range(left, n):
                    trace.append('(')
                    dfs(n, left + 1, right)
                    trace.pop()
            if right < left:
                for i in range(right, n):
                    trace.append(')')
                    dfs(n, left, right + 1)
                    trace.pop()
        dfs(n, 0, 0)
        return res
        
# @lc code=end

