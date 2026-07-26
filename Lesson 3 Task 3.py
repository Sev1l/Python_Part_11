##Recursion
# Task 3 (Balance all the brackets)


def balanced_brackets(my_string: str):
    pairs = {')': '(', ']': '['}
    opening = set(pairs.values())
    closing = set(pairs.keys())

    stack = []
    for ch in my_string:
        if ch in opening:
            stack.append(ch)
        elif ch in closing:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0
ok = balanced_brackets("([([])])")
print(ok)

ok = balanced_brackets("(python version [3.7]) please use this one!")
print(ok)

ok = balanced_brackets("(()]")
print(ok)

ok = balanced_brackets("([bad egg)]")
print(ok)

