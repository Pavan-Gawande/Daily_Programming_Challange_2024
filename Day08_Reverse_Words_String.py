def reverse_String(input_String):
    word_List = list(map(str, input_String.split()))
    result = []
    for word in word_List:
        if(not word.isspace()):
            temp = word.lstrip()
            res.append(temp.rstrip())
    return ' '.join(res[::-1])

input_String= input()
print(reverse_String(input_String))