def Get_Evaluated(s):
    l = []
    for i in s:
        if(i.isdigit()):
            l.append(i)
        else:
            if(i == '^'):
                exp = f'{str(l[-2])}**{str(l[-1])}'
            else:
                exp = str(l[-2])+i+str(l[-1])
            l = l[:-2]
            l.append(eval(exp))
        print(l)
    return l[0]

s = input()
print(Get_Evaluated(s))

