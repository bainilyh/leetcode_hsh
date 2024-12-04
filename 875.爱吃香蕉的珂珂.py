#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k速度消耗
        def f(k, piles, h):
            for pile in piles:
                if pile > k:
                    h -= pile // k
                    if pile % k != 0:
                        h -= 1
                else:
                    h -= 1
            return h
                    
        
        
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            leve_h = f(mid, piles, h)
            if leve_h == 0:
                right = mid - 1
            elif leve_h > 0:
                right = mid - 1
            elif leve_h < 0:
                left = mid + 1
        return left
        
# @lc code=end

