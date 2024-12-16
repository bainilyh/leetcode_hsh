#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# 解题思路:
# 1. 使用回溯算法生成所有可能的组合
# 2. 从1到n中选择k个数,每次选择时:
#    - 选择当前数,然后递归选择剩余的数
#    - 不选择当前数,继续下一个数
# 3. 当已选择的数的个数等于k时,得到一个有效组合
#
# 数据结构:
# - 列表: 存储当前组合和最终结果
# - 递归: 实现回溯过程
#
# 算法:
# - 回溯算法(深度优先搜索)

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 存储最终结果
        result = []
        
        def backtrack(start: int, curr: List[int]):
            # 如果当前组合长度等于k,说明找到一个有效组合
            if len(curr) == k:
                result.append(curr[:])
                return
            
            # 从start开始遍历,直到n
            # 剪枝优化:当剩余的数字不足以凑成k个数时,直接返回
            for i in range(start, n + 1 - (k - len(curr)) + 1):
                # 选择当前数
                curr.append(i)
                # 递归选择下一个数
                backtrack(i + 1, curr)
                # 回溯,撤销选择
                curr.pop()
        
        # 从1开始选择数字
        backtrack(1, [])
        return result

# @lc code=end
# 时间复杂度: O(C(n,k)), 需要生成所有可能的组合
# 空间复杂度: O(k), 递归调用栈的深度为k
