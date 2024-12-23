#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#
# 解题思路:
# 1. 使用广度优先搜索(BFS)对二叉树进行层序遍历
# 2. 使用队列存储每一层的节点
# 3. 最后将结果反转得到自底向上的层序遍历
#
# 使用的数据结构和算法:
# - 队列(deque): 用于BFS遍历
# - 列表(list): 存储最终结果
# - 广度优先搜索(BFS): 实现层序遍历
#
# 时间复杂度: O(n), n为节点数量
# 空间复杂度: O(n), 队列中最多存储n个节点

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 处理空树的情况
        if not root:
            return []
        
        # 导入双端队列
        from collections import deque
        # 创建队列用于BFS
        queue = deque([root])
        # 存储最终结果
        result = []
        
        # 当队列不为空时继续遍历
        while queue:
            # 获取当前层的节点数量
            level_size = len(queue)
            # 存储当前层的节点值
            current_level = []
            
            # 遍历当前层的所有节点
            for _ in range(level_size):
                # 从队列中取出节点
                node = queue.popleft()
                # 将节点值添加到当前层列表
                current_level.append(node.val)
                
                # 将左子节点加入队列
                if node.left:
                    queue.append(node.left)
                # 将右子节点加入队列
                if node.right:
                    queue.append(node.right)
            
            # 将当前层添加到结果列表
            result.append(current_level)
        
        # 返回反转后的结果，实现自底向上的层序遍历
        return result[::-1]

# @lc code=end
