#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)
        
# @lc code=end

