# Roll The Dice
# Problem Description
# Laila is presented with a challenge involving a dice and a distinctive structure composed of cubes. Her task is to navigate from one cube to another while minimizing the total cost of movement.

# The structure is built by sequentially placing cubes adjacent to existing ones - to the left, right, top, or down. The placement steps are provided as input, specifying the existing cube, the new cube, and the direction of placement. Also, before processing the placement steps, order them in ascending order of first cube number followed by next cube number.

# Each cube is identified by a unique integer. Once the structure is formed, Laila uses a standard six-faced dice to move between adjacent cubes. The initial values on the top, left, and front faces of the dice are given. To move to a neighbouring cube, she rolls the dice in one of the four cardinal directions (up, down, left, or right). Each roll changes the orientation of the dice, and the number that appears on the new top face determines the cost of that move. Note that the opposite faces of the cube always add up to 7.

# Laila may move to an adjacent cube only if one exists in that direction. The goal is to determine the minimum total cost required to reach the destination cube from the source cube.

# Constraints
# 1 <= number of cubes in the structure <= 50

# Cubes may overlap during placement; in such cases, the one which already present should be removed from structure to place the new one.

# Initial top face value will not contribute to the cost.

# Input
# The first line consists of an integer N denoting the number of cube placements.
# The next N lines describe how each cube is placed relative to another, specifying the existing cube, the new cube, and the direction of placement.
# The second-to-last line contains two space-separated integers representing the source and destination cubes.
# The final line contains three space-separated integers representing the values on the top, left, and front faces of the dice.

# Output
# Print a single integer denoting the minimum cost of reaching destination.

# Time Limit (secs)
# 1

# Examples
# Example 1

# Input

# 8

# 6 7 right

# 1 3 left

# 7 8 top

# 1 4 down

# 4 5 right

# 5 6 down

# 1 2 top

# 8 9 left

# 3 8

# 4 1 2

# Output

# 11

# Explanation

# The arrangement of cubes is shown below.

# com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@11ce2e22:image1.png

# Given source is 3 and destination is 8.

# There are many ways possible to travel from source to destination. One of the path resulting in lowest cost is given below.

# The initial cube has the top, left, and front faces numbered 4, 1, and 2, respectively.

# Roll right:
# The cube's new faces are top = 1, left = 3, front = 2.
# Cost so far: 1
# Roll down:
# Now the faces are top = 5, left = 3, front = 1.
# Cost so far: 1 + 5 = 6
# Roll right:
# The cube updates to top = 3, left = 2, front = 1.
# Cost so far: 6 + 3 = 9
# Roll right again:
# Faces become top = 2, left = 4, front = 1.
# Final cost: 9 + 2 = 11
# Note that the path described above is one of the possible paths that results in the minimum cost.

# Example 2

# Input

# 3

# 1 2 right

# 3 4 left

# 2 3 down

# 1 3

# 6 2 3

# Output

# 6

# Explanation

# The arrangement of cubes is shown below.

# com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@11ce2e22:image2.png

# Given source is 1 and destination is 3.

# There are many ways possible to travel from source to destination. One of the path resulting in lowest cost is given below.

# The initial cube has the top, left, and front faces numbered 6, 2, and 3, respectively.

# Roll down:
# The cube's new faces are top = 4, left = 2, front = 6.
# Cost so far: 4
# Roll right:
# Now the faces are top = 2, left = 3, front = 6.
# Final cost: 4 + 2 = 6


import sys
import heapq

# ---------------------------- Dice helpers ---------------------------- #

def make_orientation(top, left, front):
    """Return the full 6-tuple (top, bottom, left, right, front, back).
       Opposites always sum to 7."""
    bottom = 7 - top
    right  = 7 - left
    back   = 7 - front
    return (top, bottom, left, right, front, back)

def roll_right(ori):
    # (t, b, l, r, f, ba) -> (l, r, b, t, f, ba)
    t, b, l, r, f, ba = ori
    return (l, r, b, t, f, ba)

def roll_left(ori):
    # (t, b, l, r, f, ba) -> (r, l, t, b, f, ba)
    t, b, l, r, f, ba = ori
    return (r, l, t, b, f, ba)

def roll_up(ori):
    # (t, b, l, r, f, ba) -> (f, ba, l, r, b, t)
    t, b, l, r, f, ba = ori
    return (f, ba, l, r, b, t)

def roll_down(ori):
    # (t, b, l, r, f, ba) -> (ba, f, l, r, t, b)
    t, b, l, r, f, ba = ori
    return (ba, f, l, r, t, b)

def build_all_orientations_and_transitions(initial_top, initial_left, initial_front):
    """Enumerate all 24 orientations reachable from the given initial orientation.
       Return:
         - orientations: list of 6-tuples,
         - index_of_orientation: dict {6-tuple -> idx}
         - trans[idx]['R'/'L'/'U'/'D'] -> next_idx
    """
    start = make_orientation(initial_top, initial_left, initial_front)
    # BFS to enumerate orientations
    orientations = []
    index_of_orientation = {}

    def add(ori):
        if ori not in index_of_orientation:
            index_of_orientation[ori] = len(orientations)
            orientations.append(ori)
            return True
        return False

    from collections import deque
    q = deque()
    add(start); q.append(start)

    while q:
        o = q.popleft()
        for fn in (roll_right, roll_left, roll_up, roll_down):
            no = fn(o)
            if add(no):
                q.append(no)

    # Build transitions
    trans = []
    for o in orientations:
        d = {
            'R': index_of_orientation[roll_right(o)],
            'L': index_of_orientation[roll_left(o)],
            'U': index_of_orientation[roll_up(o)],
            'D': index_of_orientation[roll_down(o)],
        }
        trans.append(d)
    return orientations, index_of_orientation, trans

