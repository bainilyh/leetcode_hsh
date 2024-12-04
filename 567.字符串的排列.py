#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)        
        windows = Counter()
        left, right = 0, 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1
            
            # while valid == len(need): 与最小覆盖字串不同，这里需要完全匹配
            # 那么当左右窗口大于s1长度时候就进行窗口收缩
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if windows[d] == need[d]:
                        valid -= 1
                    windows[d] -= 1
        return False
                        
# @lc code=end

