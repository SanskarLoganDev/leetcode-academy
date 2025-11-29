import sys
from collections import deque

def solve_bubble_shooter():
    try:
        raw_input = sys.stdin.read().splitlines()
        input_data = [line.strip() for line in raw_input if line.strip()]
    except Exception:
        return

    if not input_data: return
    
    iterator = iter(input_data)
    
    try:
        r_c = next(iterator).split()
        R, C = int(r_c[0]), int(r_c[1])
        M = int(next(iterator))
        
        grid = []
        for _ in range(M):
            grid.append(next(iterator).split())
            

        for _ in range(R - M):
            grid.append(['.'] * C)
            
        colors_list = next(iterator).split()
        point_vals = [int(x) for x in next(iterator).split()]
        points_map = {c: p for c, p in zip(colors_list, point_vals)}
        
        N = int(next(iterator))
        K = int(next(iterator))
        
    except StopIteration: return
    except ValueError: return
    
    def get_cluster(r, c, color):
        cluster = []
        q = deque([(r, c)])
        visited = set([(r, c)])
        cluster.append((r, c))
        
        while q:
            curr_r, curr_c = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if (nr, nc) not in visited and grid[nr][nc] == color:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        cluster.append((nr, nc))
        return cluster

    total_bonus = 0

    def apply_gravity():

        nonlocal total_bonus
        safe = set()
        q = deque()
        
        for c in range(C):
            if grid[0][c] != '.':
                safe.add((0, c))
                q.append((0, c))
        
        while q:
            r, c = q.popleft()
            
            if r + 1 < R and grid[r+1][c] != '.':
                if (r+1, c) not in safe:
                    safe.add((r+1, c))
                    q.append((r+1, c))
            
            curr_color = grid[r][c]
            for dc in [-1, 1]:
                nc = c + dc
                if 0 <= nc < C and grid[r][nc] != '.':
                    if (r, nc) not in safe and grid[r][nc] == curr_color:
                        safe.add((r, nc))
                        q.append((r, nc))
        
        falling_bubbles = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] != '.' and (r, c) not in safe:
                    falling_bubbles.append((r, c))
        
        for r, c in falling_bubbles:
            total_bonus += points_map.get(grid[r][c], 0)
            grid[r][c] = '.'

    
    curr_r, curr_c = R, N
    dr, dc = -1, -1 
    
    bounces = 0
    
    while bounces < K:
        if all(all(c == '.' for c in row) for row in grid):
            break

        next_r = curr_r + dr
        next_c = curr_c + dc

        if next_c < 0:
            dc = -dc
            next_c = curr_c + dc
        elif next_c >= C:
            dc = -dc
            next_c = curr_c + dc
            
        # Top/Bottom Wall Hit
        if next_r < 0:
            dr = -dr
            next_r = curr_r + dr
        elif next_r >= R:
            dr = -dr
            next_r = curr_r + dr
        
        cell_vert = (curr_r + dr, curr_c)       
        cell_horz = (curr_r, curr_c + dc)       
        cell_diag = (curr_r + dr, curr_c + dc)
        
        def is_bubble(pos):
            return 0 <= pos[0] < R and 0 <= pos[1] < C and grid[pos[0]][pos[1]] != '.'
            
        has_v = is_bubble(cell_vert)
        has_h = is_bubble(cell_horz)
        has_d = is_bubble(cell_diag)
        
        hit = False
        
        if has_v and has_h:
            c1 = get_cluster(*cell_vert, grid[cell_vert[0]][cell_vert[1]])
            c2 = get_cluster(*cell_horz, grid[cell_horz[0]][cell_horz[1]])
            for r, c in c1 + c2: grid[r][c] = '.'
            dr = -dr
            dc = -dc
            hit = True
            
        elif has_v:
            cl = get_cluster(*cell_vert, grid[cell_vert[0]][cell_vert[1]])
            for r, c in cl: grid[r][c] = '.'
            dr = -dr
            hit = True
            
        elif has_h:
            cl = get_cluster(*cell_horz, grid[cell_horz[0]][cell_horz[1]])
            for r, c in cl: grid[r][c] = '.'
            dc = -dc
            hit = True
            
        elif has_d:
            cl = get_cluster(*cell_diag, grid[cell_diag[0]][cell_diag[1]])
            for r, c in cl: grid[r][c] = '.'
            dr = -dr
            dc = -dc
            hit = True
            
        if hit:
            bounces += 1
            apply_gravity()
        else:
            curr_r, curr_c = next_r, next_c

    print(total_bonus)

if __name__ == "__main__":
    solve_bubble_shooter()