#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0 # 表示当前位置最远能跳到哪
        for i in range(len(nums)):
            if end < i: 
                return False
            end = max(end, i + nums[i])
        return True
        
# @lc code=end

