# Stylus Simulator
# Problem Description

# Raju, an avid digital artist, uses his tablet and stylus to create geometric art on a 2D canvas grid of size N × M. He carefully plans his drawing commands in advance and executes them sequentially, striving for perfection.

# You are tasked with simulating Raju's drawing commands on a digital canvas. Each rectangle drawn is axis-aligned and defined by its top-left coordinates, width, and height.

# Commands must be executed in the order provided. Invalid commands should be skipped but logged to the output. The following rules apply:

# Rectangles must remain fully within the grid.
# Rectangles must not touch or overlap each other, including at edges or corners.
# A rectangle completely enclosed within another is considered overlapping and is invalid.
# com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@60219a32:image1.png
# Constraints

# 1<= M, N <= 20

# 1 <= C <= 20

# 1 <= w, h <= 20

# The grid spans from (0,0) to (N, M).

# For extend or shrink commands, if the rectangle sides are equal to those defined in the command, it is a valid command.

# Input

# The first line contains two integers, M and N, representing the height and width of the canvas grid, respectively.

# The second line contains an integer C, denoting the number of commands to be executed.

# Each of the following C lines describes a command in one of the formats above.

# Output

# Print each invalid command exactly as it appears in the input, in order.

# After processing all commands, print the total number of valid rectangles remaining on the canvas.

# Time Limit (secs)
# 1

# Examples

# Example 1

# Input

# 8 6

# 7

# draw 0 6 3 3

# draw 4 3 2 2

# shrink 0 6 2 2

# remove 4 3 2 2

# extend 0 6 7 7

# shrink 0 6 4 4

# shrink 0 6 1 1

# Output

# extend 0 6 7 7

# shrink 0 6 4 4

# 1

# Explanation

# The canvas is 6 × 8.
# The first rectangle is drawn at (0, 6) with size 3 × 3.
# The second rectangle is drawn at (4, 3) with size 2 × 2.
# The first rectangle shrunk to 2 × 2.
# The second rectangle is removed.
# The extend command is invalid (out of bounds).
# The shrink command is invalid (already smaller).
# The final shrink reduces the rectangle to 1 × 1.
# Only one rectangle remains.
# Example 2

# Input

# 4 4

# 5

# draw 0 2 1 2

# draw 2 4 2 2

# shrink 0 2 1 1

# extend 0 2 1 2

# draw 2 2 1 1

# Output

# draw 2 2 1 1

# 2

# Explanation

# The canvas is 4 × 4.
# The first rectangle is drawn at (0, 2) with size 1 × 2.
# The second rectangle is drawn at (2, 4) with size 2 × 2.
# The first rectangle shrunk to 1 × 1.
# The rectangle is extended back to 1 × 2.
# The third draw command will overlap existing rectangle, hence invalid.
# Two rectangles remain.

import sys

def next_nonempty(lines, idx):
    n = len(lines)
    while idx < n and lines[idx].strip() == "":
        idx += 1
    return idx

def parse_two_ints(line):
    parts = line.strip().split()
    return int(parts[0]), int(parts[1])

def parse_cmd(line):
    # Keep original spacing for echoing invalid lines.
    parts = line.strip().split()
    if not parts:
        return None
    cmd = parts[0].lower()
    if cmd not in ("draw", "remove", "extend", "shrink"):
        return None
    if len(parts) != 5:
        return None
    x = int(parts[1]); y = int(parts[2]); w = int(parts[3]); h = int(parts[4])
    return cmd, x, y, w, h

class Rect:
    __slots__ = ("x","y","w","h","left","right","top","bottom")
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.left   = x
        self.right  = x + w
        self.top    = y
        self.bottom = y - h  # because y is top

def in_bounds(r: Rect, width: int, height: int) -> bool:
    return (0 <= r.x and r.right <= width and
            0 <= r.y and r.bottom >= 0)

def touch_or_overlap(a: Rect, b: Rect) -> bool:
    # Invalid if projections on both axes intersect or touch (>= / <= with equality)
    return not (a.right < b.left or b.right < a.left or
                a.top   < b.bottom or b.top   < a.bottom)

def find_by_top_left(rects, x, y):
    # unique by (x,y)
    for i, r in enumerate(rects):
        if r.x == x and r.y == y:
            return i
    return -1

def find_exact(rects, x, y, w, h):
    for i, r in enumerate(rects):
        if r.x == x and r.y == y and r.w == w and r.h == h:
            return i
    return -1

def has_conflict(rects, new_rect: Rect, ignore_idx: int = -1) -> bool:
    for i, r in enumerate(rects):
        if i == ignore_idx:
            continue
        if touch_or_overlap(r, new_rect):
            return True
    return False

def main():
    lines = sys.stdin.read().splitlines()
    i = next_nonempty(lines, 0)
    if i >= len(lines): 
        print(0)
        return

    # First line: M N (height, width)
    height_val, width_val = parse_two_ints(lines[i]); i += 1

    i = next_nonempty(lines, i)
    if i >= len(lines):
        print(0); return
    commands_count = int(lines[i].strip()); i += 1

    rects = []                 # list[Rect]
    invalid_outputs = []       # original lines of invalid commands, in order

    # Process commands
    cmd_lines_read = 0
    while cmd_lines_read < commands_count and i < len(lines):
        i = next_nonempty(lines, i)
        if i >= len(lines):
            break
        original_line = lines[i].rstrip("\n")
        i += 1
        cmd_lines_read += 1

        parsed = parse_cmd(original_line)
        if parsed is None:
            invalid_outputs.append(original_line)
            continue

        op, x, y, w, h = parsed

        if w <= 0 or h <= 0:
            invalid_outputs.append(original_line)
            continue

        if op == "draw":
            newr = Rect(x, y, w, h)
            if not in_bounds(newr, width_val, height_val):
                invalid_outputs.append(original_line)
                continue
            if has_conflict(rects, newr, -1):
                invalid_outputs.append(original_line)
                continue
            rects.append(newr)

        elif op == "remove":
            idx_found = find_exact(rects, x, y, w, h)
            if idx_found == -1:
                invalid_outputs.append(original_line)
                continue
            rects.pop(idx_found)

        elif op == "extend":
            idx = find_by_top_left(rects, x, y)
            if idx == -1:
                invalid_outputs.append(original_line)
                continue
            curr = rects[idx]
            # must not be smaller than current; equality allowed
            if w < curr.w or h < curr.h:
                invalid_outputs.append(original_line)
                continue
            newr = Rect(x, y, w, h)
            if not in_bounds(newr, width_val, height_val):
                invalid_outputs.append(original_line)
                continue
            if has_conflict(rects, newr, ignore_idx=idx):
                invalid_outputs.append(original_line)
                continue
            # apply
            rects[idx] = newr

        elif op == "shrink":
            idx = find_by_top_left(rects, x, y)
            if idx == -1:
                invalid_outputs.append(original_line)
                continue
            curr = rects[idx]
            # must not be larger than current; equality allowed
            if w > curr.w or h > curr.h:
                invalid_outputs.append(original_line)
                continue
            newr = Rect(x, y, w, h)
            if not in_bounds(newr, width_val, height_val):
                invalid_outputs.append(original_line)
                continue
            if has_conflict(rects, newr, ignore_idx=idx):
                invalid_outputs.append(original_line)
                continue
            rects[idx] = newr

        else:
            invalid_outputs.append(original_line)

    # Output: invalid commands (in order), then number of rectangles
    for s in invalid_outputs:
        print(s)
    print(len(rects))

main()
