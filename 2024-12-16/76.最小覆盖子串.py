#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# 解题思路:
# 1. 使用滑动窗口法解决此问题
# 2. 用两个哈希表记录窗口内字符频次和目标字符串t的字符频次
# 3. 用双指针left和right维护滑动窗口
# 4. 当窗口包含所有t中字符时,尝试收缩左边界找最小窗口
#
# 数据结构:
# - 哈希表: 记录字符频次
# - 双指针: 维护滑动窗口
#
# 算法:
# - 滑动窗口

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 特殊情况处理
        if not s or not t or len(s) < len(t):
            return ""
            
        # 创建两个计数器
        need = {}  # 记录t中字符频次
        window = {}  # 记录窗口中字符频次
        
        # 初始化need字典
        for c in t:
            need[c] = need.get(c, 0) + 1
            
        # 初始化窗口指针和结果变量
        left = 0  # 左指针
        right = 0  # 右指针
        valid = 0  # 已匹配字符数
        start = 0  # 最小覆盖子串的起始位置
        min_len = float('inf')  # 最小覆盖子串的长度
        
        # 开始滑动窗口
        while right < len(s):
            # 扩大窗口
            c = s[right]
            right += 1
            
            # 更新窗口内数据
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
                    
            # 判断是否需要收缩窗口
            while valid == len(need):
                # 更新最小覆盖子串
                if right - left < min_len:
                    start = left
                    min_len = right - left
                    
                # 缩小窗口
                d = s[left]
                left += 1
                
                # 更新窗口内数据
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    
        # 返回结果
        return "" if min_len == float('inf') else s[start:start + min_len]

# @lc code=end

# 时间复杂度: O(n), n为字符串s的长度
# 空间复杂度: O(k), k为字符集大小,本题中为t的长度
