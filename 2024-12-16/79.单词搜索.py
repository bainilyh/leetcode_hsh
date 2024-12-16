#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# 解题思路:
# 1. 使用深度优先搜索(DFS)遍历二维网格
# 2. 从每个单元格开始尝试匹配单词
# 3. 使用visited数组标记已访问的单元格,避免重复访问
# 4. 递归搜索上下左右四个方向
#
# 数据结构:
# - 二维数组board: 存储字符网格
# - 集合visited: 记录已访问的单元格坐标
#
# 算法:
# - DFS(深度优先搜索)
# - 回溯

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 获取网格的行数和列数
        rows, cols = len(board), len(board[0])
        # 创建访问标记集合
        visited = set()
        
        def dfs(row: int, col: int, index: int) -> bool:
            # 如果已经匹配完整个单词,返回True
            if index == len(word):
                return True
            
            # 检查当前位置是否越界或已访问或字符不匹配
            if (row < 0 or row >= rows or col < 0 or col >= cols or 
                (row, col) in visited or board[row][col] != word[index]):
                return False
            
            # 标记当前单元格为已访问
            visited.add((row, col))
            
            # 搜索四个方向
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                if dfs(row + dx, col + dy, index + 1):
                    return True
            
            # 回溯,移除访问标记
            visited.remove((row, col))
            return False
        
        # 从每个单元格开始尝试匹配
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False

# @lc code=end

# 时间复杂度: O(N * M * 4^L), 其中N和M是网格的行数和列数,L是单词长度
# 空间复杂度: O(L), L是单词长度,主要是递归调用栈的开销
