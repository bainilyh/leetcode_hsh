#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 解题思路：二分查找
        # 数据结构：数组
        # 算法：修改版二分查找，需要判断哪部分是有序的

        if not nums:
            return -1  # 如果数组为空，返回-1
        
        left, right = 0, len(nums) - 1  # 初始化左右指针
        
        while left <= right:
            mid = (left + right) // 2  # 计算中间位置
            
            if nums[mid] == target:  # 如果找到目标值，直接返回索引
                return mid
            
            # 判断左半部分是否有序
            if nums[left] <= nums[mid]:
                # 目标值在左半有序部分
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # 在左半部分继续搜索
                else:
                    left = mid + 1   # 在右半部分继续搜索
            # 右半部分有序
            else:
                # 目标值在右半有序部分
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # 在右半部分继续搜索
                else:
                    right = mid - 1  # 在左半部分继续搜索
                    
        return -1  # 没有找到目标值，返回-1

# @lc code=end

# 时间复杂度：O(log n)，使用二分查找，每次将搜索范围缩小一半。
# 空间复杂度：O(1)，只使用了常数级别的额外空间。
