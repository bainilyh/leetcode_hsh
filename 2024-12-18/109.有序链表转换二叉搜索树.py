#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
解题思路:
1. 使用快慢指针找到链表的中间节点作为根节点
2. 将链表分成左右两部分，分别递归构造左右子树
3. 由于链表是有序的，构造出的二叉搜索树自然满足BST性质

使用的数据结构和算法:
- 链表
- 二叉搜索树
- 快慢指针
- 递归
"""

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 如果链表为空，返回None
        if not head:
            return None
        # 如果只有一个节点，直接返回树节点
        if not head.next:
            return TreeNode(head.val)
            
        # 使用快慢指针找到中间节点
        slow = fast = prev = head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        # 断开链表，分成左右两部分
        prev.next = None
        
        # 创建根节点
        root = TreeNode(slow.val)
        
        # 递归构造左子树（使用中间节点左边的链表部分）
        root.left = self.sortedListToBST(head)
        # 递归构造右子树（使用中间节点右边的链表部分）
        root.right = self.sortedListToBST(slow.next)
        
        return root

"""
时间复杂度: O(nlogn)
- 每次需要遍历一半的链表找到中间节点，时间为O(n/2)
- 递归树的深度为O(logn)
- 总时间复杂度为O(nlogn)

空间复杂度: O(logn)
- 递归调用栈的深度为O(logn)
"""

# @lc code=end
