#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#
# [1,2,3,1,1]
# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 判断是否在days内完成装送 O(n)
        def f(cap, weights, days):
            tmp_cap = 0
            for weight in weights:
                tmp_cap += weight
                if tmp_cap > cap:
                    days -= 1
                    tmp_cap = weight
                elif tmp_cap == cap:
                    days -= 1
                    tmp_cap = 0
                elif days < 0: #减枝
                    return days
            if tmp_cap > 0:
                days -= 1
            return days
                
        # 左边界二分查找（求最小的重量)
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            need_days = f(mid, weights, days)
            if need_days == 0:
                right = mid - 1
            elif need_days > 0:
                right = mid - 1
            elif need_days < 0:
                left = mid + 1
        return left
# @lc code=end

