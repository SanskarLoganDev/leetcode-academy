# 355. Design Twitter

# Neetcode 150 (Important)

# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

# Constraints:

# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
# A user cannot follow himself.

import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.tweetTime = 0
        self.tweetMap = defaultdict(list) # {userId : [(tweetTime, tweetId)]}
        self.followeeMap = defaultdict(set) # {followerId: set(followeeId)}

    def postTweet(self, userId: int, tweetId: int) -> None: # time complexity O(1)
        self.tweetTime-=1 # here we -1 as in python we don't have max heap, so we will use min heap and to get the most recent tweet we will use negative time
        self.tweetMap[userId].append((self.tweetTime, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]: # time complexity O(T), where T is the total number of tweets of the user and the users he follows
        heap = []
        # the for loops below are used to get all the tweets of the user and the users he follows in a single heap
        # Collect all tweets from the user and each followee into heap -> scans T tuples → O(T)
        for user in self.tweetMap[userId]:
            heap.append(user)
        for followeeId in self.followeeMap[userId]:
            for user in self.tweetMap[followeeId]:
                heap.append(user)
        heapq.heapify(heap) # heapify happens on the first element of the tuple, which is tweetTime here. Time complexity O(T) 
        res = []
        count = 1
        while heap and count<=10: # extracting only 10 most recent tweets, Pop up to 10 items (heappop) → ≤10 × O(log T) = O(log T) (constant factor 10)
            time, userid = heapq.heappop(heap)
            res.append(userid)
            count+=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None: # time complexity O(1)
        self.followeeMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None: # time complexity O(1)
        if followerId in self.followeeMap:
            self.followeeMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)