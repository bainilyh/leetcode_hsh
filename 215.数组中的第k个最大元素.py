#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # def partition(nums, low, high):
        #     pivot = nums[low]
        #     while low < high:
        #         while low < high and nums[high] >= pivot:
        #             high -= 1
        #         nums[low] = nums[high]
        #         while low < high and nums[low] <= pivot:
        #             low += 1
        #         nums[high] = nums[low]
        #     nums[low] = pivot
        #     return low
        
        # res_index = len(nums) - k
        # low, high = 0, len(nums) - 1
        
        # while low < high:
        #     cur_index = partition(nums, low, high)
        #     if cur_index == res_index:
        #         return nums[cur_index]
        #     elif cur_index > res_index:
        #         high = cur_index - 1
        #     elif cur_index < res_index:
        #         low = cur_index + 1
        # return nums[low]
            
# @lc code=end

