import sys
from collections import deque, defaultdict

def solve_cubemid():
    
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # Parsing
        S = int(next(iterator))

        matrix = []
        for _ in range(S):
            layer = []
            for _ in range(S):
                layer.append(next(iterator))
            matrix.append(layer)
            
        # Parse Start and Goal
        start_l, start_r, start_c = int(next(iterator)), int(next(iterator)), int(next(iterator))
        end_l, end_r, end_c = int(next(iterator)), int(next(iterator)), int(next(iterator))
        
        start_node = (start_l, start_r, start_c)
        end_node = (end_l, end_r, end_c)
        
    except StopIteration:
        return

    if matrix[start_l][start_r][start_c] == 'E' or matrix[end_l][end_r][end_c] == 'E':
        print(-1)
        return

    # Build the Graph (Adjacency List)
    adj = defaultdict(set)

    for l in range(S):
        for r in range(S):
            for c in range(S):
                ctype = matrix[l][r][c]
                
                if ctype == 'E':
                    continue
                
                current = (l, r, c)
                potential_connections = []

                if ctype == 'D':
                    potential_connections.append((l, r, c - 1)) 
                    potential_connections.append((l, r, c + 1)) 
                    potential_connections.append((l - 1, r, c))
                    potential_connections.append((l + 1, r, c)) 
                
                # Ramp to Upper-Right
                elif ctype == 'R':
                    potential_connections.append((l, r - 1, c + 1))
                    potential_connections.append((l, r + 1, c - 1)) 

                # Ramp to Upper-Left
                elif ctype == 'L':
                    potential_connections.append((l, r - 1, c - 1))
                    potential_connections.append((l, r + 1, c + 1))
                    
                # Ramp to Next Layer Down
                elif ctype == 'F':
                    potential_connections.append((l + 1, r + 1, c)) 
                    potential_connections.append((l - 1, r - 1, c)) 
                    
                # Ramp to Next Layer Up
                elif ctype == 'B':
                    potential_connections.append((l + 1, r - 1, c)) 
                    potential_connections.append((l - 1, r + 1, c)) 

                # Process connections
                for nl, nr, nc in potential_connections:
                    if 0 <= nl < S and 0 <= nr < S and 0 <= nc < S:
                        if matrix[nl][nr][nc] != 'E':
                            neighbor = (nl, nr, nc)
                            adj[current].add(neighbor)
                            adj[neighbor].add(current)

    # BFS for Shortest Path
    queue = deque([(start_node, 0)])
    visited = {start_node}
    
    while queue:
        curr, dist = queue.popleft()
        
        if curr == end_node:
            print(dist)
            return
        
        for neighbor in adj[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                
    print(-1)

if __name__ == '__main__':
    solve_cubemid()