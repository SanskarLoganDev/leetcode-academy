from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

problems = [
    # Arrays & Hashing
    {"n": 1,  "name": "Contains Duplicate",                   "topic": "Arrays & Hashing",        "diff": "easy"},
    {"n": 2,  "name": "Valid Anagram",                        "topic": "Arrays & Hashing",        "diff": "easy"},
    {"n": 3,  "name": "Two Sum",                              "topic": "Arrays & Hashing",        "diff": "easy"},
    {"n": 4,  "name": "Group Anagrams",                       "topic": "Arrays & Hashing",        "diff": "medium"},
    {"n": 5,  "name": "Top K Frequent Elements",              "topic": "Arrays & Hashing",        "diff": "medium"},
    {"n": 6,  "name": "Encode and Decode Strings",            "topic": "Arrays & Hashing",        "diff": "medium"},
    {"n": 7,  "name": "Product of Array Except Self",         "topic": "Arrays & Hashing",        "diff": "medium"},
    {"n": 8,  "name": "Valid Sudoku",                         "topic": "Arrays & Hashing",        "diff": "medium"},
    {"n": 9,  "name": "Longest Consecutive Sequence",         "topic": "Arrays & Hashing",        "diff": "medium"},
    # Two Pointers
    {"n": 10, "name": "Valid Palindrome",                     "topic": "Two Pointers",            "diff": "easy"},
    {"n": 11, "name": "Two Sum II - Input Array Is Sorted",   "topic": "Two Pointers",            "diff": "medium"},
    {"n": 12, "name": "3Sum",                                 "topic": "Two Pointers",            "diff": "medium"},
    {"n": 13, "name": "Container With Most Water",            "topic": "Two Pointers",            "diff": "medium"},
    {"n": 14, "name": "Trapping Rain Water",                  "topic": "Two Pointers",            "diff": "hard"},
    # Sliding Window
    {"n": 15, "name": "Best Time to Buy and Sell Stock",                      "topic": "Sliding Window", "diff": "easy"},
    {"n": 16, "name": "Longest Substring Without Repeating Characters",       "topic": "Sliding Window", "diff": "medium"},
    {"n": 17, "name": "Longest Repeating Character Replacement",              "topic": "Sliding Window", "diff": "medium"},
    {"n": 18, "name": "Permutation in String",                                "topic": "Sliding Window", "diff": "medium"},
    {"n": 19, "name": "Minimum Window Substring",                             "topic": "Sliding Window", "diff": "hard"},
    {"n": 20, "name": "Sliding Window Maximum",                               "topic": "Sliding Window", "diff": "hard"},
    # Stack
    {"n": 21, "name": "Valid Parentheses",                    "topic": "Stack", "diff": "easy"},
    {"n": 22, "name": "Min Stack",                            "topic": "Stack", "diff": "medium"},
    {"n": 23, "name": "Evaluate Reverse Polish Notation",     "topic": "Stack", "diff": "medium"},
    {"n": 24, "name": "Generate Parentheses",                 "topic": "Stack", "diff": "medium"},
    {"n": 25, "name": "Daily Temperatures",                   "topic": "Stack", "diff": "medium"},
    {"n": 26, "name": "Car Fleet",                            "topic": "Stack", "diff": "medium"},
    {"n": 27, "name": "Largest Rectangle in Histogram",       "topic": "Stack", "diff": "hard"},
    # Binary Search
    {"n": 28, "name": "Binary Search",                        "topic": "Binary Search", "diff": "easy"},
    {"n": 29, "name": "Search a 2D Matrix",                   "topic": "Binary Search", "diff": "medium"},
    {"n": 30, "name": "Koko Eating Bananas",                  "topic": "Binary Search", "diff": "medium"},
    {"n": 31, "name": "Find Minimum in Rotated Sorted Array", "topic": "Binary Search", "diff": "medium"},
    {"n": 32, "name": "Search in Rotated Sorted Array",       "topic": "Binary Search", "diff": "medium"},
    {"n": 33, "name": "Time Based Key-Value Store",           "topic": "Binary Search", "diff": "medium"},
    {"n": 34, "name": "Median of Two Sorted Arrays",          "topic": "Binary Search", "diff": "hard"},
    # Linked List
    {"n": 35, "name": "Reverse Linked List",                  "topic": "Linked List", "diff": "easy"},
    {"n": 36, "name": "Merge Two Sorted Lists",               "topic": "Linked List", "diff": "easy"},
    {"n": 37, "name": "Reorder List",                         "topic": "Linked List", "diff": "medium"},
    {"n": 38, "name": "Remove Nth Node From End of List",     "topic": "Linked List", "diff": "medium"},
    {"n": 39, "name": "Copy List with Random Pointer",        "topic": "Linked List", "diff": "medium"},
    {"n": 40, "name": "Add Two Numbers",                      "topic": "Linked List", "diff": "medium"},
    {"n": 41, "name": "Linked List Cycle",                    "topic": "Linked List", "diff": "easy"},
    {"n": 42, "name": "Find the Duplicate Number",            "topic": "Linked List", "diff": "medium"},
    {"n": 43, "name": "LRU Cache",                            "topic": "Linked List", "diff": "medium"},
    {"n": 44, "name": "Merge K Sorted Lists",                 "topic": "Linked List", "diff": "hard"},
    {"n": 45, "name": "Reverse Nodes in K-Group",             "topic": "Linked List", "diff": "hard"},
    # Trees
    {"n": 46, "name": "Invert Binary Tree",                                         "topic": "Trees", "diff": "easy"},
    {"n": 47, "name": "Maximum Depth of Binary Tree",                               "topic": "Trees", "diff": "easy"},
    {"n": 48, "name": "Diameter of Binary Tree",                                    "topic": "Trees", "diff": "easy"},
    {"n": 49, "name": "Balanced Binary Tree",                                       "topic": "Trees", "diff": "easy"},
    {"n": 50, "name": "Same Tree",                                                  "topic": "Trees", "diff": "easy"},
    {"n": 51, "name": "Subtree of Another Tree",                                    "topic": "Trees", "diff": "easy"},
    {"n": 52, "name": "Lowest Common Ancestor of a Binary Search Tree",             "topic": "Trees", "diff": "medium"},
    {"n": 53, "name": "Binary Tree Level Order Traversal",                          "topic": "Trees", "diff": "medium"},
    {"n": 54, "name": "Binary Tree Right Side View",                                "topic": "Trees", "diff": "medium"},
    {"n": 55, "name": "Count Good Nodes in Binary Tree",                            "topic": "Trees", "diff": "medium"},
    {"n": 56, "name": "Validate Binary Search Tree",                                "topic": "Trees", "diff": "medium"},
    {"n": 57, "name": "Kth Smallest Element in a BST",                              "topic": "Trees", "diff": "medium"},
    {"n": 58, "name": "Construct Binary Tree from Preorder and Inorder Traversal",  "topic": "Trees", "diff": "medium"},
    {"n": 59, "name": "Binary Tree Maximum Path Sum",                               "topic": "Trees", "diff": "hard"},
    {"n": 60, "name": "Serialize and Deserialize Binary Tree",                      "topic": "Trees", "diff": "hard"},
    # Heap / Priority Queue
    {"n": 61, "name": "Kth Largest Element in a Stream",  "topic": "Heap / Priority Queue", "diff": "easy"},
    {"n": 62, "name": "Last Stone Weight",                 "topic": "Heap / Priority Queue", "diff": "easy"},
    {"n": 63, "name": "K Closest Points to Origin",       "topic": "Heap / Priority Queue", "diff": "medium"},
    {"n": 64, "name": "Kth Largest Element in an Array",  "topic": "Heap / Priority Queue", "diff": "medium"},
    {"n": 65, "name": "Task Scheduler",                   "topic": "Heap / Priority Queue", "diff": "medium"},
    {"n": 66, "name": "Design Twitter",                   "topic": "Heap / Priority Queue", "diff": "medium"},
    {"n": 67, "name": "Find Median from Data Stream",     "topic": "Heap / Priority Queue", "diff": "hard"},
    # Backtracking
    {"n": 68, "name": "Subsets",                              "topic": "Backtracking", "diff": "medium"},
    {"n": 69, "name": "Combination Sum",                      "topic": "Backtracking", "diff": "medium"},
    {"n": 70, "name": "Permutations",                         "topic": "Backtracking", "diff": "medium"},
    {"n": 71, "name": "Subsets II",                           "topic": "Backtracking", "diff": "medium"},
    {"n": 72, "name": "Combination Sum II",                   "topic": "Backtracking", "diff": "medium"},
    {"n": 73, "name": "Word Search",                          "topic": "Backtracking", "diff": "medium"},
    {"n": 74, "name": "Palindrome Partitioning",              "topic": "Backtracking", "diff": "medium"},
    {"n": 75, "name": "Letter Combinations of a Phone Number","topic": "Backtracking", "diff": "medium"},
    {"n": 76, "name": "N-Queens",                             "topic": "Backtracking", "diff": "hard"},
    # Tries
    {"n": 77, "name": "Implement Trie (Prefix Tree)",                   "topic": "Tries", "diff": "medium"},
    {"n": 78, "name": "Design Add and Search Words Data Structure",     "topic": "Tries", "diff": "medium"},
    {"n": 79, "name": "Word Search II",                                 "topic": "Tries", "diff": "hard"},
    # Graphs
    {"n": 80, "name": "Number of Islands",                                      "topic": "Graphs", "diff": "medium"},
    {"n": 81, "name": "Clone Graph",                                            "topic": "Graphs", "diff": "medium"},
    {"n": 82, "name": "Max Area of Island",                                     "topic": "Graphs", "diff": "medium"},
    {"n": 83, "name": "Pacific Atlantic Water Flow",                            "topic": "Graphs", "diff": "medium"},
    {"n": 84, "name": "Surrounded Regions",                                     "topic": "Graphs", "diff": "medium"},
    {"n": 85, "name": "Rotting Oranges",                                        "topic": "Graphs", "diff": "medium"},
    {"n": 86, "name": "Walls and Gates",                                        "topic": "Graphs", "diff": "medium"},
    {"n": 87, "name": "Course Schedule",                                        "topic": "Graphs", "diff": "medium"},
    {"n": 88, "name": "Course Schedule II",                                     "topic": "Graphs", "diff": "medium"},
    {"n": 89, "name": "Redundant Connection",                                   "topic": "Graphs", "diff": "medium"},
    {"n": 90, "name": "Number of Connected Components in an Undirected Graph",  "topic": "Graphs", "diff": "medium"},
    {"n": 91, "name": "Graph Valid Tree",                                       "topic": "Graphs", "diff": "medium"},
    {"n": 92, "name": "Word Ladder",                                            "topic": "Graphs", "diff": "hard"},
    # Advanced Graphs
    {"n": 93, "name": "Reconstruct Itinerary",              "topic": "Advanced Graphs", "diff": "hard"},
    {"n": 94, "name": "Min Cost to Connect All Points",     "topic": "Advanced Graphs", "diff": "medium"},
    {"n": 95, "name": "Network Delay Time",                 "topic": "Advanced Graphs", "diff": "medium"},
    {"n": 96, "name": "Swim in Rising Water",               "topic": "Advanced Graphs", "diff": "hard"},
    {"n": 97, "name": "Alien Dictionary",                   "topic": "Advanced Graphs", "diff": "hard"},
    {"n": 98, "name": "Cheapest Flights Within K Stops",    "topic": "Advanced Graphs", "diff": "medium"},
    # 1-D DP
    {"n": 99,  "name": "Climbing Stairs",                   "topic": "1-D Dynamic Programming", "diff": "easy"},
    {"n": 100, "name": "Min Cost Climbing Stairs",          "topic": "1-D Dynamic Programming", "diff": "easy"},
    {"n": 101, "name": "House Robber",                      "topic": "1-D Dynamic Programming", "diff": "medium"},
    {"n": 102, "name": "House Robber II",                   "topic": "1-D Dynamic Programming", "diff": "medium"},
    {"n": 103, "name": "Longest Palindromic Substring",     "topic": "1-D Dynamic Programming", "diff": "medium"},
    {"n": 104, "name": "Palindromic Substrings",            "topic": "1-D Dynamic Programming", "diff": "medium"},
    {"n": 105, "name": "Decode Ways",                       "topic": "1-D Dynamic Programming", "diff": "medium"},
    {"n": 106, "name": "Coin Change",                       "topic": "1-D Dynamic Programming", "diff": "medium"},
    {"n": 107, "name": "Maximum Product Subarray",          "topic": "1-D Dynamic Programming", "diff": "medium"},
    {"n": 108, "name": "Word Break",                        "topic": "1-D Dynamic Programming", "diff": "medium"},
    {"n": 109, "name": "Longest Increasing Subsequence",    "topic": "1-D Dynamic Programming", "diff": "medium"},
    {"n": 110, "name": "Partition Equal Subset Sum",        "topic": "1-D Dynamic Programming", "diff": "medium"},
    # 2-D DP
    {"n": 111, "name": "Unique Paths",                                      "topic": "2-D Dynamic Programming", "diff": "medium"},
    {"n": 112, "name": "Longest Common Subsequence",                        "topic": "2-D Dynamic Programming", "diff": "medium"},
    {"n": 113, "name": "Best Time to Buy and Sell Stock with Cooldown",     "topic": "2-D Dynamic Programming", "diff": "medium"},
    {"n": 114, "name": "Coin Change II",                                    "topic": "2-D Dynamic Programming", "diff": "medium"},
    {"n": 115, "name": "Target Sum",                                        "topic": "2-D Dynamic Programming", "diff": "medium"},
    {"n": 116, "name": "Interleaving String",                               "topic": "2-D Dynamic Programming", "diff": "medium"},
    {"n": 117, "name": "Longest Increasing Path in a Matrix",               "topic": "2-D Dynamic Programming", "diff": "hard"},
    {"n": 118, "name": "Distinct Subsequences",                             "topic": "2-D Dynamic Programming", "diff": "hard"},
    {"n": 119, "name": "Edit Distance",                                     "topic": "2-D Dynamic Programming", "diff": "medium"},
    {"n": 120, "name": "Burst Balloons",                                    "topic": "2-D Dynamic Programming", "diff": "hard"},
    {"n": 121, "name": "Regular Expression Matching",                       "topic": "2-D Dynamic Programming", "diff": "hard"},
    # Greedy
    {"n": 122, "name": "Maximum Subarray",                      "topic": "Greedy", "diff": "medium"},
    {"n": 123, "name": "Jump Game",                             "topic": "Greedy", "diff": "medium"},
    {"n": 124, "name": "Jump Game II",                          "topic": "Greedy", "diff": "medium"},
    {"n": 125, "name": "Gas Station",                           "topic": "Greedy", "diff": "medium"},
    {"n": 126, "name": "Hand of Straights",                     "topic": "Greedy", "diff": "medium"},
    {"n": 127, "name": "Merge Triplets to Form Target Triplet", "topic": "Greedy", "diff": "medium"},
    {"n": 128, "name": "Partition Labels",                      "topic": "Greedy", "diff": "medium"},
    {"n": 129, "name": "Valid Parenthesis String",              "topic": "Greedy", "diff": "medium"},
    # Intervals
    {"n": 130, "name": "Insert Interval",                       "topic": "Intervals", "diff": "medium"},
    {"n": 131, "name": "Merge Intervals",                       "topic": "Intervals", "diff": "medium"},
    {"n": 132, "name": "Non-overlapping Intervals",             "topic": "Intervals", "diff": "medium"},
    {"n": 133, "name": "Meeting Rooms",                         "topic": "Intervals", "diff": "easy"},
    {"n": 134, "name": "Meeting Rooms II",                      "topic": "Intervals", "diff": "medium"},
    {"n": 135, "name": "Minimum Interval to Include Each Query","topic": "Intervals", "diff": "hard"},
    # Math & Geometry
    {"n": 136, "name": "Rotate Image",      "topic": "Math & Geometry", "diff": "medium"},
    {"n": 137, "name": "Spiral Matrix",     "topic": "Math & Geometry", "diff": "medium"},
    {"n": 138, "name": "Set Matrix Zeroes", "topic": "Math & Geometry", "diff": "medium"},
    {"n": 139, "name": "Happy Number",      "topic": "Math & Geometry", "diff": "easy"},
    {"n": 140, "name": "Plus One",          "topic": "Math & Geometry", "diff": "easy"},
    {"n": 141, "name": "Pow(x, n)",         "topic": "Math & Geometry", "diff": "medium"},
    {"n": 142, "name": "Multiply Strings",  "topic": "Math & Geometry", "diff": "medium"},
    {"n": 143, "name": "Detect Squares",    "topic": "Math & Geometry", "diff": "medium"},
    # Bit Manipulation
    {"n": 144, "name": "Single Number",         "topic": "Bit Manipulation", "diff": "easy"},
    {"n": 145, "name": "Number of 1 Bits",      "topic": "Bit Manipulation", "diff": "easy"},
    {"n": 146, "name": "Counting Bits",         "topic": "Bit Manipulation", "diff": "easy"},
    {"n": 147, "name": "Reverse Bits",          "topic": "Bit Manipulation", "diff": "easy"},
    {"n": 148, "name": "Missing Number",        "topic": "Bit Manipulation", "diff": "easy"},
    {"n": 149, "name": "Sum of Two Integers",   "topic": "Bit Manipulation", "diff": "medium"},
    {"n": 150, "name": "Reverse Integer",       "topic": "Bit Manipulation", "diff": "medium"},
]

TOPICS = sorted(set(p["topic"] for p in problems))


@app.route("/")
def index():
    return render_template("index.html", topics=TOPICS)


@app.route("/random")
def get_random():
    from flask import request
    diff  = request.args.get("diff",  "all")
    topic = request.args.get("topic", "all")

    pool = [
        p for p in problems
        if (diff  == "all" or p["diff"]  == diff)
        and (topic == "all" or p["topic"] == topic)
    ]

    if not pool:
        return jsonify({"error": "No problems match this combination."}), 404

    picked = random.choice(pool)
    slug = picked["name"].lower()
    for ch in " /(),.":
        slug = slug.replace(ch, "-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    slug = slug.strip("-")

    return jsonify({
        "n":     picked["n"],
        "name":  picked["name"],
        "topic": picked["topic"],
        "diff":  picked["diff"],
        "pool":  len(pool),
        "url":   f"https://leetcode.com/problems/{slug}/",
    })


if __name__ == "__main__":
    print("Running at http://127.0.0.1:5000")
    app.run(debug=True)