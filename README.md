# LeetCode Academy

A structured collection of LeetCode solutions in Python, organized by difficulty and topic. Includes standalone easy/medium problem sets and a complete [NeetCode 150](https://neetcode.io/) track.

---

## Repository Structure

```
leetcode-academy/
├── easy/                   # Easy-level problems by topic
├── medium/                 # Medium-level problems by topic
├── hard/                   # Hard-level problems by topic
├── Interview-Questions/    # Interview questions by company
└── Neetcode 150/           # NeetCode 150 curriculum by category
```

---

## DSA Topics Covered

### 1. Arrays & Lists
**Core idea:** Contiguous memory, O(1) index access. Most problems involve traversal, prefix sums, or two-pointer/sliding-window techniques.

Key patterns:
- Prefix sums for range queries
- Two pointers for sorted arrays (e.g., 3Sum, container with most water)
- In-place modification (remove duplicates, move zeros)
- Binary search on sorted/rotated arrays

Problems: `two_sum`, `product_of_array_except_self`, `valid_sudoku`, `container_with_most_water`, `3sum`, `search_in_rotated_sorted_array`, `koko_eating_bananas`, `find_min_in_rotated_sorted_array`

---

### 2. Strings
**Core idea:** Character sequences. Problems often involve parsing, pattern matching, or stack-based processing.

Key patterns:
- Hash maps for character frequency
- Stack for balanced parentheses / expression evaluation
- Two pointers for palindrome / reversal
- Sliding window for substring problems

Problems: `valid_anagram`, `longest_substring_without_repeating_chars`, `permutation_in_string`, `minimum_window_substring`, `reverse_words_in_string`, `simplify_path`, `basic_calculator_2`

---

### 3. Hash Maps & Hash Sets
**Core idea:** O(1) average lookup/insert. Used for frequency counting, deduplication, and fast membership checks.

Key patterns:
- Frequency maps for anagram/duplicate detection
- Value-to-index maps (Two Sum pattern)
- Sets for O(1) existence checks

Problems: `group_anagrams`, `top_k_frequent_elements`, `longest_consecutive_sequence`, `contains_duplicate`, `word_subsets`, `roman_to_integer`

---

### 4. Two Pointers
**Core idea:** Use two indices moving toward each other or in the same direction to avoid O(n²) brute force on sorted arrays or strings.

Key patterns:
- Left/right convergence on sorted arrays
- Fast/slow pointers on linked lists (cycle detection)
- Partition-based approaches

Problems: `valid_palindrome`, `two_sum_II`, `3sum`, `container_with_most_water`, `trapping_rain_water`

---

### 5. Sliding Window
**Core idea:** Maintain a window of elements, expanding/shrinking to satisfy a constraint, achieving O(n) for substring/subarray problems.

Key patterns:
- Fixed-size window (moving average, x-sum of subarrays)
- Variable-size window with a frequency map
- Monotonic deque for window maximum

Problems: `best_time_to_buy_and_sell_stock`, `longest_substring_without_repeating_chars`, `longest_repeating_char_replacement`, `permutation_in_string`, `minimum_window_substring`, `sliding_window_maximum`

---

### 6. Stacks & Queues
**Core idea:** LIFO (stack) and FIFO (queue) for ordered processing. Monotonic stacks are useful for "next greater/smaller element" problems.

Key patterns:
- Monotonic stack for temperature/histogram/car fleet problems
- Stack for expression evaluation and parenthesis matching
- Queue/deque for BFS or sliding window maximum

Problems: `valid_parentheses`, `min_stack`, `evaluate_reverse_polish_notation`, `daily_temperatures`, `car_fleet`, `largest_rectangle_in_histogram`, `generate_parentheses`, `baseball_game`

---

### 7. Linked Lists
**Core idea:** Node chains with O(1) insert/delete but O(n) access. Problems frequently use dummy nodes, fast/slow pointers, or reversal.

Key patterns:
- Dummy head node to simplify edge cases
- Fast/slow pointer (cycle detection, find middle)
- In-place reversal (iterative and recursive)
- Merge patterns for sorted lists

Problems: `reverse_linked_list`, `merge_two_linked_lists`, `linked_list_cycle`, `reorder_list`, `remove_nth_node_from_end`, `copy_list_with_random_pointer`, `add_two_numbers`, `LRU_cache`, `merge_k_sorted_lists`, `reverse_nodes_in_k_group`

---

### 8. Binary Search
**Core idea:** Halve the search space each step for O(log n). Applies to sorted arrays, search spaces, and "minimise the maximum" problems.

Key patterns:
- Classic binary search on index
- Search on answer space (e.g., find minimum feasible value)
- Variants: rotated arrays, 2D matrix search

Problems: `binary_search`, `search_a_2D_matrix`, `koko_eating_bananas`, `find_min_in_rotated_sorted_array`, `search_in_rotated_sorted_array`, `time-based_key_value_store`, `median_of_two_sorted_arrays`

---

### 9. Trees
**Core idea:** Hierarchical node structure. Problems use DFS (preorder/inorder/postorder) or BFS (level order).

Key patterns:
- Recursive DFS for path sums, depth, LCA
- BFS / level-order traversal using a queue
- BST property: left < root < right (inorder gives sorted output)
- Serialize/deserialize for tree reconstruction

Problems: `invert_binary_tree`, `max_depth`, `diameter_of_binary_tree`, `balanced_binary_tree`, `same_tree`, `subtree_of_another_tree`, `LCA_in_BST`, `binary_tree_level_order_traversal`, `binary_tree_right_side_view`, `valid_bst`, `kth_smallest_in_BST`, `construct_from_preorder_inorder`, `binary_tree_maximum_path_sum`, `serialize_deserialize`

---

### 10. Heap / Priority Queue
**Core idea:** Efficiently get min or max in O(log n). Python's `heapq` is a min-heap; negate values for max-heap behavior.

Key patterns:
- Top-K elements using a heap of size K
- Two heaps (min + max) for median tracking
- Lazy deletion for design problems

Problems: `kth_largest_element`, `k_closest_points_to_origin`, `last_stone_weight`, `task_scheduler`, `design_twitter`, `find_median_from_data_stream`, `kth_largest_element_in_stream`

---

### 11. Graphs
**Core idea:** Nodes and edges. Solved with DFS, BFS, or Union-Find depending on connectivity/ordering requirements.

Key patterns:
- BFS for shortest path in unweighted graphs
- DFS for connected components, cycle detection
- Topological sort (DFS or Kahn's BFS) for dependency ordering
- Union-Find for dynamic connectivity

Problems: `number_of_islands`, `max_area_of_island`, `clone_graph`, `walls_and_gates`, `rotting_oranges`, `pacific_atlantic_water_flow`, `surrounded_regions`, `course_schedule`, `course_schedule_2`, `number_of_connected_components`, `graph_valid_tree`, `redundant_connection`, `word_ladder`, `number_of_provinces`

---

### 12. Advanced Graphs
**Core idea:** Weighted graph algorithms for shortest path and minimum spanning tree.

Key patterns:
- Dijkstra's algorithm (min-heap) for single-source shortest path
- Bellman-Ford for graphs with negative weights / limited hops
- Prim's / Kruskal's for MST (min cost to connect all points)
- Eulerian path reconstruction (Hierholzer's algorithm)

Problems: `network_delay_time`, `cheapest_flights_with_k_stops`, `min_cost_to_connect_all_points`, `swim_in_rising_water`, `reconstruct_itinerary`, `alien_dictionary`

---

### 13. Trie (Prefix Tree)
**Core idea:** Tree where each node represents a character prefix. Enables O(m) word insert/search (m = word length).

Key patterns:
- `TrieNode` with a `children` dict and `is_end` flag
- DFS on trie for wildcard search
- Backtracking on trie + board for Word Search II

Problems: `implement_trie_prefix_tree`, `design_add_and_search_words`, `word_search2`

---

### 14. Backtracking
**Core idea:** Build a solution incrementally, abandoning ("backtracking") as soon as a constraint is violated.

Key patterns:
- Choose → Explore → Unchoose
- Avoid duplicates by sorting + skipping equal siblings
- Pruning with early termination

Problems: `subsets`, `subsets2`, `permutations`, `combination_sum`, `combination_sum2`, `generate_parentheses`, `word_search`, `palindrome_partitioning`, `letter_combinations_phone_number`, `N-Queens`

---

### 15. Intervals
**Core idea:** Sort by start time, then sweep through to merge, count, or schedule.

Key patterns:
- Merge overlapping intervals (sort + greedy sweep)
- Insert interval with binary search
- Meeting rooms: counting concurrent intervals with a min-heap

Problems: `insert_interval`, `merge_intervals`, `non_overlapping_intervals`, `meeting_rooms`, `meeting_rooms_2`, `minimum_interval_to_include_each_query`

---

### 16. Greedy
**Core idea:** Make the locally optimal choice at each step. Works when local optima lead to global optima.

Key patterns:
- Kadane's algorithm for maximum subarray
- Jump game: track max reachable index
- Activity selection / interval scheduling

Problems: `maximum_subarray`, `jump_game`, `jump_game2`

---

### 17. 1D Dynamic Programming
**Core idea:** Break a problem into overlapping subproblems. Cache results (memoization/tabulation) to avoid recomputation.

Key patterns:
- Bottom-up DP table with base cases
- State: `dp[i]` = best answer using first `i` elements
- Common recurrences: LIS, knapsack, decode ways

Problems: `climbing_stairs`, `min_cost_climbing_stairs`, `house_robber`, `house_robber_2`, `longest_palindromic_substring`, `palindromic_substrings`, `decode_ways`, `coin_change`, `maximum_product_subarray`, `word_break`, `longest_increasing_subsequence`, `partition_equal_subset_sum`

---

### 18. 2D Dynamic Programming
**Core idea:** Extend 1D DP to a 2D grid or two-sequence state. Common in string comparison and path-counting problems.

Key patterns:
- `dp[i][j]` depends on `dp[i-1][j]`, `dp[i][j-1]`, `dp[i-1][j-1]`
- Interval DP for burst balloons / regex matching
- Matrix DP for unique paths, longest increasing path

Problems: `unique_paths`, `longest_common_subsequence`, `best_time_to_buy_sell_stock_cooldown`, `coin_change2`, `target_sum`, `interleaving_string`, `edit_distance`, `longest_increasing_path_in_matrix`, `distinct_subsequences`, `burst_balloons`, `regular_expression_matching`

---

### 19. Bit Manipulation
**Core idea:** Operate directly on binary representations for O(1) tricks.

Key patterns:
- XOR to find a unique number (pairs cancel out)
- `n & (n-1)` removes the lowest set bit
- Left/right shifts for powers of two
- Mask-based operations for subsets

Problems: `single_number`, `number_of_1_bits`, `counting_bits`, `reverse_bits`, `missing_number`, `sum_of_two_integers`, `reverse_integer`

---

### 20. Math & Geometry
**Core idea:** Number theory, modular arithmetic, and matrix transformations.

Key patterns:
- Layer-by-layer rotation for matrix problems
- Spiral / zigzag traversal
- Fast exponentiation (binary exponentiation)
- String multiplication (grade-school multiply)

Problems: `rotate_image`, `spiral_matrix`, `set_matrix_zeroes`, `pow`, `multiply_strings`, `detect_squares`, `happy_number`, `plus_one`

---

### 21. Sorting
**Core idea:** Ordering elements to enable binary search, greedy decisions, or simplified comparisons.

Key patterns:
- Custom comparator with `key=` or `functools.cmp_to_key`
- Counting sort for bounded integer ranges
- Partial sort with `heapq.nlargest` / `nsmallest`

Problems: `largest_number_after_swapping`, `top_k_frequent_elements`, `top_k_frequent_words`

---

### 22. Dynamic Programming (Easy)
**Core idea:** Same as 1D/2D DP above, applied to simpler problem structures.

Problems: `pascal_triangle`, `divisor_game`

---

## Progress Summary

| Category | Problems Solved |
|---|---|
| Arrays & Lists | ~30+ |
| Strings | ~20+ |
| Hash Maps / Sets | ~10+ |
| Two Pointers | 5 |
| Sliding Window | 6 |
| Stacks & Queues | ~12 |
| Linked Lists | ~11 |
| Binary Search | 7 |
| Trees | ~15+ |
| Heap | 7 |
| Graphs | ~14 |
| Advanced Graphs | 6 |
| Trie | 3 |
| Backtracking | 10 |
| Intervals | 6 |
| Greedy | 3 |
| 1D Dynamic Programming | 12 |
| 2D Dynamic Programming | 11 |
| Bit Manipulation | 7 |
| Math & Geometry | 8 |

---

## Language & Tools

- **Language:** Python 3
- **Curriculum:** [NeetCode 150](https://neetcode.io/practice)
