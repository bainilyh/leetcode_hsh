#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2s = {'2':'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs','8': 'tuv', '9': 'wxyz'}
        res, trace = [], []
        def dfs(digits, start):
            if not digits:
                return res
            if len(trace) == len(digits):
                res.append(''.join(trace))
                return
            d = digits[start]
            s = d2s[d]
            for i in range(len(s)):
                trace.append(s[i])
                dfs(digits, start + 1)
                trace.pop()
        dfs(digits, 0)
        return res
        
# @lc code=end

