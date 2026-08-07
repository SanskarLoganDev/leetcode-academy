# 1146. Snapshot Array

# Implement a SnapshotArray that supports the following interface:

# SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

# Example 1:

# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

# Constraints:

# 1 <= length <= 5 * 104
# 0 <= index < length
# 0 <= val <= 109
# 0 <= snap_id < (the total number of times we call snap())
# At most 5 * 104 calls will be made to set, snap, and get.

class SnapshotArray:

    def __init__(self, length: int): # time: O(length), space: O(length)
        self.arr = [0]*length
        self.count = 0
        self.snapshots = {}

    def set(self, index: int, val: int) -> None: # O(1)
        self.arr[index] = val

    def snap(self) -> int: # time: O(length), space: O(length)
        self.count+=1
        snap_id = self.count-1
        self.snapshots[snap_id] = self.arr.copy()
        return snap_id


    def get(self, index: int, snap_id: int) -> int: # O(1)
        snap = self.snapshots[snap_id]
        return snap[index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# self.snapshots[snap_id] = self.arr is wrong because:
# This is a classic Python aliasing bug — 
# self.arr and self.snapshots[snap_id] are pointing at the exact same list object in memory, not two separate copies.
# you are not copying the contents of self.arr into a new list. 
# You're just making the dictionary entry self.snapshots[snap_id] point to the same list object that self.arr already points to 
# — like giving a second name to the same box, not making a duplicate box. Assignment in Python (x = y) for mutable objects like lists never copies; 
# it just binds a new reference to the existing object.



# OPTIMISED SOLUTION

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.snapshots = {}
        # intially each element = 0
        for i in range(length):
            self.snapshots[i] = [(0,0)]

    def set(self, index: int, val: int) -> None:
        self.snapshots[index].append((self.snap_id, val))


    def snap(self) -> int:
        self.snap_id+=1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap = self.snapshots[index]
        # binary search on snap_id (as they will be in sorted order), 
        # also there could be multiple values for the same snap_id for an index
        # for example {1: [(0,2), (0,3), (0,5), (0,2), (1,5)]}
        l = 0
        r = len(snap)-1
        res = 0
        while l<=r:
            mid = (l+r)//2
            if snap[mid][0]==snap_id:
                res = snap[mid][1]
                l=mid+1
            elif snap[mid][0] < snap_id:
                res = snap[mid][1] # for the edge case discussed below
                l=mid+1
            else:
                r=mid-1
        return res


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# Edge case consideration, if current snap id is not found, simply return the value at that index for any of the previous snap ids:

# Input
# ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
# [[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
# Output
# [null,null,0,1,2,15,3,4,15]
# Expected
# [null,null,0,1,2,15,3,4,15]

# When there's no entry with a tag exactly equal to the queried snap_id. Your set(0, 15) recorded the change under tag 0 
# (since it happened before any snap() call bumped self.snap_id). Later, snap() gets called three times, producing snapshot IDs 0, 1, 2 
# — none of which triggers a new set, so no new tags ever get added to snapshots[0]. When you then call get(0, 2), 
# you're asking "what was index 0's value as of snapshot 2?" — 
# the correct answer is "whatever the most recent set was, as long as it happened at or before snapshot 2's tag."