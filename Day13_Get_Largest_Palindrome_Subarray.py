def get_Longest_Palindrome(input_string):
    length = len(input_string)
    longest_palindrome = ''

    def is_palindrome(string):
        return string == string[::-1]
    
    for start in range(length):
        for end in range(start+1, length+1):
            sub_String = input_string[start:end]
            if(is_palindrome(sub_String)):
                if(len(sub_String) > len(longest_palindrome)):
                    longest_palindrome = sub_String
    return longest_palindrome

input_string = input()
print(get_Longest_Palindrome(input_string))