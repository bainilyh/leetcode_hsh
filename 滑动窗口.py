# 解决子数组问题
# 寻找符合某个条件的最长/最短子数组/子串【子串是连续的】


# 暴力求解
# def f(nums):
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             处理 nums[i:j]

# 滑动窗口
# 左闭右开 [0,0) 不包含元素
from collections import Counter
# def sw(s):
#     windows = Counter()
#     left, right = 0, 0
#     while right < len(s):
#         c = s[right]
#         windows[right] += 1
#         right += 1
        
#         while left < right and 判断左侧窗口是否要收缩:
#             d = s[left]
#             windows[d] -= 1
#             left +=1

def minWindow(self, s: str, t: str) -> str:
    need = Counter(t)
    windows = Counter()
    left, right = 0, 0
    valid = 0 # 通过valid控制左窗口滑动
    start_index, len_ = 0, float('inf') # 记录最优值
    while right < len(s):
        # 滑动右窗口
        c = s[right]
        right += 1
        
        # 判断是否更新状态
        if c in need:
            windows[c] += 1
            if windows[c] == need[c]:
                valid += 1
        
        # 滑动左窗口
        while valid == len(need):
            # 更新返回数据
            if right - left < len_:
                len_ = right - left
                start_index = left
            d = s[left]
            left += 1
            if d in need:
                if windows[d] == need[d]:
                    valid -= 1
                windows[d] -= 1
    return s[start_index: start_index + len_] if len_ != float('inf') else ''