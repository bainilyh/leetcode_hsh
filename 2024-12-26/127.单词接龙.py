#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# 解题思路:
# 1. 将单词转换问题看作图的最短路径问题
# 2. 每个单词是图中的一个节点，如果两个单词可以通过改变一个字母相互转换，则它们之间有一条边
# 3. 使用广度优先搜索(BFS)找到从beginWord到endWord的最短路径
#
# 数据结构: 队列、集合、图
# 算法: 广度优先搜索(BFS)
#
# 时间复杂度: O(N * 26 * L), N是单词表中单词的数量，L是单词的长度
# 空间复杂度: O(N), N是单词表中单词的数量

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 如果结束单词不在单词表中，直接返回0
        if endWord not in wordList:
            return 0
            
        # 将单词表转换为集合，提高查找效率
        wordSet = set(wordList)
        # 如果开始单词在单词表中，需要移除以避免重复访问
        if beginWord in wordSet:
            wordSet.remove(beginWord)
            
        # 创建队列，用于BFS
        queue = [(beginWord, 1)]
        # 遍历队列
        while queue:
            word, level = queue.pop(0)
            # 如果找到结束单词，返回转换序列的长度
            if word == endWord:
                return level
                
            # 尝试改变当前单词的每个位置的字母
            for i in range(len(word)):
                # 尝试将当前位置替换为a-z的每个字母
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    # 如果新单词在单词表中
                    if newWord in wordSet:
                        # 将新单词加入队列，层数加1
                        queue.append((newWord, level + 1))
                        # 从单词表中移除该单词，避免重复访问
                        wordSet.remove(newWord)
                        
        # 如果无法转换到结束单词，返回0
        return 0
        
# @lc code=end
