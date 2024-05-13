def isValid(s):
    parens = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }
    stack = []
    for i in s:
        if i in parens:
            stack.append(i)
        elif len(stack) == 0 or parens[stack.pop()] != i:
            return False
    return len(stack) == 0
print(isValid("()"))
print(isValid("[()}"))