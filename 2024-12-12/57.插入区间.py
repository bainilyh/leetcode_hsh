#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# 解题思路:
# 1. 遍历原有区间列表,将新区间插入到合适位置
# 2. 处理重叠区间,合并重叠部分
# 
# 使用的数据结构和算法:
# - 数组
# - 双指针
# - 区间合并
#
# 时间复杂度: O(n) - 需要遍历一次区间列表
# 空间复杂度: O(n) - 需要存储合并后的区间列表

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 定义结果列表
        res = []
        # 获取区间列表长度
        n = len(intervals)
        # 当前遍历位置
        i = 0
        
        # 将所有在新区间左侧且不重叠的区间加入结果列表
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # 合并所有与新区间重叠的区间
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # 将合并后的新区间加入结果列表    
        res.append(newInterval)
        
        # 将所有在新区间右侧且不重叠的区间加入结果列表
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res
        
# @lc code=end
