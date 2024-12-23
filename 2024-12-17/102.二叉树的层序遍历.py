#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# 解题思路:
# 1. 使用队列实现二叉树的层序遍历
# 2. 每次从队列取出一层的所有节点,将它们的值加入结果列表
# 3. 同时将下一层的节点加入队列
# 4. 直到队列为空,遍历结束
#
# 使用的数据结构和算法:
# - 数据结构: 二叉树、队列
# - 算法: 广度优先搜索(BFS)
#
# 时间复杂度: O(n), n为节点数,需要遍历所有节点
# 空间复杂度: O(w), w为树的最大宽度,队列中最多存储一层的节点数

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 如果根节点为空,返回空列表
        if not root:
            return []
            
        # 初始化结果列表和队列
        result = []
        queue = [root]
        
        # 当队列不为空时继续遍历
        while queue:
            # 获取当前层的节点数
            level_size = len(queue)
            # 存储当前层的节点值
            current_level = []
            
            # 遍历当前层的所有节点
            for _ in range(level_size):
                # 从队列头部取出节点
                node = queue.pop(0)
                # 将节点值加入当前层列表
                current_level.append(node.val)
                
                # 将左右子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 将当前层的节点值列表加入结果
            result.append(current_level)
            
        return result
        
# @lc code=end
