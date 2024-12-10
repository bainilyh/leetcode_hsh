#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 使用双指针法
        left = 0  # 慢指针，指向当前可以放置元素的位置
        for right in range(len(nums)):  # 快指针，遍历整个数组
            if nums[right] != val:  # 如果当前元素不等于要删除的值
                nums[left] = nums[right]  # 将当前元素移到左指针位置
                left += 1  # 左指针向右移动
        return left  # 返回新数组的长度

# @lc code=end

# 解题思路：
# 1. 使用双指针法，一个慢指针left和一个快指针right
# 2. 快指针用于遍历数组，慢指针用于指示下一个不等于val的元素应该放置的位置
# 3. 当快指针遇到不等于val的元素时，将其复制到慢指针位置，并将慢指针向前移动

# 数据结构：
# - 数组（原地修改）

# 算法：
# - 双指针法

# 时间复杂度：O(n)，其中n是数组的长度。我们只需要遍历一次数组。
# 空间复杂度：O(1)，我们只使用了常数额外空间。
