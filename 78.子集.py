#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, trace = [], []
        def dfs(nums, start):
            res.append(list(trace))
            for i in range(start, len(nums)):
                trace.append(nums[i])
                dfs(nums, i + 1)
                trace.pop()
        dfs(nums, 0)
        return res
        
# @lc code=end

