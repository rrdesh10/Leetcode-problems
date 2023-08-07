def parentheses(st: str):
    opcl = dict(('{}', '()', '[]'))
    stack = []

    for idx in st:
        if idx in '{([':
            stack.append(idx)

        elif len(stack) == 0 or idx != opcl[stack.pop()]:
            return False

    return len(stack) == 0

print(parentheses("()"))