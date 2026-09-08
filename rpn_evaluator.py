import math

ALLOWED = {'+', '-', '*', '/', '^', '**', '%', '//', 'sqrt', 'abs'}

def is_numeric_string(s: str) -> bool:
    s = s.strip()
    return s.replace('.', '', 1).replace('-', '', 1).isdigit()

def evaluate_rpn(tokens: list[str]) -> float | int:
    stack = []
    
    binary_operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b) if isinstance(a, int) and isinstance(b, int) else a / b,
        '//': lambda a, b: a // b,
        '%': lambda a, b: a % b,
        '^': lambda a, b: a ** b,
        '**': lambda a, b: a ** b,
    }
    
    unary_operators = {
        'sqrt': lambda a: math.sqrt(a),
        'abs': lambda a: abs(a),
    }

    for token in tokens:
        if token in binary_operators:
            right = stack.pop()
            left = stack.pop()
            result = binary_operators[token](left, right)
            stack.append(result)
        elif token in unary_operators:
            val = stack.pop()
            result = unary_operators[token](val)
            stack.append(result)
        else:
            num = float(token) if '.' in token else int(token)
            stack.append(num)

    return stack.pop()

expr = input("Enter RPN Expression (space-separated) >>> ")

tokens = expr.split()
print("Processed Tokens:", tokens)

if any(not (is_numeric_string(item) or item in ALLOWED) for item in tokens):
    print("Unrecognized symbol used in expression.")
    exit(1)

print(f"Result: {evaluate_rpn(tokens)}")