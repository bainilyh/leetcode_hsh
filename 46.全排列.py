#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, used, trace = [], [False] * len(nums), []
        def dfs(nums):
            if len(trace) == len(nums):
                res.append(list(trace))
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                trace.append(nums[i])
                used[i] = True
                dfs(nums)
                trace.pop()
                used[i] = False
        dfs(nums)
        return res
        
# @lc code=end

