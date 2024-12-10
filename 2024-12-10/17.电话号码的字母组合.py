#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 如果输入为空，返回空列表
        if not digits:
            return []
        
        # 定义电话号码到字母的映射
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def backtrack(digits, index) -> None:
            # 如果路径长度等于输入长度，添加到结果列表
            if len(path) == len(digits):
                combinations.append(''.join(path))
                return
            
            # 获取当前数字对应的字母
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                # 将字母添加到路径
                path.append(letter)
                # 递归处理下一个数字
                backtrack(index + 1, path)
                # 回溯，移除最后添加的字母
                path.pop()
        
        combinations = []
        path = []
        backtrack(0, [])
        return combinations

# @lc code=end

# 解题思路：
# 1. 使用回溯法（深度优先搜索）生成所有可能的字母组合
# 2. 利用字典存储数字到字母的映射关系
# 3. 递归构建每个组合，当组合长度等于输入长度时，将其添加到结果列表

# 数据结构：
# - 列表（List）：存储最终的组合结果和当前构建的路径
# - 字典（Dict）：存储数字到字母的映射关系

# 算法：
# - 回溯法（Backtracking）：系统地搜索所有可能的解，并在确定某个选择不可行时撤销该选择

# 时间复杂度：O(4^n)，其中n是输入的数字个数。
# 在最坏情况下（输入的每个数字都对应4个字母），每个位置有4种选择。

# 空间复杂度：O(n)，其中n是输入的数字个数。
# 这里的空间主要用于递归调用栈和存储最终结果。递归深度最大为n。
