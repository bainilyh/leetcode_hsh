#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
# 解题思路:
# 1. 从边界上的'O'开始进行深度优先搜索(DFS)
# 2. 将与边界相连的'O'标记为特殊字符(如'#'),这些是不会被包围的
# 3. 遍历整个矩阵,将剩余的'O'变为'X'(这些是被包围的)
# 4. 将标记的'#'恢复为'O'
#
# 数据结构: 二维数组
# 算法: 深度优先搜索(DFS)
#
# 时间复杂度: O(M*N) - M和N分别是矩阵的行数和列数
# 空间复杂度: O(M*N) - 最坏情况下的递归栈深度

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(i: int, j: int) -> None:
            # 如果越界或者不是'O',则返回
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
            
            # 将当前'O'标记为'#'
            board[i][j] = '#'
            
            # 递归处理上下左右四个方向
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        # 处理第一行和最后一行
        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)
        
        # 处理第一列和最后一列
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        
        # 将剩余的'O'变为'X',将'#'恢复为'O'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        
# @lc code=end
