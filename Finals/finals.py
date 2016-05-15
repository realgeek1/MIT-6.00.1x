def dict_invert(d):
    ls = []
    result ={}
    for i in d.itervalues():
        for g in d:
             if d[g] == i:
                 ls.append(g)
        result[i] = sorted(ls)
        ls = []
    return result
    
def getSublists(L, n):  
    bl = []
    subl = []
    s=0
    c=n
    end = len(L)
    while c < end+1:
        for i in range(s,c):
            subl.append(L[i])
        s+=1
        c+=1
        bl.append(subl)
        subl=[]
    return bl  

    
def longestRun(L):
    ls = []
    for n in range(len(L)):
        ls.append(getSublists(L,n))
    ls.reverse()
    for list1 in ls:
        if all(x<y for x, y in zip(L, L[1:])) == True:
            return list1

class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
        
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        self.name = name
        if status in ['citizen','legal_resident','illegal_resident']:
            self.status = status
        else:
            raise ValueError
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status
            
    
        
        