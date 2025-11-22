# SecretKey
# Problem Description

# Rupa was on the internet when she found a tough challenge called "Can you guess the Secret Key?" Let's see what it is.

# In this challenge, Rupa is presented with an N×M grid of English letters. Hidden in this grid is a secret key, a word of length T. The key can start at any cell, and each next letter must be reached by moving exactly one step up, down, left, or right (no diagonals), without revisiting any cell. Each move takes one second, so the first letter is at time 1, the second at time 2, and so on.

# Instead of the exact positions of the key's letters, you are given clues. Each clue tells you that at time t, the next letter is not in a specific sub grid (from (x1, y1) to (x2, y2), 1-based indexing).

# Using these clues, Rupa needs to deduce the secret key from the grid. Help Rupa.

# Your task:

# If the clues uniquely determine the secret key, print the key.
# If there are multiple possible keys, or if any letter cannot be found based on the clues, print "Not enough clues".

# For example, consider a 3×3 grid. If there is a clue stating that at time T, the next letter is not present in the sub grid from (1, 1) to (3, 3) (using 1-based indexing), it implies that the letter does not exist anywhere in the grid at time T seconds.

# Constraints

# 1 <= N, M <= 25

# 1 <= T <= 25

# 1 <= I <= 30

# The grid will have only alphabets of any case.

# Input

# First line: Two integers N and M (1 <= N, M <= 25) - grid size.
# Next N lines: Each contains M space-separated letters - the grid.
# Next line: Integer T (1 <= T <= 25) - length of the secret key and also the number of time units required to form the secret word.
# Next line: Integer I (1 <= I <= 30) - number of clues.
# Next 2×I lines: For each clue:
# Line 1: Integer t (1 <= t <= T) - time step.
# Line 2: Four integers x1 y1 x2 y2 - top-left and bottom-right corners of the sub grid where the letter at time t is not located.
# Output

# Print the secret key if it can be uniquely determined.
# Otherwise, print "Not enough clues".
# Notes

# You cannot revisit any cell.
# If a clue excludes the entire grid for a time step, print "Not enough clues ".
# Time Limit (secs)
# 1

# Examples

# Example 1

# Input

# 4 4

# A b c D

# e F g h

# i J k l

# m n o P

# 4

# 8

# 1

# 1 1 1 2

# 1

# 1 1 4 1

# 1

# 2 1 4 4

# 1

# 2 4 4 4

# 2

# 1 1 4 3

# 3

# 1 1 4 3

# 3

# 3 1 4 4

# 4

# 1 1 4 3

# Output

# cDhl

# Explanation

# According to the given details, at time T = 1, the character won't be in the sub grids from (1,1) to (1,2), (1,1) to (4,1), (2,1) to (4,4) and (2,4) to (4,4). Thus, the cells in which the character can be present at time T = 1 are (1,3) and (1,4). At time T = 2, the character won't be in the sub grid from (1,1) to (4,3), so the cells where the character can be present are (1,4), (2,4), (3,4), and (4,4). Likewise, at time T = 3, the cells in which the character can be present are (1,4) and (2,4), and at time T = 4, the valid positions are (1,4), (2,4), (3,4), and (4,4).

# Given that the character can only move up, down, left, or right, let's assume the starting cell at T = 1 is (1,3). From (1,3), we can move right to (1,4), then down to (2,4), and again down to (3,4). According to the clues, this is a valid path, and no other valid traversals are found. Hence, the characters in the visited cells form the secret key, which is cDhl.

# Example 2

# Input

# 3 3

# v a i

# s h n

# a v i

# 3

# 2

# 1

# 1 1 2 2

# 3

# 2 1 3 3

# Output

# Not enough clues

# Explanation

# According to the given clues, at time T = 1, the character can be in the cells (1, 3), (2, 3), (3, 1), (3, 2), (3, 3) and at time T = 3, the character can be in the cells (1, 1), (1, 2), (1, 3)

# But we can see that these clues aren't sufficient to find the secret cell. Hence print the "Not enough clues".

# Example 3

# Input

# 3 3

# a d j

# a c e

# n c y

# 3

# 2

# 1

# 1 1 2 2

# 3

# 1 1 3 3

# Output

# Not enough clues

# Explanation

# According to the given clues, at time T = 3, the sub grid from (1,1) to (3,3) does not contain the character (i.e., the 3rd character of the secret key). As a result, the clues are insufficient / incorrect to determine the character at this position, so we simply print the same.


# SecretKey - CodeVita-ready solution
# Finds the secret key if uniquely determined; otherwise prints "Not enough clues".

import sys

def read_all_tokens():
    # Robust against blank lines and varying whitespace.
    return sys.stdin.read().split()

