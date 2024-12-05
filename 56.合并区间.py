#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][-1]
        res = []
        for i in range(1, len(intervals)):
            start_new = intervals[i][0]
            end_new = intervals[i][-1]
            if start_new > end:
                res.append([start, end])
                start = start_new
                end = end_new
                
            else:
                end = max(end, end_new) # 思考这里为什么需要比较呢？
        res.append([start, end])
        return res
        
# @lc code=end

