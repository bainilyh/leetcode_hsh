#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 解题思路：使用两次二分查找，分别找到目标值的第一个和最后一个位置
        # 数据结构：数组
        # 算法：修改版二分查找，需要分别处理左边界和右边界

        def findLeft(nums, target):
            # 查找目标值的第一个位置
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                # 如果中间值大于等于目标值，继续向左查找
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            # 检查是否找到目标值
            if left < len(nums) and nums[left] == target:
                return left
            return -1

        def findRight(nums, target):
            # 查找目标值的最后一个位置
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                # 如果中间值小于等于目标值，继续向右查找
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            # 检查是否找到目标值
            if right >= 0 and nums[right] == target:
                return right
            return -1

        # 如果数组为空，直接返回[-1, -1]
        if not nums:
            return [-1, -1]
        
        # 分别查找左右边界并返回结果
        left = findLeft(nums, target)
        right = findRight(nums, target)
        return [left, right]

# @lc code=end

# 时间复杂度：O(log n)，使用了两次二分查找，每次的时间复杂度都是O(log n)
# 空间复杂度：O(1)，只使用了常数级别的额外空间
