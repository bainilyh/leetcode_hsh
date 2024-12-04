#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 对于最大和为n，看看能否分割成k个
        def f(n, nums, k):
            cur_ = 0
            for num in nums:
                cur_ += num
                if cur_ > n:
                    k -= 1
                    cur_ = num
                elif cur_ == n:
                    k -= 1
                    cur_ = 0
            if cur_ > 0:
                k -= 1
            return k
                
        
        
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = left + (right - left) // 2
            leve_k = f(mid, nums, k)
            if leve_k == 0:
                right = mid - 1
            elif leve_k > 0:
                right = mid - 1
            elif leve_k < 0:
                left = mid + 1
        return left
        
# @lc code=end

