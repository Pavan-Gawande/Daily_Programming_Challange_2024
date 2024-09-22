def get_Substring(input_string, k):
    n = len(input_string)
    substrings = []
    for start in range(n):
        for end in range(start+1, n+1):
            sub_string = s[start:end]
            char_set = set(sorted(sub_string))
            if(len(char_set) == k):
                l.append(sub_string)
    return len(l)
    
input_string = input()
k = int(input())
print(get_Substring(input_string,k))