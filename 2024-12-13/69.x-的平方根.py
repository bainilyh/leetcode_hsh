#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#
# 解题思路:
# 1. 使用二分查找算法来查找平方根
# 2. 初始搜索范围为[0,x]
# 3. 每次取中间值mid,比较mid*mid与x的大小
# 4. 如果mid*mid <= x < (mid+1)*(mid+1),则mid即为结果
# 5. 否则根据大小关系调整搜索范围
#
# 数据结构: 整数
# 算法: 二分查找
#
# 时间复杂度: O(logx) - 二分查找的时间复杂度
# 空间复杂度: O(1) - 只使用常数额外空间

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # 特殊情况处理
        if x == 0:
            return 0
        
        # 初始化二分查找的左右边界
        left, right = 1, x
        
        # 进行二分查找
        while left <= right:
            # 计算中间值
            mid = (left + right) // 2
            
            # 如果找到平方根
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            # 如果mid的平方大于x,在左半部分继续搜索
            elif mid * mid > x:
                right = mid - 1
            # 如果mid的平方小于x,在右半部分继续搜索
            else:
                left = mid + 1
        
        return 0  # 默认返回值(实际不会执行到这里)

# @lc code=end
