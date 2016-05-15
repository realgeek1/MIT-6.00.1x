def f(a,b):
    return a+b
    
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). 
    The function will return a tuple of two dictionaries: 
    a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, 
    calculated as follows:

    intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. 
    To get the values of the intersect dictionary, 
    look at the common keys in d1 and d2 and apply the function f to these keys' values -- 
    the value of the common key in d1 is the first parameter to the function and the value of
    the common key in d2 is the second parameter to the function. Do not implement f inside your
    dict_interdiff code -- assume it is defined outside.
    difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1
    whose key appears only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears
    only in d2 and not in d1.
    '''
    # Your code here
    intersection = {}
    difference = {}
    for a,b in d1.iteritems():
        for c,d in d2.iteritems():
            if a == c:
                intersection[a] = f(b,d)
            else: 
                difference[a] = b
                difference[c] = d
    updatedDifference = difference.copy()
    for a in difference:
        if a in intersection:
            
            del updatedDifference[a]            
    #print intersection
    #print difference1
    answer = (intersection,updatedDifference)
    #print answer
    return answer