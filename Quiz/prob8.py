def f(s):
    return 'a' in s
    
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    for a in L:
        if f(a) == False:
            L.remove(a)
    return len(L)
#run_satisfiesF(L, satisfiesF)


#Right Solution (Can't figure out why I only
#got 17.5/20 in the solution I wrote(above))
#
#
#def satisfiesF(L):
#
#    newList = [k for k in L if f(k) == True]
#    L[:] = newList     
#    return len(L)
#run_satisfiesF(L, satisfiesF)