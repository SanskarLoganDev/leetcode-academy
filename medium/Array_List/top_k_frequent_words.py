# 692. Top K Frequent Words
# Solved
# Medium
# Topics
# conpanies icon
# Companies
# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:

# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
 

# Constraints:

# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]

# worst case time complexity O(n log n) due to sorting, but can be improved to O(n log k) using a heap.
# complexity analysis:
# O(nlogn+nlogk), which is still dominated by O(nlogn) unless k is very close to n.

from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        count = Counter(words)
        return [x[0] for x in count.most_common(k)]
    
    