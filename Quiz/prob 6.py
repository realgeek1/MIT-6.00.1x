#def flatten(aList):
#    ''' 
#    aList: a list 
#    Returns a copy of aList, which is a flattened version of aList 
#    '''    
#    while True:
#        boolean = True
#        for obj in aList:
#            if type(obj) == list:
#                boolean = False
#                for a in obj:
#                    aList.append(a)
#                aList.remove(obj)
#        if boolean == True:
#            break
#    return aList

def flatten(aList):
    ltype = type(aList)
    aList = list(aList)
    i = 0
    while i < len(aList):
        while isinstance(aList[i], list):
            if not aList[i]:
                aList.pop(i)
                i -= 1
                break
            else:
                aList[i:i + 1] = aList[i]
        i += 1
    return ltype(aList)





