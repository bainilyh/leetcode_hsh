#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# 解题思路:
# 1. 使用动态规划来解决
# 2. 创建dp数组,dp[i]表示爬到第i阶的方法数
# 3. dp[i] = dp[i-1] + dp[i-2]
# 4. 因为每次可以爬1或2个台阶
# 5. 所以到达第i阶的方法 = 从第i-1阶爬1阶 + 从第i-2阶爬2阶
#
# 数据结构:
# - 数组: dp数组存储每一阶的方法数
#
# 时间复杂度: O(n), n为楼梯阶数
# 空间复杂度: O(n), 需要dp数组存储中间状态

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 特殊情况处理
        if n <= 2:
            return n
            
        # 创建dp数组并初始化
        dp = [0] * (n + 1)
        dp[1] = 1  # 爬1阶楼梯只有1种方法
        dp[2] = 2  # 爬2阶楼梯有2种方法
        
        # 从第3阶开始计算到第n阶
        for i in range(3, n + 1):
            # 当前阶数的方法数等于前两阶方法数之和
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]

# @lc code=end
