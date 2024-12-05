#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 相当于爬楼梯，求最小爬楼梯的步数
        # 贪心算法每次选择最大的硬币，方法不行。
        
        # 这里dfs定义：当金额为amount时，返回所需硬币个数，不能凑的时候为-1
        mem_ = {} #这里还是声明数组好，节约空间。
        def dfs(coins, amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in mem_:
                return mem_[amount]
            res = float('inf')
            for coin in coins:
                cur_res = dfs(coins, amount - coin)
                if cur_res == -1:
                    continue
                res = min(res, cur_res + 1)
            mem_[amount] = res if res != float('inf') else -1
            return mem_[amount]
        
        return dfs(coins, amount)
        
# @lc code=end

