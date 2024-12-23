# #
# # @lc app=leetcode.cn id=96 lang=python3
# #
# # [96] 不同的二叉搜索树
# #
# # 解题思路1 - 动态规划:
# # 1. dp[i]表示i个节点能构成的不同二叉搜索树的个数
# # 2. 状态转移方程: dp[n] = sum(dp[i-1] * dp[n-i]) for i in range(1,n+1)
# # 3. 初始条件: dp[0] = dp[1] = 1
# #
# # 解题思路2 - 数学方法(卡特兰数):
# # 1. 二叉搜索树的个数实际上是卡特兰数
# # 2. 卡特兰数公式: C(n) = C(2n,n)/(n+1) = (2n)!/(n!*(n+1)!)
# # 3. 递推公式: C(n+1) = C(n)*(4n+2)/(n+2)
# #
# # 解题思路3 - 递归+记忆化:
# # 1. 对于每个根节点i，左子树由[1,i-1]构成，右子树由[i+1,n]构成
# # 2. 使用记忆化避免重复计算
# # 3. 递归终止条件: n=0或n=1时返回1

# # @lc code=start
# class Solution:
#     def numTrees(self, n: int) -> int:
#         # 方法1: 动态规划
#         def dp_solution(n):
#             dp = [0] * (n + 1)
#             dp[0] = dp[1] = 1
            
#             for i in range(2, n + 1):
#                 for j in range(1, i + 1):
#                     dp[i] += dp[j - 1] * dp[i - j]
#             return dp[n]
        
#         # 方法2: 卡特兰数
#         def catalan_solution(n):
#             c = 1
#             for i in range(n):
#                 c = c * 2 * (2 * i + 1) // (i + 2)
#             return c
        
#         # 方法3: 递归+记忆化
#         def recursive_solution(n, memo=None):
#             if memo is None:
#                 memo = {}
#             if n in memo:
#                 return memo[n]
#             if n <= 1:
#                 return 1
                
#             count = 0
#             for i in range(1, n + 1):
#                 # 左子树的可能数量 * 右子树的可能数量
#                 left = recursive_solution(i - 1, memo)
#                 right = recursive_solution(n - i, memo)
#                 count += left * right
            
#             memo[n] = count
#             return count
        
#         # 这里使用卡特兰数解法，因为时间复杂度最优
#         return catalan_solution(n)

# # 动态规划解法:
# # 时间复杂度: O(n^2)
# # 空间复杂度: O(n)

# # 卡特兰数解法:
# # 时间复杂度: O(n)
# # 空间复杂度: O(1)

# # 递归+记忆化解法:
# # 时间复杂度: O(n^2)
# # 空间复杂度: O(n)
# # @lc code=end
