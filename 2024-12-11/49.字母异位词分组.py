#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# 解题思路:
# 使用哈希表存储字母异位词分组
# 将每个字符串排序后作为key,原字符串作为value存入哈希表
# 最后返回哈希表的所有value即为分组结果
#
# 数据结构: 哈希表、字符串
# 算法: 排序
#
# 时间复杂度: O(nklogk) - n为字符串数量,k为字符串的最大长度
# 空间复杂度: O(nk) - 需要存储所有字符串

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 创建哈希表存储分组结果
        anagram_dict = {}
        
        # 遍历所有字符串
        for s in strs:
            # 将字符串排序后作为key
            sorted_str = ''.join(sorted(s))
            # 如果key不存在,创建新列表
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = []
            # 将原字符串加入对应的分组
            anagram_dict[sorted_str].append(s)
        
        # 返回所有分组
        return list(anagram_dict.values())
        
# @lc code=end
