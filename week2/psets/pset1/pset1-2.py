s = input('Put a string to have bobs counted')
counter = 0
for x in range(0,len(s)-2):
    var1 = s.count('bob',x,x+3) 
    if (var1 == 1):
        counter += 1
print 'Number of times bob occurs is: ' + str(counter) 