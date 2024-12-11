#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# 解题思路:
# 使用回溯算法,通过递归的方式生成所有可能的排列
# 使用visited数组标记已经使用过的数字
# 每次递归时,从未使用的数字中选择一个加入当前排列,然后继续递归
# 当排列长度等于原数组长度时,说明找到了一个完整的排列
#
# 数据结构: 数组、递归调用栈、visited标记数组
# 算法: 回溯算法(深度优先搜索)
#
# 时间复杂度: O(n!) - n个数字的全排列有n!种可能
# 空间复杂度: O(n) - 递归调用栈的深度为n,visited数组长度为n

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            # 如果当前排列长度等于n,说明找到了一个完整排列
            if len(curr) == n:
                output.append(curr[:])
                return
            
            # 遍历所有数字
            for i in range(n):
                # 如果当前数字未被使用
                if not visited[i]:
                    # 标记为已使用
                    visited[i] = True
                    # 将当前数字加入排列
                    curr.append(nums[i])
                    # 递归处理剩余数字
                    backtrack(curr)
                    # 回溯,移除当前数字
                    curr.pop()
                    # 标记为未使用
                    visited[i] = False
        
        n = len(nums)
        visited = [False] * n  # 标记数组,记录每个数字是否被使用
        output = []
        backtrack([])
        return output
        
# @lc code=end
