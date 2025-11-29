import sys
from collections import deque

# --- BLOSSOM ALGORITHM FOR MAXIMUM MATCHING ---
# Necessary for general graphs (non-bipartite)
class MaxMatching:
    def __init__(self, n, adj):
        self.n = n
        self.adj = adj
        self.match = [-1] * n
        self.p = []
        self.base = []
        self.used = []
        self.blossom = []
    
    def lca(self, a, b):
        used = [False] * self.n
        # Trace path from a to root
        while True:
            a = self.base[a]
            used[a] = True
            if self.match[a] == -1: break
            a = self.p[self.match[a]]
        # Trace from b to find intersection
        while True:
            b = self.base[b]
            if used[b]: return b
            b = self.p[self.match[b]]

    def mark_path(self, v, b, children):
        while self.base[v] != b:
            self.blossom[self.base[v]] = self.blossom[self.base[self.match[v]]] = True
            self.p[v] = children
            children = self.match[v]
            v = self.p[self.match[v]]

    def find_path(self, root):
        self.used = [False] * self.n
        self.p = [-1] * self.n
        self.base = list(range(self.n))
        self.used[root] = True
        q = deque([root])

        while q:
            u = q.popleft()
            for v in self.adj[u]:
                if self.base[v] == self.base[u] or self.match[v] == u:
                    continue
                if v == root or (self.match[v] != -1 and self.p[self.match[v]] != -1):
                    curbase = self.lca(u, v)
                    self.blossom = [False] * self.n
                    self.mark_path(u, curbase, v)
                    self.mark_path(v, curbase, u)
                    for i in range(self.n):
                        if self.blossom[self.base[i]]:
                            self.base[i] = curbase
                            if not self.used[i]:
                                self.used[i] = True
                                q.append(i)
                elif self.p[v] == -1:
                    self.p[v] = u
                    if self.match[v] == -1:
                        return v
                    self.used[self.match[v]] = True
                    q.append(self.match[v])
        return -1

    def solve(self):
        # Greedy initialization
        for i in range(self.n):
            if self.match[i] == -1:
                for v in self.adj[i]:
                    if self.match[v] == -1:
                        self.match[v] = i
                        self.match[i] = v
                        break
        # Augment paths
        count = 0
        for i in range(self.n):
            if self.match[i] == -1:
                target = self.find_path(i)
                if target != -1:
                    while target != -1:
                        parent = self.p[target]
                        prev_match = self.match[parent]
                        self.match[target] = parent
                        self.match[parent] = target
                        target = prev_match
        
        # Calculate size
        matches = 0
        for i in range(self.n):
            if self.match[i] != -1:
                matches += 1
        return matches // 2

# --- MAIN LOGIC ---

def solve_cardboard():
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        box_n = int(next(iterator))
        box_m = int(next(iterator))
        num_lines = int(next(iterator))
        
        partitions = []
        for _ in range(num_lines):
            x1 = int(next(iterator))
            y1 = int(next(iterator))
            x2 = int(next(iterator))
            y2 = int(next(iterator))
            partitions.append((x1, y1, x2, y2))
    except StopIteration:
        return

    # 1. Map Walls
    blocked_paths = set() # ((x,y), (nx,ny))

    for x1, y1, x2, y2 in partitions:
        if x1 == x2: # Vertical
            curr_x = x1
            min_y, max_y = min(y1, y2), max(y1, y2)
            for y in range(min_y, max_y):
                c_left = (curr_x - 1, y)
                c_right = (curr_x, y)
                blocked_paths.add((c_left, c_right))
                blocked_paths.add((c_right, c_left))
        else: # Horizontal
            curr_y = y1
            min_x, max_x = min(x1, x2), max(x1, x2)
            for x in range(min_x, max_x):
                c_down = (x, curr_y - 1)
                c_up = (x, curr_y)
                blocked_paths.add((c_down, c_up))
                blocked_paths.add((c_up, c_down))

    # 2. Flood Fill to find Regions
    cell_to_region = {}
    region_count = 0
    visited = set()

    for x in range(box_n):
        for y in range(box_m):
            if (x, y) in visited:
                continue
            
            current_id = region_count
            region_count += 1
            
            q = deque([(x, y)])
            visited.add((x, y))
            cell_to_region[(x, y)] = current_id
            
            count = 0
            min_rx, max_rx = x, x
            min_ry, max_ry = y, y
            
            while q:
                cx, cy = q.popleft()
                count += 1
                min_rx = min(min_rx, cx)
                max_rx = max(max_rx, cx)
                min_ry = min(min_ry, cy)
                max_ry = max(max_ry, cy)
                
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < box_n and 0 <= ny < box_m:
                        # Only move if NO WALL
                        if ((cx, cy), (nx, ny)) not in blocked_paths:
                            if (nx, ny) not in visited:
                                visited.add((nx, ny))
                                cell_to_region[(nx, ny)] = current_id
                                q.append((nx, ny))
            
            # 3. Validation Check A: Rectangle Geometry
            # Area of cells found must equal Area of bounding box
            width = max_rx - min_rx + 1
            height = max_ry - min_ry + 1
            if count != width * height:
                print("Invalid")
                return

    # 4. Validation Check B: Internal Walls (Dangling Partitions)
    # If two cells are neighbors AND in the same region, there CANNOT be a wall between them.
    for (u, v) in blocked_paths:
        # blocked_paths contains walls between adjacent cells u and v
        # Check if u and v are inside the valid grid logic
        ux, uy = u
        vx, vy = v
        
        # Filter out boundary walls that are strictly outside the box range (though input shouldn't have them)
        if 0 <= ux < box_n and 0 <= uy < box_m and 0 <= vx < box_n and 0 <= vy < box_m:
            # If they belong to the same region...
            if cell_to_region.get(u) is not None and cell_to_region.get(v) is not None:
                if cell_to_region[u] == cell_to_region[v]:
                    # A wall exists inside a single region -> "Incomplete" partition
                    print("Invalid")
                    return

    # 5. Build Region Graph
    adj = [set() for _ in range(region_count)]
    
    for x in range(box_n):
        for y in range(box_m):
            u = cell_to_region[(x, y)]
            # Check Right
            if x + 1 < box_n:
                v = cell_to_region[(x + 1, y)]
                if u != v:
                    adj[u].add(v)
                    adj[v].add(u)
            # Check Top
            if y + 1 < box_m:
                v = cell_to_region[(x, y + 1)]
                if u != v:
                    adj[u].add(v)
                    adj[v].add(u)
    
    adj_list = [list(s) for s in adj]

    # 6. Max Matching
    matcher = MaxMatching(region_count, adj_list)
    matching_size = matcher.solve()

    # Result = Total Regions - Pairs that share a hole
    print(region_count - matching_size)

if __name__ == "__main__":
    solve_cardboard()