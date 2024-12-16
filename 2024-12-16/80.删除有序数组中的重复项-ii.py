#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        解题思路:
        - 使用双指针法,slow指针表示处理完成的数组的最后一个位置,fast指针用于遍历数组
        - 由于题目要求最多保留2个重复元素,所以我们需要判断当前元素是否可以保留
        - 判断方法是将当前元素与slow-2位置的元素比较,如果不同则可以保留
        
        数据结构:
        - 数组
        
        算法:
        - 双指针
        
        时间复杂度: O(n) - 只需要遍历一次数组
        空间复杂度: O(1) - 只使用了常数个变量
        """
        # 如果数组长度小于等于2,不需要处理
        if len(nums) <= 2:
            return len(nums)
        
        # slow指向下一个要填入的位置
        slow = 2
        # fast指针用于遍历数组
        for fast in range(2, len(nums)):
            # 如果当前元素与slow-2位置的元素不同,说明可以保留当前元素
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
                
        return slow

# @lc code=end
