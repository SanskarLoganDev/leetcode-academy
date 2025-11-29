import sys

def solve_wall_shooter():
    # 1. Reading Input
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return

    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        K = int(next(iterator)) # Target bounces
        start_x = int(next(iterator))
        start_y = int(next(iterator))
        N = int(next(iterator)) # Paddle Length
        x1 = int(next(iterator))
        y1 = int(next(iterator))
        x2 = int(next(iterator))
        y2 = int(next(iterator))
    except StopIteration:
        return

    # 2. Setup Coordinate System
    # Ensure min/max bounds are correct regardless of input order
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2) # This is the Paddle/Bottom level
    max_y = max(y1, y2) # This is the Top Wall

    # Ball State
    bx, by = float(start_x), float(start_y)
    dx, dy = -1.0, 1.0 # 45 degrees counter-clockwise (Up-Right)

    # Paddle State
    # "Paddle begins in the centre... ball launches from middle of your paddle"
    # This implies Paddle Center initially aligns with Ball Start X.
    px = float(start_x) 
    half_pad = N / 2.0

    bounces = 0
    max_move_dist = 0.0
    
    # Small epsilon for float comparison to detect corner hits
    EPS = 1e-9

    # 3. Simulation Loop
    while bounces < K:
        # Calculate time to collision for all 4 boundaries
        # Time = (Target - Current) / Velocity
        
        t_events = []

        # Top Wall (only if moving Up)
        if dy > 0:
            t = (max_y - by) / dy
            t_events.append((t, 'TOP'))
        
        # Bottom/Paddle (only if moving Down)
        if dy < 0:
            t = (min_y - by) / dy
            t_events.append((t, 'BOTTOM'))

        # Right Wall (only if moving Right)
        if dx > 0:
            t = (max_x - bx) / dx
            t_events.append((t, 'RIGHT'))
            
        # Left Wall (only if moving Left)
        if dx < 0:
            t = (min_x - bx) / dx
            t_events.append((t, 'LEFT'))

        # Sort events by time. Filter out negative/zero times (floating point noise)
        valid_events = [e for e in t_events if e[0] > EPS]
        if not valid_events:
            break
            
        valid_events.sort(key=lambda x: x[0])
        
        # Get the earliest collision time
        time_to_collision = valid_events[0][0]
        
        # Check for "Corner Hit" (Simultaneous collisions)
        # Example: Hitting Top and Right at the same time
        collisions = []
        for t, w in valid_events:
            if abs(t - time_to_collision) < EPS:
                collisions.append(w)
            else:
                break
        
        # Move Ball
        bx += dx * time_to_collision
        by += dy * time_to_collision
        
        # Process Collisions
        hit_paddle = False
        
        for wall in collisions:
            if wall == 'TOP':
                dy = -dy
                bounces += 1
            elif wall == 'BOTTOM':
                hit_paddle = True
                dy = -dy
                # Paddle reflection does NOT count as a score bounce
            elif wall == 'LEFT':
                dx = -dx
                bounces += 1
            elif wall == 'RIGHT':
                dx = -dx
                bounces += 1
        
        # Handle Paddle Movement Logic
        if hit_paddle:
            # Current Paddle Range
            pad_left = px - half_pad
            pad_right = px + half_pad
            
            dist_moved = 0.0
            
            # If ball is to the left of paddle coverage
            if bx < pad_left:
                # Move paddle Left so that Left Edge touches ball
                # Wait! Optimization: To minimize movement, we want the *closest* edge to touch the ball.
                # If ball is at 2, and paddle is [4, 6]. We move paddle to [2, 4]. Center becomes 3. Move = 4-3=1? 
                # No, strictly: Center was 5. New Center 3. Dist 2.
                # Lazy Strat: Align Left Edge to Ball? No, align *closest* edge.
                # Actually, simply shifting the range [L, R] to include X is the logic.
                # Shift = pad_left - bx. New center = px - Shift.
                shift = pad_left - bx
                px -= shift
                dist_moved = shift
                
            # If ball is to the right of paddle coverage
            elif bx > pad_right:
                # Move paddle Right so that Right Edge touches ball
                shift = bx - pad_right
                px += shift
                dist_moved = shift
            
            # If ball is inside [pad_left, pad_right], dist_moved is 0.
            
            if dist_moved > max_move_dist:
                max_move_dist = dist_moved

    # Output as integer
    print(int(max_move_dist))

if __name__ == "__main__":
    solve_wall_shooter()