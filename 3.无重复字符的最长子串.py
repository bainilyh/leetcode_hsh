#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows = Counter()
        left, right = 0, 0
        len_ = 0
        while right < len(s):
            c = s[right]
            right += 1
            
            windows[c] += 1
            
            while windows[c] > 1:
                d = s[left]
                left += 1
                windows[d] -= 1
            
            # 每次记录当前记录    
            len_ = max(len_, right - left)
        return len_
    
# @lc code=end

