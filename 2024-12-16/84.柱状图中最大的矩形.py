#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# 解题思路:
# 1. 使用单调栈来解决,栈中存储柱子的索引
# 2. 栈中的柱子高度保持单调递增
# 3. 当遇到比栈顶矮的柱子时,说明可以计算栈顶柱子为高的矩形面积
# 4. 为了处理边界情况,在heights首尾添加高度为0的柱子
#
# 数据结构: 单调栈
# 算法: 单调栈 + 面积计算
#
# 时间复杂度: O(n) - 每个元素最多入栈出栈各一次
# 空间复杂度: O(n) - 栈的大小最大为n

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 在heights首尾添加0,便于处理边界情况
        heights = [0] + heights + [0]
        # 初始化栈和最大面积
        stack = []
        max_area = 0
        
        # 遍历所有柱子
        for i in range(len(heights)):
            # 当栈不为空且当前柱子比栈顶柱子矮时
            while stack and heights[i] < heights[stack[-1]]:
                # 弹出栈顶元素
                cur_height = heights[stack.pop()]
                # 计算宽度(右边界-左边界-1)
                cur_width = i - stack[-1] - 1
                # 更新最大面积
                max_area = max(max_area, cur_height * cur_width)
            # 将当前柱子索引入栈
            stack.append(i)
            
        return max_area
        
# @lc code=end
