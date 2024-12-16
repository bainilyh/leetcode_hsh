#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# 解题思路:
# 1. 这是一个在旋转排序数组中查找目标值的问题,数组中可能包含重复元素
# 2. 使用二分查找,但需要处理重复元素的情况
# 3. 当nums[mid] == nums[left]时,无法判断哪边有序,需要left++来处理重复元素
# 4. 其他情况下,判断哪半边有序,然后判断target是否在有序的半边范围内
#
# 数据结构: 数组
# 算法: 二分查找
#
# 时间复杂度: O(logn),最坏情况下数组中有大量重复元素时为O(n)
# 空间复杂度: O(1)

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 特判空数组
        if not nums:
            return False
            
        left, right = 0, len(nums) - 1
        
        # 二分查找
        while left <= right:
            mid = (left + right) // 2
            
            # 找到目标值
            if nums[mid] == target:
                return True
                
            # 处理重复元素的情况
            if nums[left] == nums[mid]:
                left += 1
                continue
                
            # 判断左半边是否有序
            if nums[left] <= nums[mid]:
                # target在左半边的范围内
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右半边有序
            else:
                # target在右半边的范围内
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        return False
        
# @lc code=end
