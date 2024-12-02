#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, trace = [], []
        global curSum
        curSum = 0
        def dfs(nums, target, start):
            global curSum
            if curSum == target:
                res.append(list(trace))
                return
            if curSum > target:
                return 
            for i in range(start, len(nums)):
                trace.append(nums[i])
                curSum += nums[i]
                dfs(nums, target, i) #重点!!!!
                trace.pop()
                curSum -= nums[i]
        dfs(candidates, target, 0)
        return res
                
        
# @lc code=end

