#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            sqrt = x // mid
            if sqrt == mid:
                return mid
            elif sqrt > mid:
                left = mid + 1
            elif sqrt < mid:
                right = mid - 1
        return left - 1
        
# @lc code=end

