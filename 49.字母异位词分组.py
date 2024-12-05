#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_ = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            map_[sorted_s].append(s)
        res = []
        for value in map_.values():
            res.append(value)
        return res
                
# @lc code=end

