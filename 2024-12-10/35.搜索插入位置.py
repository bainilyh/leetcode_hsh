#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 解题思路：使用二分查找在有序数组中找到目标值的位置或应该插入的位置
        # 数据结构：数组
        # 算法：二分查找

        # 初始化左右指针
        left, right = 0, len(nums) - 1

        # 二分查找过程
        while left <= right:
            # 计算中间位置
            mid = (left + right) // 2
            
            # 如果找到目标值，直接返回索引
            if nums[mid] == target:
                return mid
            # 如果中间值大于目标值，在左半部分继续查找
            elif nums[mid] > target:
                right = mid - 1
            # 如果中间值小于目标值，在右半部分继续查找
            else:
                left = mid + 1
        
        # 如果没有找到目标值，left 就是目标值应该插入的位置
        return left

# @lc code=end

# 时间复杂度：O(log n)，使用二分查找，每次将搜索范围缩小一半
# 空间复杂度：O(1)，只使用了常数级别的额外空间
