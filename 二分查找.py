# 【大前提】 有序数组；有序数组；有序数组
# 1. 基本二分查找框架
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1

# 2. 左边界二分查找；【找不到target返回大于target的最小索引】
# 有需求【小于 target 的最大元素的索引】就可以 left_bound(nums, target) - 1
def left_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    # 找不到target返回大于target的最小索引
    # return left 
    # 找不到target返回-1
    if left < 0 or left >= len(nums):
        return -1
    return left if nums[left] == target else -1

# 3. 右边界二分查找；【找不到target返回小于target的最大索引】
def right_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    # 找不到target返回小于target的最大索引
    # return left - 1 
    # 找不到target返回-1
    if left - 1 < 0 or left - 1 >= len(nums):
        return -1
    return left - 1 if nums[left - 1] == target else -1
        