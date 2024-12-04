#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
# [4,5,6,7,0,1,2,3]
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[0]:
                # 在大增序里判断是否存在target
                if nums[0] <= target and nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[0]:
                # 在小增序里判断是否存在target
                if nums[mid] < target and nums[-1] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
# @lc code=end

