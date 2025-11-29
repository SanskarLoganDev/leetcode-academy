import sys
from collections import deque

def solve():
    # 1. Read Input
    try:
        # Reading all input from standard input
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        iterator = iter(input_data)
        try:
            N = int(next(iterator))
        except StopIteration:
            return
            
        grid = []
        for _ in range(N):
            grid.append(next(iterator))
            
    except Exception as e:
        return

    # Grid organization:
    # grid[0] is the Innermost Ring (Length 4)
    # grid[N-1] is the Outermost Ring
    
    # 2. Setup BFS
    queue = deque()
    visited = set()
    
    outer_ring_idx = N - 1
    outer_ring_len = len(grid[outer_ring_idx])
    
    # Initialize with all valid entry points in the outermost ring
    # Distance is 1 because entering the first room counts as 1 room crossed
    found_entry = False
    for i in range(outer_ring_len):
        if grid[outer_ring_idx][i] == '0':
            queue.append((outer_ring_idx, i, 1))
            visited.add((outer_ring_idx, i))
            found_entry = True
            
    if not found_entry:
        print(0) # Cannot even enter the temple
        return

    # 3. BFS Loop
    while queue:
        r, i, dist = queue.popleft()
        
        # Target Check: If we are in the innermost ring (0), we have reached the center
        if r == 0:
            print(dist)
            return

        current_len = len(grid[r])
        
        # Possible Moves
        neighbors = []
        
        # A. Lateral Moves (Left/Right) - Circular
        neighbors.append((r, (i - 1 + current_len) % current_len)) # Left
        neighbors.append((r, (i + 1) % current_len))               # Right
        
        # B. Inward Move (to r-1)
        # Logic: Room i connects to i // 2 in the inner ring
        if r > 0:
            neighbors.append((r - 1, i // 2))
            
        # C. Outward Move (to r+1)
        # Logic: Room i connects to 2*i and 2*i+1 in the outer ring
        if r < N - 1:
            neighbors.append((r + 1, 2 * i))
            neighbors.append((r + 1, 2 * i + 1))
            
        # Process Neighbors
        for nr, ni in neighbors:
            # Bounds check is implicit by logic, but we must check blockages
            if (nr, ni) not in visited:
                if grid[nr][ni] == '0': # Only move if open
                    visited.add((nr, ni))
                    queue.append((nr, ni, dist + 1))

    # If queue empties and we never reached ring 0
    print(0)

if __name__ == "__main__":
    solve()