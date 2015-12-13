import re
def increment(s):
    #if all(char=='z' for char in s):
    #    raise Exception("String too large.")
    if not s:
        return 'b'
    if s[-1] == 'z':
        return increment(s[:-1])+'a'
    else:
        return s[:-1]+chr(ord(s[-1])+1)

def isValid(s):
    if 'i' in s or 'o' in s or 'l' in s:
        return False
    return hasSequence(s) and hasPairs(s)

def hasSequence(s):
    for i in range(len(s)-2):
        if ord(s[i+1])-1 == ord(s[i]) and ord(s[i+2])-2 == ord(s[i]):
            return True
    return False
def hasPairs(s):
    reg = re.compile(r'(\w)\1')
    return len(re.findall(reg,s))>=2

def day11(inp='hepxcrrq'):
    inp=increment(inp)
    while not isValid(inp):
        inp = increment(inp)
    return inp

p1 = day11()
print(p1)
print(day11(p1))
    
