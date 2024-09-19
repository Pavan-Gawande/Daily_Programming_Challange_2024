import itertools
def Get_Permutations(input_string):
    result = []
    perms = itertools.permutations(input_string)
    unique_perms = set(perms)
    for word in unique_perms:
        result.append(''.join(word))
    return sorted(result)

input_string = input()
print(Get_Permutations(input_string))
