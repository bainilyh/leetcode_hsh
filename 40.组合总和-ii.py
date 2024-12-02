#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, trace = [], []
        global tmp
        tmp = 0
        candidates.sort()
        def dfs(nums, start):
            global tmp
            if tmp == target:
                res.append(list(trace))
                return
            if tmp > target:
                return # 减枝!!! TODO 
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                trace.append(nums[i])
                tmp += nums[i]
                dfs(nums, i + 1)
                trace.pop()
                tmp -= nums[i]
        dfs(candidates, 0)
        return res
        
                
        
# @lc code=end

