def Get_Evaluated(s):
    l = []
    for i in s:
        if(i.isdigit()):
            l.append(i)
        else:
            if(i == '^'):
                exp = str(int(l[-2])^int(l[-1]))
            elif(i == '/'):
                exp = str(int(int(l[-2])/int(l[-1])))
            else:
                exp = str(l[-2])+i+str(l[-1])
            l = l[:-2]
            l.append(eval(exp))
    return l[0]

s = ''.join(input().split())
print(Get_Evaluated(s))

