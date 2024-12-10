#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 解题思路：排序 + 双指针
        # 数据结构：列表
        # 算法：排序，双指针遍历

        # 对数组进行排序
        nums.sort()
        n = len(nums)
        result = []

        # 遍历数组，固定第一个数
        for i in range(n - 2):
            # 跳过重复的第一个数，避免重复结果
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 设置左右指针
            left, right = i + 1, n - 1
            
            # 双指针遍历
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # 找到符合条件的三元组
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过重复的左指针
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 跳过重复的右指针
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 移动左右指针
                    left += 1
                    right -= 1
                elif total < 0:
                    # 和小于0，左指针右移
                    left += 1
                else:
                    # 和大于0，右指针左移
                    right -= 1
        
        return result

# @lc code=end

# 时间复杂度：O(n^2)，其中 n 是数组的长度。排序的时间复杂度是 O(nlogn)，
# 双指针遍历的时间复杂度是 O(n^2)，总体时间复杂度为 O(n^2)。
# 空间复杂度：O(1)，除了存储答案的列表外，我们只需要常数级别的空间。
