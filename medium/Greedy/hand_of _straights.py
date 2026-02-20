# 846. Hand of Straights
# Neetcode 150

# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

 

# Constraints:

# 1 <= hand.length <= 104
# 0 <= hand[i] <= 109
# 1 <= groupSize <= hand.length

# time complexity O(NlogN + NK) where N is the number of cards in the hand and K is the group size, we are sorting the hand which takes O(NlogN) and then we are iterating through the hand and for each card we are checking for the next groupSize-1 cards which takes O(K)
# space complexity O(N) for the dictionary to store the frequency of each card in the hand

from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        hand.sort()
        d = {}
        for n in hand: # count the frequency of each card in the hand
            if n in d:
                d[n]+=1
            else:
                d[n] = 1
        while len(d)!=0:
            start = next(iter(d)) # get the smallest card in the hand to start forming a group, we can also use min(d.keys()) but it is O(N) while next(iter(d)) is O(1)
            # for key in d: # we can also use this loop to get the smallest card in the hand
            #     start = key
            #     break

            for n in range(start, start+groupSize): # check for the next groupSize-1 cards to form a group
                if n not in d: # if we don't have the next card in the hand, we can't form a group
                    return False
                d[n]-=1
                if d[n]==0: # if we have used all the cards of that value, we can remove it from the dictionary
                    d.pop(n) # can also use del d[n]
            
        return True

# here we are not iterating through the dictionary and deleting as we will get the error "RuntimeError: dictionary changed size during iteration" as we are modifying the dictionary while iterating through it.
# Instead we iterate through the range of cards we need to form a group and check if we have those cards in the dictionary, if we don't have any card in the dictionary we return False, if we have the card we decrement its frequency and if its frequency becomes 0 we remove it from the dictionary.
