# 快排
def quick_sort(nums, low, high):
    def partition(nums, low, high):
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low
    
    if low < high:
        pivot_pos = partition(nums, low, high)
        quick_sort(nums, low, pivot_pos - 1)
        quick_sort(nums, pivot_pos + 1, high)
        
nums = [2, 5, 1, 7, 10 , 24, 13, 16, 3, 9, 8]
quick_sort(nums, 0, len(nums) - 1)
print(nums)
    
             