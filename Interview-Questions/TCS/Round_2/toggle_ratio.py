import sys

def get_cost(from_pat, to_pat, X, Y):
    """
    Calculates toggle cost. Returns -1 if not exactly 1 toggle.
    """
    s1 = "".join(from_pat)
    s2 = "".join(to_pat)
    if len(s1) != len(s2): return -1
    
    diffs = 0
    cost = 0
    
    for c1, c2 in zip(s1, s2):
        # A segment is ON if it is not a space
        # We use strip() to handle potentially different whitespace chars if any
        is_on_1 = c1.strip() != ''
        is_on_2 = c2.strip() != ''
        
        if is_on_1 == is_on_2:
            continue
        
        diffs += 1
        if diffs > 1: return -1
        
        if is_on_1 and not is_on_2:
            cost += X # ON to OFF
        else:
            cost += Y # OFF to ON
            
    return cost if diffs == 1 else -1

def evaluate_expression(tokens, priority):
    """
    Evaluates expression with Custom Priority and Brackets.
    """
    # Map priority: Higher index = Higher precedence
    prec_map = {c: i for i, c in enumerate(priority)}
    
    output_queue = []
    op_stack = []
    
    for token in tokens:
        if isinstance(token, float):
            output_queue.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            # Pop until '('
            while op_stack and op_stack[-1] != '(':
                output_queue.append(op_stack.pop())
            if op_stack and op_stack[-1] == '(':
                op_stack.pop() # Discard '('
            else:
                return -float('inf') # Mismatched parens
        else: # Operator
            # While stack top has >= precedence
            while (op_stack and op_stack[-1] != '(' and 
                   op_stack[-1] in prec_map and
                   prec_map[op_stack[-1]] >= prec_map[token]):
                output_queue.append(op_stack.pop())
            op_stack.append(token)
    
    while op_stack:
        if op_stack[-1] == '(': return -float('inf') # Mismatched
        output_queue.append(op_stack.pop())
        
    # RPN Evaluation
    stack = []
    for token in output_queue:
        if isinstance(token, float):
            stack.append(token)
        else:
            if len(stack) < 2: return -float('inf')
            val2 = stack.pop()
            val1 = stack.pop()
            
            if token == '+': stack.append(val1 + val2)
            elif token == '-': stack.append(val1 - val2)
            elif token == '*': stack.append(val1 * val2)
            elif token == '/': 
                if val2 == 0: return -float('inf') # Div by Zero check
                stack.append(val1 / val2)
                
    return stack[0] if stack and len(stack) == 1 else -float('inf')

def parse_and_calc(char_list, priority):
    tokens = []
    curr_num = ""
    
    for c in char_list:
        if c.isdigit():
            curr_num += c
        else:
            if curr_num:
                tokens.append(float(curr_num))
                curr_num = ""
            tokens.append(c)
    if curr_num:
        tokens.append(float(curr_num))
        
    if not tokens: return -float('inf')
    
    # Basic Syntax Validation
    # Valid start: Number or '('
    # Valid end: Number or ')'
    if isinstance(tokens[0], str) and tokens[0] != '(': return -float('inf')
    if isinstance(tokens[-1], str) and tokens[-1] != ')': return -float('inf')

    # Run Evaluator
    try:
        return evaluate_expression(tokens, priority)
    except:
        return -float('inf')

def solve():

    LIB = {
        '0': (" _ ", "| |", "|_|"), 
        '1': ("   ", "  |", "  |"), 
        '2': ("   ", "| |", "| |"), 
        '3': ("   ", "|_|", "| |"), 
        '5': ("   ", "| |", "|_|"), 
        '6': (" _ ", "  |", " _|"), 
        '7': (" _ ", "  |", "  |"), 
        '8': (" _ ", " _|", "  |"), 
        '9': (" _ ", "|_|", "  |"), 
        '+': ("   ", " _|", "  |"), 
        '-': (" _ ", "|_|", "| |"), 
        '*': ("   ", "|_|", "|_|"), 
        '/': (" _ ", " _|", " _|"), 
        '(': ("|  ", "|  ", "|  "), 
        ')': ("  |", "  |", "  |"), 
    }
    
    try:
        input_raw = sys.stdin.read().splitlines()
        input_data = [x for x in input_raw if x]
    except: return

    if not input_data: return

    try:
        N = int(input_data[0].strip())
        line1 = input_data[1]
        line2 = input_data[2]
        line3 = input_data[3]
        priority = input_data[4].strip()
        costs = list(map(int, input_data[5].split()))
        X, Y, P, Q = costs[0], costs[1], costs[2], costs[3]
    except: return

    curr_chars = []
    curr_pats = []
    
    # Parsing Input
    for i in range(N):
        s = i * 3
        # Handle line length safety
        p1 = line1[s:s+3] if len(line1) > s else "   "
        p2 = line2[s:s+3] if len(line2) > s else "   "
        p3 = line3[s:s+3] if len(line3) > s else "   "
        pat = (p1, p2, p3)
        curr_pats.append(pat)
        
        found = '?'
        for k, v in LIB.items():
            if v == pat:
                found = k
                break
        curr_chars.append(found)

    max_ratio = -1.0
    
    for i in range(N):
        orig_char = curr_chars[i]
        orig_pat = curr_pats[i]
        
        for target_char, target_pat in LIB.items():
            if target_char == orig_char: continue
            
            # Calculate LED Toggle Cost
            t_cost = get_cost(orig_pat, target_pat, X, Y)
            if t_cost == -1: continue 
            
            # Calculate Conversion Cost (P/Q)
            total_cost = t_cost
            
            # Treat Brackets '(' ')' as Operators (non-digits)
            is_num_orig = orig_char.isdigit() if orig_char != '?' else False
            is_num_targ = target_char.isdigit()
            
            if orig_char != '?':
                if is_num_orig and not is_num_targ:
                    total_cost += P # Number -> Operator/Bracket
                elif not is_num_orig and is_num_targ:
                    total_cost += Q # Operator/Bracket -> Number
            
            # Form New Equation
            new_chars = curr_chars[:]
            new_chars[i] = target_char
            
            try:
                val = parse_and_calc(new_chars, priority)
                if val != -float('inf'):
                    ratio = val / total_cost
                    if ratio > max_ratio:
                        max_ratio = ratio
            except:
                continue

    if max_ratio < 0:
        print("0.00")
    else:
        print(f"{max_ratio:.2f}")

if __name__ == "__main__":
    solve()