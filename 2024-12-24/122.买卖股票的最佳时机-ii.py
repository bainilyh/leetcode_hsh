#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#
# 解题思路:
# 1. 使用动态规划,dp[i][j]表示第i天状态为j时的最大利润
# 2. j=0表示不持有股票,j=1表示持有股票
# 3. 状态转移方程:
#    dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i]) # 不持有 = max(前一天不持有, 前一天持有并卖出)
#    dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) # 持有 = max(前一天持有, 前一天不持有并买入)
#
# 使用的数据结构和算法:
# - 数据结构:二维dp数组
# - 算法:动态规划
#
# 时间复杂度:O(n) - 需要遍历一次价格数组
# 空间复杂度:O(n) - 需要2*n的dp数组,可以优化到O(1)

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 如果价格列表为空或只有一天，无法获得利润
        if len(prices) <= 1:
            return 0
            
        n = len(prices)
        # 创建dp数组,dp[i][0]表示第i天不持有股票的最大利润,dp[i][1]表示第i天持有股票的最大利润
        dp = [[0, 0] for _ in range(n)]
        
        # 初始化第一天的状态
        dp[0][0] = 0  # 第一天不持有股票,利润为0
        dp[0][1] = -prices[0]  # 第一天持有股票,利润为负的股票价格
        
        # 遍历每一天,计算两种状态的最大利润
        for i in range(1, n):
            # 计算第i天不持有股票的最大利润
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 计算第i天持有股票的最大利润
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            
        # 最后一天不持有股票的状态一定比持有股票的状态利润高
        return dp[n-1][0]

    # 贪心算法解法
    # 解题思路:
    # 1. 由于可以进行多次交易，只要后一天的价格比前一天高，就可以进行买卖
    # 2. 贪心策略:只要有利润就进行交易，最终累加所有正利润
    # 3. 这种方法可以得到最优解，因为把所有上涨的价格差都计入利润中
    #
    # 使用的数据结构和算法:
    # - 数据结构:单个变量记录总利润
    # - 算法:贪心算法
    #
    # 时间复杂度:O(n) - 只需要遍历一次价格数组
    # 空间复杂度:O(1) - 只需要一个变量存储总利润
    def maxProfit2(self, prices: List[int]) -> int:
        # 如果价格列表为空或只有一天，无法获得利润
        if len(prices) <= 1:
            return 0
            
        total_profit = 0
        # 遍历价格数组，只要后一天价格比前一天高，就可以获得利润
        for i in range(1, len(prices)):
            # 如果当天价格比前一天高，就进行一次买卖交易
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
                
        return total_profit
        
# @lc code=end
