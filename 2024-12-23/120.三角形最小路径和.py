#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# 解题思路:
# 1. 可以使用两种动态规划方法:自底向上或自顶向下
# 2. 自底向上:每个位置的最小路径和等于当前值加上下一行相邻位置的最小值
# 3. 自顶向下:每个位置的最小路径和等于当前值加上上一行相邻位置的最小值
#
# 使用的数据结构和算法:
# - 数据结构:二维数组(三角形)
# - 算法:动态规划(两种方向)

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 获取三角形的高度
        n = len(triangle)
        
        # 方法1: 自底向上
        def bottom_up() -> int:
            # 从倒数第二行开始向上遍历
            for i in range(n-2, -1, -1):
                # 遍历当前行的每个位置
                for j in range(len(triangle[i])):
                    # 当前位置的最小路径和等于当前值加上下一行相邻位置的最小值
                    triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
            return triangle[0][0]
        
        # 方法2: 自顶向下
        def top_down() -> int:
            # 创建dp数组存储每个位置的最小路径和
            dp = [[0] * n for _ in range(n)]
            dp[0][0] = triangle[0][0]
            
            # 从第二行开始向下遍历
            for i in range(1, n):
                # 处理每行的第一个和最后一个元素
                dp[i][0] = dp[i-1][0] + triangle[i][0]
                dp[i][i] = dp[i-1][i-1] + triangle[i][i]
                
                # 处理中间的元素
                for j in range(1, i):
                    # 当前位置的最小路径和等于当前值加上上一行相邻位置的最小值
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            
            # 返回最后一行中的最小值
            return min(dp[n-1])
        
        # 这里使用自顶向下的方法
        return top_down()

# @lc code=end

# 时间复杂度: O(n^2), n为三角形的高度,两种方法都需要遍历每一行的每个元素
# 空间复杂度: 
# - 自底向上: O(1), 直接在输入数组上修改
# - 自顶向下: O(n^2), 需要额外的dp数组存储中间结果
