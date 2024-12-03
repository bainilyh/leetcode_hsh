#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, trace = [], []
        nums.sort()
        def dfs(nums, start):
            res.append(list(trace))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                trace.append(nums[i])
                dfs(nums, i + 1)
                trace.pop()
        dfs(nums, 0)
        return res
    
        
# @lc code=end

