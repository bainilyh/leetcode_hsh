#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 解题思路：排序 + 双指针
        # 数据结构：列表
        # 算法：排序，双指针遍历

        nums.sort()  # 对数组进行排序
        n = len(nums)
        closest_sum = float('inf')  # 初始化最接近的和为无穷大

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 跳过重复的第一个数，避免重复计算

            left, right = i + 1, n - 1  # 设置左右指针

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return current_sum  # 如果和等于目标值，直接返回

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum  # 更新最接近的和

                if current_sum < target:
                    left += 1  # 和小于目标值，左指针右移
                else:
                    right -= 1  # 和大于目标值，右指针左移

        return closest_sum

# @lc code=end

# 时间复杂度：O(n^2)，其中 n 是数组的长度。排序的时间复杂度是 O(nlogn)，
# 双指针遍历的时间复杂度是 O(n^2)，总体时间复杂度为 O(n^2)。
# 空间复杂度：O(1)，除了输入数组外，我们只需要常数级别的空间。
