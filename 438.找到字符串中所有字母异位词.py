#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        windows = Counter()
        left, right = 0, 0
        valid = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1
            
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if need[d] == windows[d]:
                        valid -= 1
                    windows[d] -= 1
        return res
        
# @lc code=end

