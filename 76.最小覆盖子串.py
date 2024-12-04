#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# "ADOBECODEBANC"
# "ABC"

# @lc code=start
from collections import Counter

class Solution:
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
                      
# @lc code=end

