#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # 从右向左找到第一个相邻升序的位置
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            # 从右向左找到第一个大于nums[i]的数
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # 交换这两个数
            nums[i], nums[j] = nums[j], nums[i]
        
        # 将i之后的数反转
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# @lc code=end

# [1,2,3]
# [3,2,1]
# [1,1,5]
# 解题思路：
# 1. 从右向左找到第一个相邻升序的位置i
# 2. 从右向左找到第一个大于nums[i]的数j
# 3. 交换nums[i]和nums[j]
# 4. 将i之后的数反转

# 数据结构：
# - 输入的nums是一个整数列表
# - 使用了两个整数指针（i和j）来遍历和修改列表

# 算法：
# - 线性扫描
# - 双指针（用于反转）

# 时间复杂度：O(n)，其中n是列表的长度。最坏情况下需要扫描两次列表，反转一次。
# 空间复杂度：O(1)，只使用了常数级别的额外空间。
