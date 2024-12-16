#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# 解题思路：动态规划
# 1. 创建dp数组,dp[i]表示以nums[i]结尾的最大子数组和
# 2. 状态转移方程：dp[i] = max(nums[i], dp[i-1] + nums[i])
# 3. 最终结果为dp数组中的最大值
#
# 时间复杂度：O(n) - 遍历一次数组
# 空间复杂度：O(n) - 使用dp数组存储中间结果

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 特殊情况处理
        if not nums:
            return 0
            
        n = len(nums)
        # 创建dp数组并初始化
        dp = [0] * n
        dp[0] = nums[0]
        
        # 遍历数组，计算每个位置的最大子数组和
        for i in range(1, n):
            # 状态转移：要么自成一段，要么与前面的最大子数组和相连
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        # 返回dp数组中的最大值
        return max(dp)
        
# @lc code=end
