import sys
from collections import deque

# --- VECTOR MATH HELPERS ---
def vec_add(v1, v2): return (v1[0]+v2[0], v1[1]+v2[1], v1[2]+v2[2])
def vec_sub(v1, v2): return (v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2])
def vec_neg(v): return (-v[0], -v[1], -v[2])
def vec_dot(v1, v2): return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
def vec_cross(a, b):
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])

def solve_rubiverse():
    # 1. Read Input
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return
    
    iterator = iter(input_data)
    
    # Read 4x4 Grid
    grid = []
    try:
        for _ in range(4):
            grid.append(list(next(iterator)))
    except StopIteration:
        return

    # Read the 24-character content string
    try:
        content_str = next(iterator)
        query_corner = next(iterator)
    except StopIteration:
        return

    # 2. Parse Faces and Assign Content
    # Faces are ordered by scanning net left-to-right, top-to-bottom
    faces = {} # Map 'A' -> {r, c, chars: [], normal, up}
    face_order = []
    
    rows = 4
    cols = len(grid[0]) # usually 4
    
    for r in range(rows):
        for c in range(len(grid[r])):
            char = grid[r][c]
            if 'A' <= char <= 'Z':
                face_order.append(char)
                faces[char] = {
                    'r': r, 
                    'c': c, 
                    'chars': [],
                    'normal': None,
                    'up': None
                }

    # Distribute content string (4 chars per face)
    # Row major: 0=TL, 1=TR, 2=BL, 3=BR
    idx = 0
    for face_id in face_order:
        faces[face_id]['chars'] = list(content_str[idx : idx+4])
        idx += 4

    # 3. BFS to Determine 3D Orientation
    # Start with the first face in the list, assign it to FRONT
    # Orientation: Normal=(0,0,1), Up=(0,1,0) (Standard Z-forward, Y-up)
    
    start_face = face_order[0]
    faces[start_face]['normal'] = (0, 0, 1)
    faces[start_face]['up'] = (0, 1, 0)
    
    # Queue for BFS: (face_char)
    queue = deque([start_face])
    visited = {start_face}
    
    while queue:
        curr_char = queue.popleft()
        curr = faces[curr_char]
        
        curr_n = curr['normal']
        curr_u = curr['up']
        # Right vector = Up x Normal
        curr_r_vec = vec_cross(curr_u, curr_n)
        
        r, c = curr['r'], curr['c']
        
        # Directions in Grid: (dr, dc) mapping to logic
        # (-1, 0) = Grid UP. Corresponds to 3D vector: curr_u
        # (1, 0)  = Grid DOWN. Corresponds to 3D vector: -curr_u
        # (0, 1)  = Grid RIGHT. Corresponds to 3D vector: curr_r_vec
        # (0, -1) = Grid LEFT. Corresponds to 3D vector: -curr_r_vec
        
        moves = [
            (-1, 0, curr_u, 'UP'),
            (1, 0, vec_neg(curr_u), 'DOWN'),
            (0, 1, curr_r_vec, 'RIGHT'),
            (0, -1, vec_neg(curr_r_vec), 'LEFT')
        ]
        
        for dr, dc, move_3d_vec, direction in moves:
            nr, nc = r + dr, c + dc
            
            # Bounds check
            if 0 <= nr < rows and 0 <= nc < len(grid[nr]):
                neighbor_char = grid[nr][nc]
                if 'A' <= neighbor_char <= 'Z' and neighbor_char not in visited:
                    # Calculate Neighbor Orientation
                    # 1. Neighbor Normal = The direction we moved towards (move_3d_vec)
                    # 2. Neighbor Up = ?
                    #    - If we moved along Up/Down axis: New Up = -Old Normal (folding over edge)
                    #    - If we moved along Left/Right axis: New Up = Old Up (rolling sideways)
                    
                    new_normal = move_3d_vec
                    new_up = (0,0,0)
                    
                    if direction == 'UP':
                        # Moving up, top edge folds back. New Up is opposite of old Normal
                        new_up = vec_neg(curr_n)
                    elif direction == 'DOWN':
                        # Moving down, bottom edge folds back. New Up is old Normal
                        new_up = curr_n
                    else:
                        # Moving Left/Right, the "Up" direction is preserved relative to the viewer
                        new_up = curr_u
                        
                    faces[neighbor_char]['normal'] = new_normal
                    faces[neighbor_char]['up'] = new_up
                    
                    visited.add(neighbor_char)
                    queue.append(neighbor_char)

    # 4. Solve for the Corner
    result = []
    
    # Get Normals of the 3 query faces
    # The corner in 3D space is the sum of the 3 face normals meeting there
    # (assuming unit cubes centered at origin, corners are like (+1, +1, +1))
    try:
        n1 = faces[query_corner[0]]['normal']
        n2 = faces[query_corner[1]]['normal']
        n3 = faces[query_corner[2]]['normal']
    except KeyError:
        # Invalid query corner
        return

    corner_vec = vec_add(vec_add(n1, n2), n3)
    
    for f_char in query_corner:
        face = faces[f_char]
        n = face['normal']
        u = face['up']
        r_vec = vec_cross(u, n)
        
        # Project corner vector onto local face coordinates
        # Y-axis score (Up/Down)
        y_score = vec_dot(corner_vec, u)
        # X-axis score (Left/Right)
        x_score = vec_dot(corner_vec, r_vec)
        
        # Determine quadrant
        # y > 0 is Top, y < 0 is Bottom
        # x > 0 is Right, x < 0 is Left
        
        idx = -1
        if y_score > 0: # Top
            if x_score < 0: 
                idx = 0 # Top-Left
            else:           
                idx = 1 # Top-Right
        else: # Bottom
            if x_score < 0:
                idx = 2 # Bottom-Left
            else:       
                idx = 3 # Bottom-Right
            
        result.append(face['chars'][idx])

    print("".join(result))

if __name__ == "__main__":
    solve_rubiverse()