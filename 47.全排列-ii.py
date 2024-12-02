#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, trace = [], []
        used = [False] * len(nums)
        nums.sort()
        def dfs(nums):
            if len(trace) == len(nums):
                res.append(list(trace))
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                trace.append(nums[i])
                used[i] = True
                dfs(nums)
                trace.pop()
                used[i] = False
        dfs(nums)
        return res
                
                    
        
# @lc code=end

