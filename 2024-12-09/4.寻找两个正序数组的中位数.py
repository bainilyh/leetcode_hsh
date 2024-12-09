#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确保 nums1 是较短的数组，如果不是则交换
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # 获取两个数组的长度
        m, n = len(nums1), len(nums2)
        # 初始化二分查找的左右边界
        left, right = 0, m
        
        # 开始二分查找
        while left <= right:
            # 计算 nums1 的分割点
            i = (left + right) // 2
            # 计算 nums2 的分割点
            j = (m + n + 1) // 2 - i
            
            # 如果 nums1 左半部分的最大值大于 nums2 右半部分的最小值，右边界左移
            if i > 0 and nums1[i-1] > nums2[j]:
                right = i - 1
            # 如果 nums2 左半部分的最大值大于 nums1 右半部分的最小值，左边界右移
            elif i < m and nums2[j-1] > nums1[i]:
                left = i + 1
            # 找到合适的分割点
            else:
                # 处理 nums1 左半部分为空的情况
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])
                
                # 如果总长度为奇数，直接返回左半部分的最大值
                if (m + n) % 2 == 1:
                    return max_left
                
                # 处理 nums1 或 nums2 右半部分为空的情况
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                
                # 返回中位数（左半部分最大值和右半部分最小值的平均值）
                return (max_left + min_right) / 2.0
        
# @lc code=end

# 时间复杂度：O(log(min(m,n)))，其中 m 和 n 分别是 nums1 和 nums2 的长度。
# 二分查找的次数与较短数组的长度成对数关系。

# 空间复杂度：O(1)。只使用了常数个额外变量，不随输入规模增长。