# ---------------------------- Build structure ---------------------------- #

def simulate_structure(placements_sorted):
    """
    Build the cube structure on a 2-D grid.
    - placements_sorted: list of tuples (a, b, dir)
    Returns:
      position_of_cube: {cubeId: (x, y)}
      cube_at_cell: {(x, y): cubeId}
    """
    position_of_cube = {}
    cube_at_cell = {}

    def place_cube_at(cube_id, xy):
        """Place/move cube_id to xy. If another cube is at xy, remove it. If cube_id
           was elsewhere, vacate the old cell."""
        # if target occupied by someone else: remove that cube from structure
        other = cube_at_cell.get(xy)
        if other is not None and other != cube_id:
            del position_of_cube[other]
            # replace occupant with the new cube

        # if this cube currently elsewhere, vacate old cell
        old = position_of_cube.get(cube_id)
        if old is not None and old in cube_at_cell and cube_at_cell.get(old) == cube_id:
            del cube_at_cell[old]

        position_of_cube[cube_id] = xy
        cube_at_cell[xy] = cube_id

    for a, b, d in placements_sorted:
        # Ensure 'a' has a position; anchor if first time we see it
        if a not in position_of_cube:
            place_cube_at(a, (0, 0))

        ax, ay = position_of_cube[a]
        if d == 'right':
            bx, by = ax + 1, ay
        elif d == 'left':
            bx, by = ax - 1, ay
        elif d == 'top':
            bx, by = ax, ay + 1
        elif d == 'down':
            bx, by = ax, ay - 1
        else:
            # unknown direction; ignore (not expected by problem)
            continue

        place_cube_at(b, (bx, by))

    return position_of_cube, cube_at_cell

def build_adjacency_from_positions(position_of_cube):
    """Return adjacency: {cubeId: [(neighborId, moveDirChar)]}, moveDirChar in 'LRUD'."""
    # Reverse map for O(1) neighbor lookup
    cell_to_cube = {pos: cid for cid, pos in position_of_cube.items()}
    adj = {cid: [] for cid in position_of_cube.keys()}
    for cid, (x, y) in position_of_cube.items():
        for dx, dy, mchar in ((1, 0, 'R'), (-1, 0, 'L'), (0, 1, 'U'), (0, -1, 'D')):
            nb = cell_to_cube.get((x + dx, y + dy))
            if nb is not None:
                adj[cid].append((nb, mchar))
    return adj

# ---------------------------- Shortest path ---------------------------- #

def min_cost_with_dice(adj, source_cube, dest_cube, initial_top, initial_left, initial_front):
    """Dijkstra over (cube, orientationIndex)."""
    if source_cube not in adj or dest_cube not in adj:
        return -1

    orientations, idx_of, trans = build_all_orientations_and_transitions(initial_top, initial_left, initial_front)

    # dist[(cubeId, oriIdx)] = cost
    dist = {}
    pq = []

    start_ori_idx = idx_of[make_orientation(initial_top, initial_left, initial_front)]
    start_state = (source_cube, start_ori_idx)
    dist[start_state] = 0
    heapq.heappush(pq, (0, source_cube, start_ori_idx))

    while pq:
        cost, cube, ori_idx = heapq.heappop(pq)
        if cost != dist.get((cube, ori_idx), None):
            continue
        if cube == dest_cube:
            return cost  # first time we pop dest is optimal (Dijkstra)

        for nb, move_char in adj[cube]:
            next_ori_idx = trans[ori_idx][move_char]
            next_top = orientations[next_ori_idx][0]  # new top after the roll
            new_cost = cost + next_top
            state = (nb, next_ori_idx)
            if new_cost < dist.get(state, 10**18):
                dist[state] = new_cost
                heapq.heappush(pq, (new_cost, nb, next_ori_idx))

    return -1

# ---------------------------- Parsing & Main ---------------------------- #

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        print(-1)
        return
    k = 0
    N = int(data[k]); k += 1

    placements = []
    for _ in range(N):
        a = int(data[k]); b = int(data[k+1]); d = data[k+2].lower(); k += 3
        placements.append((a, b, d))

    # sort by existing cube then new cube
    placements.sort(key=lambda x: (x[0], x[1]))

    source_cube = int(data[k]); dest_cube = int(data[k+1]); k += 2
    initial_top = int(data[k]); initial_left = int(data[k+1]); initial_front = int(data[k+2]); k += 3

    position_of_cube, _ = simulate_structure(placements)
    adjacency = build_adjacency_from_positions(position_of_cube)

    answer = min_cost_with_dice(adjacency, source_cube, dest_cube, initial_top, initial_left, initial_front)
    print(answer)

# Call main directly (per your preference)
main()
