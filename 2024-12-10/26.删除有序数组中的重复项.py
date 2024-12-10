#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 如果数组为空，直接返回0
        if not nums:
            return 0
        
        # 使用双指针技巧，slow指针指向当前不重复元素的位置
        slow = 0
        
        # fast指针用于遍历整个数组
        for fast in range(1, len(nums)):
            # 如果fast指针指向的元素与slow指针指向的元素不同
            if nums[fast] != nums[slow]:
                # 将slow指针向前移动一位
                slow += 1
                # 将fast指针指向的元素复制到slow指针的位置
                nums[slow] = nums[fast]
        
        # 返回不重复元素的个数（slow指针的位置加1）
        return slow + 1

# @lc code=end

# 解题思路：
# 1. 使用双指针技巧，slow指针指向当前不重复元素的位置，fast指针用于遍历整个数组。
# 2. 当fast指针指向的元素与slow指针指向的元素不同时，将fast指针指向的元素复制到slow指针的下一位置。
# 3. 最终，slow指针的位置加1就是不重复元素的个数。

# 数据结构：
# - 输入的nums是一个有序数组
# - 使用了两个整数指针（slow和fast）来遍历和修改数组

# 算法：
# - 双指针算法

# 时间复杂度：O(n)，其中n是数组的长度。只需要遍历一次数组。
# 空间复杂度：O(1)，只使用了常数级别的额外空间。
