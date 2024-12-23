#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#
# 解题思路:
# 1. 使用动态规划,dp[i]表示s[0:i]的解码方法数
# 2. 对于每个位置i,可以:
#    - 单独解码当前数字(1-9)
#    - 与前一个数字组合解码(10-26)
# 3. 状态转移方程:
#    dp[i] = dp[i-1](当前数字可解码) + dp[i-2](当前两位数可解码)
#
# 数据结构: 动态规划数组
# 算法: 动态规划

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # 特殊情况处理
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        # dp[i]表示s[0:i]的解码方法数
        dp = [0] * (n + 1)
        dp[0] = 1  # 空字符串有1种解码方法
        dp[1] = 1  # 第一个字符如果不为'0'则有1种解码方法
        
        # 遍历字符串
        for i in range(2, n + 1):
            # 当前数字可以单独解码
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # 当前数字可以与前一个数字组合解码
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]

# 时间复杂度: O(n) - 需要遍历一次字符串
# 空间复杂度: O(n) - 需要dp数组存储中间结果
# @lc code=end
