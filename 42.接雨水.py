#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left_max_arr, right_max_arr = [height[0]] * len(height), [height[-1]] * len(height)
        for i in range(1, len(height)):
            left_max_arr[i] = max(left_max_arr[i - 1], height[i])
            
        for i in range(len(height) - 2, -1, -1):
            right_max_arr[i] = max(right_max_arr[i + 1], height[i])
            
        for i in range(len(height)):
            res += min(left_max_arr[i], right_max_arr[i]) - height[i]
        
        return res
        
# @lc code=end

