def Is_Balanced_Bracket(input_string):
    bracket_dict = {')' : '(', '}' : '{', ']' : '['}
    closing = ']})'
    stack = []
    for i in input_string:
        if( i in closing):
            if(len(stack)>0 and stack[-1] == bracket_dict[i]):
                stack.pop(-1)
                continue
            return False
        else:
            stack.append(i)
    if(len(stack) == 0):
        return True
    return False

input_string = input()
print(Is_Balanced_Bracket(input_string))