def main():
    tokens = read_all_tokens()
    if not tokens:
        print("Not enough clues")
        return

    it = 0
    try:
        rows_count = int(tokens[it]); it += 1
        cols_count = int(tokens[it]); it += 1
    except:
        print("Not enough clues")
        return

    cell_count = rows_count * cols_count
    if rows_count <= 0 or cols_count <= 0:
        print("Not enough clues")
        return

    # Read grid letters (N*M tokens). Use first character of each token.
    if it + cell_count > len(tokens):
        print("Not enough clues")
        return

    grid_letters_by_id = []
    for _ in range(cell_count):
        tok = tokens[it]; it += 1
        grid_letters_by_id.append(tok[0])

    # Read T and I
    if it >= len(tokens):
        print("Not enough clues"); return
    try:
        secret_length_T = int(tokens[it]); it += 1
    except:
        print("Not enough clues"); return

    if it >= len(tokens):
        print("Not enough clues"); return
    try:
        clues_count_I = int(tokens[it]); it += 1
    except:
        print("Not enough clues"); return

    if secret_length_T <= 0 or clues_count_I < 0:
        print("Not enough clues"); return

    # Allowed masks per time step t (0-based: t_idx=0 means time 1)
    # Start with "all cells allowed", then exclude per clues.
    all_cells_mask = (1 << cell_count) - 1
    allowed_masks_per_time = [all_cells_mask for _ in range(secret_length_T)]

    # Apply clues
    for _ in range(clues_count_I):
        if it >= len(tokens): print("Not enough clues"); return
        try:
            t_val = int(tokens[it]); it += 1
        except:
            print("Not enough clues"); return

        if it + 4 > len(tokens): print("Not enough clues"); return
        try:
            x1 = int(tokens[it]); y1 = int(tokens[it+1]); x2 = int(tokens[it+2]); y2 = int(tokens[it+3])
            it += 4
        except:
            print("Not enough clues"); return

        # t_val is 1-based time index; convert to 0-based
        if not (1 <= t_val <= secret_length_T):
            print("Not enough clues"); return
        t_idx = t_val - 1

        # Normalize rectangle bounds and clamp to grid (1-based to 0-based)
        r1 = max(0, min(rows_count-1, min(x1, x2) - 1))
        r2 = max(0, min(rows_count-1, max(x1, x2) - 1))
        c1 = max(0, min(cols_count-1, min(y1, y2) - 1))
        c2 = max(0, min(cols_count-1, max(y1, y2) - 1))

        # Exclude the rectangle from allowed cells at time t_idx
        if r1 <= r2 and c1 <= c2:
            mask = 0
            for rr in range(r1, r2 + 1):
                base = rr * cols_count
                for cc in range(c1, c2 + 1):
                    mask |= (1 << (base + cc))
            allowed_masks_per_time[t_idx] &= ~mask
        # If rectangle is completely outside grid, it has no effect

    # If any time step has no allowed cells, clues are contradictory/insufficient
    for t_idx in range(secret_length_T):
        if allowed_masks_per_time[t_idx] == 0:
            print("Not enough clues")
            return

    # Precompute neighbor masks for each cell id (4-directional).
    neighbor_mask_by_id = [0] * cell_count
    for cell_id in range(cell_count):
        r = cell_id // cols_count
        c = cell_id % cols_count
        mask = 0
        if r > 0:
            mask |= (1 << ((r - 1) * cols_count + c))
        if r + 1 < rows_count:
            mask |= (1 << ((r + 1) * cols_count + c))
        if c > 0:
            mask |= (1 << (r * cols_count + (c - 1)))
        if c + 1 < cols_count:
            mask |= (1 << (r * cols_count + (c + 1)))
        neighbor_mask_by_id[cell_id] = mask

    # If T==1, we just need the set of letters from allowed time-1 cells.
    if secret_length_T == 1:
        letters_set = set()
        mask = allowed_masks_per_time[0]
        while mask:
            lowbit = mask & -mask
            cell_id = lowbit.bit_length() - 1
            mask ^= lowbit
            letters_set.add(grid_letters_by_id[cell_id])
            if len(letters_set) > 1:
                print("Not enough clues")
                return
        if not letters_set:
            print("Not enough clues")
            return
        print(next(iter(letters_set)))
        return

    # Backtracking search: gather at most two distinct words
    first_word_found = None
    found_different_word = False

    sys.setrecursionlimit(10000)

    def dfs(current_cell_id, time_index_1based, visited_mask, current_word_chars):
        nonlocal first_word_found, found_different_word

        if found_different_word:
            return  # short-circuit

        # If we've reached time T, record the word
        if time_index_1based == secret_length_T:
            final_word = ''.join(current_word_chars)
            if first_word_found is None:
                first_word_found = final_word
            elif final_word != first_word_found:
                found_different_word = True
            return

        # Determine candidates for next time (time_index_1based -> next time)
        next_time_idx = time_index_1based  # 0-based index for next time
        candidates_mask = neighbor_mask_by_id[current_cell_id]
        candidates_mask &= allowed_masks_per_time[next_time_idx]
        candidates_mask &= ~visited_mask  # must not revisit

        # Explore each candidate neighbor
        while candidates_mask and not found_different_word:
            lowbit = candidates_mask & -candidates_mask
            next_cell_id = lowbit.bit_length() - 1
            candidates_mask ^= lowbit

            current_word_chars.append(grid_letters_by_id[next_cell_id])
            dfs(
                next_cell_id,
                time_index_1based + 1,
                visited_mask | (1 << next_cell_id),
                current_word_chars
            )
            current_word_chars.pop()

    # Try all allowed starting cells for time 1
    start_mask = allowed_masks_per_time[0]
    if start_mask == 0:
        print("Not enough clues")
        return

    while start_mask and not found_different_word:
        lowbit = start_mask & -start_mask
        start_cell_id = lowbit.bit_length() - 1
        start_mask ^= lowbit

        start_word_chars = [grid_letters_by_id[start_cell_id]]
        dfs(
            start_cell_id,
            1,  # already placed time 1
            (1 << start_cell_id),
            start_word_chars
        )

    # Decide outcome
    if first_word_found is None or found_different_word:
        print("Not enough clues")
    else:
        print(first_word_found)

if __name__ == "__main__":
    main()
