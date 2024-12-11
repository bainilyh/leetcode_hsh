#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# [2,3,1,1,4]
# 解题思路:
# 使用贪心算法,每次在可跳范围内选择可以到达最远距离的位置
# 记录当前能跳到的最远位置(end)和下一步能跳到的最远位置(max_far)
# 当到达end时说明需要进行一次跳跃,更新end为max_far
#
# 数据结构: 数组
# 算法: 贪心算法
#
# 时间复杂度: O(n) - 只需要遍历一次数组
# 空间复杂度: O(1) - 只使用了常数个变量

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)  # 获取数组长度
        max_far = 0    # 下一步能跳到的最远位置
        end = 0        # 当前能跳到的最远位置
        steps = 0      # 跳跃次数
        
        # 遍历数组中除最后一个元素外的所有元素
        for i in range(n - 1):
            # 更新下一步能跳到的最远位置
            max_far = max(max_far, i + nums[i])
            
            # 如果到达当前能跳到的最远位置
            if i == end:
                # 更新当前能跳到的最远位置为下一步能跳到的最远位置
                end = max_far
                # 跳跃次数加1
                steps += 1
                
        return steps
        
# @lc code=end
