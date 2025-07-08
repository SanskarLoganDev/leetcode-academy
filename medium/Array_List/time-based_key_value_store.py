# 981. Time Based Key-Value Store (Neetcode 150) Important

# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

# Example 1:

# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
 

# Constraints:

# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.

# time complexity: O(n) for get, O(1) for set
# space complexity: O(n) where n is the number of key-value pairs
# for the below solution I get time limit exceeded for large inputs but the code is correct.

class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append([value, timestamp])
        else:
            self.dict[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        
        # if the key does not exist, return an empty string
        if key not in self.dict:
            return ""
        pairs = self.dict[key]
        
        # chccking for equality first
        for i in range(len(pairs)):
            if pairs[i][1]==timestamp:
                return pairs[i][0]
        
        # if the timestamp is greater than the first timestamp, find the value with the largest timestamp less than or equal to the given timestamp
        for i in range(len(pairs)-1):
            if pairs[i][1]< timestamp <pairs[i+1][1]:
                return pairs[i][0]
            
        # if we reach here, it means the timestamp is greater than the last timestamp
        if timestamp>self.dict[key][-1][1]:
            return self.dict[key][-1][0]
        
        # if the timestamp is less than the first timestamp, return an empty string (can also checked at the start)
        return ""
        
# optimal solution using binary search
# time complexity: O(log n) for get, O(1) for set

class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append([value, timestamp])
        else:
            self.dict[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        pairs = self.dict[key]
        res = ""
        l = 0
        r = len(pairs)-1
        while l<=r:
            mid = (l+r)//2
            if pairs[mid][1]==timestamp:
                return pairs[mid][0]
            if pairs[mid][1]<timestamp:
                res = pairs[mid][0]
                l = mid+1
            else:
                r = mid-1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)