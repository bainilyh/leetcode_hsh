#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# 解题思路:
# 1. 使用回溯法生成所有可能的子集
# 2. 对于每个数字,我们有两种选择:选或不选
# 3. 通过递归实现所有可能的组合
#
# 数据结构:
# - 列表(List): 存储输入数组和结果集
# - 递归+回溯
#
# 时间复杂度: O(2^n) - 每个元素都有选和不选两种状态
# 空间复杂度: O(n) - 递归调用栈的深度

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 定义结果列表存储所有子集
        result = []
        
        def backtrack(start: int, curr: List[int]):
            # 将当前子集加入结果列表
            result.append(curr[:])
            
            # 从start开始遍历,避免重复
            for i in range(start, len(nums)):
                # 选择当前数字
                curr.append(nums[i])
                # 递归生成包含当前数字的子集
                backtrack(i + 1, curr)
                # 回溯,移除当前数字
                curr.pop()
        
        # 从空集开始回溯
        backtrack(0, [])
        return result
        
# @lc code=end
