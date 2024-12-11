#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# 解题思路:
# 1. 使用双指针法,从两端向中间移动
# 2. 维护左右两边的最大高度
# 3. 较小的一边可以确定当前位置能接的雨水量
# 
# 数据结构: 数组
# 算法: 双指针
#
# 时间复杂度: O(n) - 只需遍历一次数组
# 空间复杂度: O(1) - 只使用常数额外空间

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # 特判空数组的情况
        if not height:
            return 0
            
        # 初始化双指针和结果
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        result = 0
        
        # 当左右指针未相遇时循环
        while left < right:
            # 更新左右两边的最大高度
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            # 处理较小的一边
            if left_max < right_max:
                # 当前位置能接的雨水 = 左边最大高度 - 当前高度
                result += left_max - height[left]
                left += 1
            else:
                # 当前位置能接的雨水 = 右边最大高度 - 当前高度
                result += right_max - height[right]
                right -= 1
                
        return result
        
# @lc code=end
