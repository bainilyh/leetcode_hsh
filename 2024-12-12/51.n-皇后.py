#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# 解题思路:
# 1. 使用回溯算法,逐行放置皇后
# 2. 对每个位置,检查是否和已放置的皇后冲突(同列、对角线)
# 3. 使用集合记录已占用的列和对角线,加速冲突检查
# 4. 找到可行解时,将棋盘状态转换为要求的字符串格式
#
# 数据结构: 
# - 集合(Set): 记录已占用的列和对角线
# - 列表(List): 存储棋盘状态和最终结果
#
# 算法: 回溯算法(深度优先搜索)
#
# 时间复杂度: O(N!) - 需要尝试所有可能的放置方式
# 空间复杂度: O(N) - 需要存储已占用的列和对角线信息

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 初始化结果列表
        result = []
        # 初始化棋盘状态,使用列表记录每行皇后的列位置
        queens = [-1] * n
        # 初始化已占用的列和对角线集合
        cols = set()
        diag1 = set()  # 主对角线 r+c
        diag2 = set()  # 副对角线 r-c
        
        def generateBoard():
            """将当前棋盘状态转换为字符串格式"""
            board = []
            for i in range(n):
                row = ['.'] * n
                row[queens[i]] = 'Q'
                board.append(''.join(row))
            return board
        
        def backtrack(row):
            """回溯函数,尝试在指定行放置皇后"""
            # 如果已经放置完所有行,说明找到一个解
            if row == n:
                result.append(generateBoard())
                return
            
            # 尝试在当前行的每一列放置皇后
            for col in range(n):
                # 检查当前位置是否可以放置皇后
                if col in cols or \
                   row + col in diag1 or \
                   row - col in diag2:
                    continue
                    
                # 放置皇后,更新状态
                queens[row] = col
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                
                # 继续处理下一行
                backtrack(row + 1)
                
                # 回溯,撤销当前位置的皇后
                queens[row] = -1
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
        
        # 从第0行开始回溯
        backtrack(0)
        return result
        
# @lc code=end
