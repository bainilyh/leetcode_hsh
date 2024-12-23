#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# 解题思路:
# 1. 使用回溯法生成所有可能的子集
# 2. 为了避免重复,需要先对数组排序,然后在同一层递归中跳过重复元素
# 3. 使用start参数控制开始位置,避免重复选择
#
# 数据结构:
# - 列表(List): 存储输入数组和结果集
# - 回溯法(Backtracking): 用于生成所有可能的组合
#
# 算法复杂度:
# - 时间复杂度: O(n * 2^n), n为数组长度
# - 空间复杂度: O(n), 递归调用栈的深度

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 定义结果列表
        result = []
        # 对输入数组排序,便于去重
        nums.sort()
        
        def backtrack(start: int, curr: List[int]):
            # 将当前组合加入结果集
            result.append(curr[:])
            
            # 从start开始遍历,避免重复选择
            for i in range(start, len(nums)):
                # 跳过同一层的重复元素
                if i > start and nums[i] == nums[i-1]:
                    continue
                # 选择当前元素
                curr.append(nums[i])
                # 递归处理下一个位置
                backtrack(i + 1, curr)
                # 回溯,移除当前元素
                curr.pop()
        
        # 从空集开始回溯
        backtrack(0, [])
        return result
        
# @lc code=end
