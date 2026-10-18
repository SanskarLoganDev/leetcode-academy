# 588. Design In-Memory File System

# Design a data structure that simulates an in-memory file system.

# Implement the FileSystem class:

# FileSystem() Initializes the object of the system.
# List<String> ls(String path)
# If path is a file path, returns a list that only contains this file's name.
# If path is a directory path, returns the list of file and directory names in this directory.
# The answer should in lexicographic order.
# void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
# void addContentToFile(String filePath, String content)
# If filePath does not exist, creates that file containing given content.
# If filePath already exists, appends the given content to original content.
# String readContentFromFile(String filePath) Returns the content in the file at filePath.
 

# Example 1:

# Input
# ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
# [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
# Output
# [null, [], null, null, ["a"], "hello"]

# Explanation
# FileSystem fileSystem = new FileSystem();
# fileSystem.ls("/");                         // return []
# fileSystem.mkdir("/a/b/c");
# fileSystem.addContentToFile("/a/b/c/d", "hello");
# fileSystem.ls("/");                         // return ["a"]
# fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
 

# Constraints:

# 1 <= path.length, filePath.length <= 100
# path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
# You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
# You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
# You can assume that the parent directory for the file in addContentToFile will exist.
# 1 <= content.length <= 50
# At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.

# For complexity:
# L = number of characters in the input path string, e.g. "/a/b/c/d" has length 8
# D = number of path components, e.g. "/a/b/c/d" has 4 components: a, b, c, d
# K = number of immediate children inside the directory being listed
# F = current number of characters already stored in a file
# C = number of characters in the new content being appended

class TrieNode:
    def __init__(self): # earlier I used hasFile for a directory that has files but it is not useful here
        self.children = {}

class FileSystem:

    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> list[str]: # Time: O(L + K log K), Space: O(L + K). O(L) to split/traverse the path, O(K log K) to sort the K immediate child names in that directory
        cur = self.root
        if path=="/":
           return sorted(cur.children.keys())
        path = path.split("/")[1:]
        for d in path:
            if isinstance(cur.children[d], str): # checking if the children is a trienode or string, and if its string, simply return it as string cannot have further nodes
                return [d]
            cur = cur.children[d]
        return sorted(cur.children.keys())

    def mkdir(self, path: str) -> None: # Time: O(L), Space: O(L)
        cur = self.root
        path = path.split("/")[1:]
        for d in path:
            if d not in cur.children:
                cur.children[d] = TrieNode()
            cur = cur.children[d]
# So if the existing file contains F characters and you're appending C characters, Python has to construct a new string:
# old content + new content
# which takes:
# Space: O(F + C)
    def addContentToFile(self, filePath: str, content: str) -> None: # Time: O(L + F + C), O(L) to process/traverse the path, O(F + C) to create the new concatenated Python string when appending content
        cur = self.root
        path = filePath.split("/")[1:]
        # just traversing the directories
        for i in range(len(path)-1):
            d = path[i]
            cur = cur.children[d]

        # here hasfile does not ensure that this directory won't have other directories within it
        filename = path[-1]
        # right now cur is at the parent directory of the file
        if filename not in cur.children:
            cur.children[filename] = content
        else:
            cur.children[filename]+= content

    def readContentFromFile(self, filePath: str) -> str: # Time: O(L), Space: O(L)
        cur = self.root
        path = filePath.split("/")[1:]
        # just traversing the directories
        for i in range(len(path)-1):
            d = path[i]
            cur = cur.children[d]

        filename = path[-1]
        return cur.children[filename]



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)