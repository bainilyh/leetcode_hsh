#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# 解题思路:
# 1. 首先按照区间的起始位置对所有区间进行排序
# 2. 遍历排序后的区间,将重叠的区间进行合并
# 3. 如果当前区间的起始位置小于等于结果数组中最后一个区间的结束位置,说明有重叠
# 4. 合并重叠区间时,取两个区间结束位置的较大值作为新区间的结束位置
#
# 使用的数据结构和算法:
# - 数组
# - 排序
# - 双指针
#
# 时间复杂度: O(nlogn), 其中n是区间的数量,主要来自排序的时间复杂度
# 空间复杂度: O(n), 需要存储合并后的区间结果

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 如果区间列表为空,直接返回空列表
        if not intervals:
            return []
            
        # 按照区间的起始位置进行排序
        intervals.sort(key=lambda x: x[0])
        
        # 初始化结果列表,将第一个区间加入
        merged = [intervals[0]]
        
        # 遍历剩余的区间
        for interval in intervals[1:]:
            # 如果当前区间的起始位置小于等于结果数组中最后一个区间的结束位置
            if interval[0] <= merged[-1][1]:
                # 更新结果数组中最后一个区间的结束位置为两个区间结束位置的较大值
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                # 如果没有重叠,直接将当前区间加入结果数组
                merged.append(interval)
        
        return merged
        
# @lc code=end
