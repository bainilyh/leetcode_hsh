#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# 解题思路:
# 1. 使用回溯算法,尝试在每个空格填入1-9,检查是否有效
# 2. 如果当前数字无效,回溯到上一步继续尝试
# 3. 使用三个集合记录每行、每列、每个3x3方格中已使用的数字
#
# 数据结构:
# - 二维数组board表示数独盘面
# - 三个字典rows,cols,boxes记录已使用数字
#
# 算法:
# - 回溯(DFS) + 约束编程
#
# 时间复杂度: O(9^m) m为空格数量
# 空间复杂度: O(m) m为空格数量,递归调用栈的深度

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 初始化三个字典,记录每行、列、3x3方格中已使用的数字
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # 遍历棋盘,记录已有数字
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    box_id = (i // 3) * 3 + j // 3
                    boxes[box_id].add(num)
        
        def backtrack(i: int, j: int) -> bool:
            # 已经填完所有空格,返回True
            if i == 9:
                return True
            
            # 计算下一个位置的坐标    
            next_i = i + (j + 1) // 9
            next_j = (j + 1) % 9
            
            # 如果当前位置已有数字,继续下一个位置
            if board[i][j] != '.':
                return backtrack(next_i, next_j)
                
            # 尝试填入1-9    
            box_id = (i // 3) * 3 + j // 3
            for num in range(1, 10):
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_id]:
                    # 在三个集合中添加该数字
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_id].add(num)
                    board[i][j] = str(num)
                    
                    # 继续填下一个位置
                    if backtrack(next_i, next_j):
                        return True
                        
                    # 回溯,移除该数字
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_id].remove(num)
                    board[i][j] = '.'
                    
            return False
            
        backtrack(0, 0)
        
# @lc code=end
