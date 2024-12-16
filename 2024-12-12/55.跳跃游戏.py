#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# 解题思路:
# 使用贪心算法,维护一个最远可达位置maxReach
# 遍历数组,如果当前位置i可达(i <= maxReach),则更新maxReach
# 最后判断maxReach是否能到达最后一个位置
#
# 数据结构: 整型变量maxReach记录最远可达位置
# 算法: 贪心算法
#
# 时间复杂度: O(n) - 遍历一次数组
# 空间复杂度: O(1) - 只使用常数额外空间

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 初始化最远可达位置为0
        maxReach = 0
        
        # 遍历数组中的每个位置
        for i in range(len(nums)):
            # 如果当前位置不可达,直接返回False
            if i > maxReach:
                return False
            # 更新最远可达位置
            maxReach = max(maxReach, i + nums[i])
            # 如果最远可达位置已经超过或等于最后一个位置,返回True
            if maxReach >= len(nums) - 1:
                return True
        
        return True
        
# @lc code=end
