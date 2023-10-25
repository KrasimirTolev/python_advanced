from collections import deque

brackets = deque(input())
open_brackets = deque()


while brackets:
    current_bracket = brackets.popleft()
    if len(open_brackets) == 0:
        if current_bracket in ')}]':
            print('NO')
            break

    if current_bracket in '([{':
        open_brackets.append(current_bracket)
    else:
        if open_brackets.pop() + current_bracket in '(){}[]':
            continue
        else:
            print('NO')
            break

else:
    print('YES')