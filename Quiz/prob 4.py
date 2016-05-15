def isPalindrome(aString):
    '''
    aString: a string
    returns True if string is a palindrome otherwise returns False
    '''
    # Your code here
    boolean = True
    length = len(aString)
    a = 0
    b = (length - 1)
    if length == 1:
        return boolean
    elif length == 0:
        return boolean
    elif length % 2 == 0:
        while a < length/2:
            if aString[b] == aString[a]:
                a += 1
                b -= 1
            else:
                boolean = False
                break
        return boolean
    else:
        while a != b:
            if aString[a] == aString[b]:
                a += 1
                b -= 1
            else:
                boolean = False
                break
        return boolean
            