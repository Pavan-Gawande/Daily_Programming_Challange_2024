def Get_Unique_Char_Substring(input_string):
    n = len(input_string)
    substring = ''
    substring_length = -99999
    for i in range(n):
        for j in range(i+1, n+1):
            temp = input_string[i:j]
            length = len(temp)
            if(len(set(sorted(temp))) == length and length > substring_length):
                substring = temp
                substring_length = length
                if(substring_length == n):
                    return substring_length
    return substring_length

input_string  = input()
print(Get_Unique_Char_Substring(input_string))