def Get_Comms(input_List):
    length =  len(input_List)
    if(length == 0 ):
        return ""
    elif(length == 1):
        return input_List[0]
    else:
        comms = input_List[0]
        for i in range(1, length):
            element =  input_List[i]
            for j in range(min(len(comms),len(element))):
                if(element[j] != comms[j]):
                    comms = comms[:j]
                    break
        return comms

strs = list(map(str, input().split()))
print(Get_Comms(strs))