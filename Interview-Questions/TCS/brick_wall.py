# The Brick wall
# Problem Description
# A plumber needs to install pipelines on a brick wall. To do this, some bricks must be broken to fit the pipes.

# There are two types of bricks in the wall:

# Red Bricks (R): Hard to break.
# Green Bricks (G): Easy to break.
# The plumber will only break Green Bricks to make the job easier. The wall is represented as a square grid, with each brick type and its length specified (e.g., "3R" means a Red Brick of length equal to three unit Bricks). The wall also includes a Source (S) where the pipe starts and a Destination (D) where it ends.

# Pipes can be laid either vertically or horizontally, moving from the current brick to any adjacent Green Brick (up, down, left, or right). The goal is to find the minimum number of Green Bricks that must be broken to connect the source to the destination. Red Bricks cannot be used.

# Assume the layout of the brick wall is shown below.

# com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@6ac4944a:image1.png

# The input notation to represent the above brick wall is shown below:

# 3R1D
# 1R1R1R1G
# 2G1G1G
# 2S2R

# Constraints
# 3<=N<=25

# Input
# The first line contains N, the size of the wall (N x N).
# The next N lines describe the wall layout using the notation above.

# Output
# Print a single integer: the least number of Green Bricks that need to be broken.

# Time Limit (secs)
# 1

# Examples
# Example 1

# 4

# 3R1D

# 1R1R1R1G

# 2G1G1G

# 2S2R

# Output

# 4

# Explanation

# The input and image already shown in description.

# From the image we can see that 4 bricks need to be destroyed to lay pipes between source and destination.

# Example 2

# Input

# 5

# 3G1R1G

# 1G1R1G2R

# 1S1R1G1R1D

# 2R1G1R1G

# 5G

# Output

# 7

# Explanation

# The image below represents the above input.

# com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@6ac4944a:image2.png

# From this you can see that 7 bricks must be broken to lay pipelines between source and destination.



from collections import deque, defaultdict

def parse_rows_raw(stream):
    """Return N and the raw encoded rows (not expanded)."""
    lines = [ln.strip() for ln in stream if ln.strip()]
    if not lines:
        return None, None
    N = int(lines[0])
    rows_raw = lines[1:1+N]
    if len(rows_raw) != N:
        return None, None
    return N, rows_raw

def build_nodes_from_tokens(N, rows_raw):
    """
    Build brick nodes from token boundaries (each token is a distinct brick).
    Returns:
      cell2node: N x N with node ids
      node_type: list of 'R','G','S','D' per node
      starts: list of S node ids
      dests: list of D node ids
    """
    cell2node = [[-1]*N for _ in range(N)]
    node_type = []
    starts, dests = [], []
    node_id = 0

    for r in range(N):
        s = rows_raw[r].replace(" ", "")
        c = 0   # current column in the grid
        i = 0   # index into the encoded string
        L = len(s)
        while i < L:
            if not s[i].isdigit():
                raise ValueError(f"Row {r}: token must start with a number")
            j = i
            while j < L and s[j].isdigit():
                j += 1
            count = int(s[i:j])
            if j >= L:
                raise ValueError(f"Row {r}: missing brick type after count")
            t = s[j]
            if t not in ("R", "G", "S", "D"):
                raise ValueError(f"Row {r}: invalid brick type {t}")

            # Fill exactly 'count' cells with this node_id
            if c + count > N:
                raise ValueError(f"Row {r}: expanded length exceeds N")
            for cc in range(c, c + count):
                cell2node[r][cc] = node_id
            node_type.append(t)
            if t == 'S':
                starts.append(node_id)
            elif t == 'D':
                dests.append(node_id)

            node_id += 1
            c += count
            i = j + 1

        if c != N:
            raise ValueError(f"Row {r}: expanded length {c} != N ({N})")

    return cell2node, node_type, starts, dests

def build_adjacency(N, cell2node):
    """Undirected adjacency: nodes touching orthogonally anywhere."""
    adj = defaultdict(set)
    for r in range(N):
        for c in range(N):
            u = cell2node[r][c]
            if r+1 < N:
                v = cell2node[r+1][c]
                if u != v:
                    adj[u].add(v); adj[v].add(u)
            if c+1 < N:
                v = cell2node[r][c+1]
                if u != v:
                    adj[u].add(v); adj[v].add(u)
    return {k: list(vs) for k, vs in adj.items()}

def solve_stream(stream) -> int:
    N, rows_raw = parse_rows_raw(stream)
    if N is None:
        return -1

    cell2node, node_type, starts, dests = build_nodes_from_tokens(N, rows_raw)
    if not starts or not dests:
        return -1

    adj = build_adjacency(N, cell2node)

    INF = 10**9
    dist = [INF] * len(node_type)
    dq = deque()

    for s in starts:
        dist[s] = 0
        dq.appendleft(s)

    def enter_cost(v):
        t = node_type[v]
        if t == 'R': return None   # blocked
        if t == 'G': return 1      # break this green brick once
        return 0                   # S or D

    # 0-1 BFS on brick graph
    while dq:
        u = dq.popleft()
        for v in adj.get(u, []):
            w = enter_cost(v)
            if w is None:
                continue
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                (dq.appendleft if w == 0 else dq.append)(v)

    ans = min(dist[d] for d in dests)
    return ans if ans < INF else -1
    
if __name__ == "__main__":
    import sys
    result = solve_stream(sys.stdin)
    print(result)