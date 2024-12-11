#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#
# 解题思路:
# 1. 需要检查数独的三个规则:每行、每列、每个3x3方格内数字不重复
# 2. 使用哈希集合存储已经遇到的数字,分别记录行、列、方格中的数字
# 3. 遍历整个数独,对每个数字进行验证
# 4. 对于3x3方格,可以用 (row//3,col//3) 来定位具体是哪个方格
#
# 数据结构: 
# - 使用set存储已出现的数字
# - 使用字典存储每行、每列、每个方格的set
#
# 时间复杂度: O(1),因为数独大小固定为9x9
# 空间复杂度: O(1),使用固定大小的额外空间

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 初始化三个字典,分别存储行、列、方格中已出现的数字
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        
        # 遍历整个数独
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                # 跳过空格
                if num == '.':
                    continue
                    
                # 检查当前数字是否已在行、列或方格中出现
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes[(i//3,j//3)]):
                    return False
                    
                # 将当前数字加入对应的集合中
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i//3,j//3)].add(num)
                
        return True
        
# @lc code=end
