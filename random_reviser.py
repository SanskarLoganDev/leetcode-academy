neetcode_150 = {
    # Arrays & Hashing
    1:  "Contains Duplicate",
    2:  "Valid Anagram",
    3:  "Two Sum",
    4:  "Group Anagrams",
    5:  "Top K Frequent Elements",
    6:  "Encode and Decode Strings",
    7:  "Product of Array Except Self",
    8:  "Valid Sudoku",
    9:  "Longest Consecutive Sequence",

    # Two Pointers
    10: "Valid Palindrome",
    11: "Two Sum II - Input Array Is Sorted",
    12: "3Sum",
    13: "Container With Most Water",
    14: "Trapping Rain Water",

    # Sliding Window
    15: "Best Time to Buy and Sell Stock",
    16: "Longest Substring Without Repeating Characters",
    17: "Longest Repeating Character Replacement",
    18: "Permutation in String",
    19: "Minimum Window Substring",
    20: "Sliding Window Maximum",

    # Stack
    21: "Valid Parentheses",
    22: "Min Stack",
    23: "Evaluate Reverse Polish Notation",
    24: "Generate Parentheses",
    25: "Daily Temperatures",
    26: "Car Fleet",
    27: "Largest Rectangle in Histogram",

    # Binary Search
    28: "Binary Search",
    29: "Search a 2D Matrix",
    30: "Koko Eating Bananas",
    31: "Find Minimum in Rotated Sorted Array",
    32: "Search in Rotated Sorted Array",
    33: "Time Based Key-Value Store",
    34: "Median of Two Sorted Arrays",

    # Linked List
    35: "Reverse Linked List",
    36: "Merge Two Sorted Lists",
    37: "Reorder List",
    38: "Remove Nth Node From End of List",
    39: "Copy List with Random Pointer",
    40: "Add Two Numbers",
    41: "Linked List Cycle",
    42: "Find the Duplicate Number",
    43: "LRU Cache",
    44: "Merge K Sorted Lists",
    45: "Reverse Nodes in K-Group",

    # Trees
    46: "Invert Binary Tree",
    47: "Maximum Depth of Binary Tree",
    48: "Diameter of Binary Tree",
    49: "Balanced Binary Tree",
    50: "Same Tree",
    51: "Subtree of Another Tree",
    52: "Lowest Common Ancestor of a Binary Search Tree",
    53: "Binary Tree Level Order Traversal",
    54: "Binary Tree Right Side View",
    55: "Count Good Nodes in Binary Tree",
    56: "Validate Binary Search Tree",
    57: "Kth Smallest Element in a BST",
    58: "Construct Binary Tree from Preorder and Inorder Traversal",
    59: "Binary Tree Maximum Path Sum",
    60: "Serialize and Deserialize Binary Tree",

    # Heap / Priority Queue
    61: "Kth Largest Element in a Stream",
    62: "Last Stone Weight",
    63: "K Closest Points to Origin",
    64: "Kth Largest Element in an Array",
    65: "Task Scheduler",
    66: "Design Twitter",
    67: "Find Median from Data Stream",

    # Backtracking
    68: "Subsets",
    69: "Combination Sum",
    70: "Permutations",
    71: "Subsets II",
    72: "Combination Sum II",
    73: "Word Search",
    74: "Palindrome Partitioning",
    75: "Letter Combinations of a Phone Number",
    76: "N-Queens",

    # Tries
    77: "Implement Trie (Prefix Tree)",
    78: "Design Add and Search Words Data Structure",
    79: "Word Search II",

    # Graphs
    80: "Number of Islands",
    81: "Clone Graph",
    82: "Max Area of Island",
    83: "Pacific Atlantic Water Flow",
    84: "Surrounded Regions",
    85: "Rotting Oranges",
    86: "Walls and Gates",
    87: "Course Schedule",
    88: "Course Schedule II",
    89: "Redundant Connection",
    90: "Number of Connected Components in an Undirected Graph",
    91: "Graph Valid Tree",
    92: "Word Ladder",

    # Advanced Graphs
    93: "Reconstruct Itinerary",
    94: "Min Cost to Connect All Points",
    95: "Network Delay Time",
    96: "Swim in Rising Water",
    97: "Alien Dictionary",
    98: "Cheapest Flights Within K Stops",

    # 1-D Dynamic Programming
    99:  "Climbing Stairs",
    100: "Min Cost Climbing Stairs",
    101: "House Robber",
    102: "House Robber II",
    103: "Longest Palindromic Substring",
    104: "Palindromic Substrings",
    105: "Decode Ways",
    106: "Coin Change",
    107: "Maximum Product Subarray",
    108: "Word Break",
    109: "Longest Increasing Subsequence",
    110: "Partition Equal Subset Sum",

    # 2-D Dynamic Programming
    111: "Unique Paths",
    112: "Longest Common Subsequence",
    113: "Best Time to Buy and Sell Stock with Cooldown",
    114: "Coin Change II",
    115: "Target Sum",
    116: "Interleaving String",
    117: "Longest Increasing Path in a Matrix",
    118: "Distinct Subsequences",
    119: "Edit Distance",
    120: "Burst Balloons",
    121: "Regular Expression Matching",

    # Greedy
    122: "Maximum Subarray",
    123: "Jump Game",
    124: "Jump Game II",
    125: "Gas Station",
    126: "Hand of Straights",
    127: "Merge Triplets to Form Target Triplet",
    128: "Partition Labels",
    129: "Valid Parenthesis String",

    # Intervals
    130: "Insert Interval",
    131: "Merge Intervals",
    132: "Non-overlapping Intervals",
    133: "Meeting Rooms",
    134: "Meeting Rooms II",
    135: "Minimum Interval to Include Each Query",

    # Math & Geometry
    136: "Rotate Image",
    137: "Spiral Matrix",
    138: "Set Matrix Zeroes",
    139: "Happy Number",
    140: "Plus One",
    141: "Pow(x, n)",
    142: "Multiply Strings",
    143: "Detect Squares",

    # Bit Manipulation
    144: "Single Number",
    145: "Number of 1 Bits",
    146: "Counting Bits",
    147: "Reverse Bits",
    148: "Missing Number",
    149: "Sum of Two Integers",
    150: "Reverse Integer",
}

import random

# Pick a random problem
num, name = random.choice(list(neetcode_150.items()))
print(f"Problem #{num}: {name}")

# Pick from a specific range (e.g., only Arrays & Hashing: 1-9)
num, name = random.choice(list(neetcode_150.items())[140:151])
print(f"Problem #{num}: {name}")