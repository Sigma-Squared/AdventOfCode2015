def day8(fname='input8.txt'):
    total = 0
    realtotal = 0
    with open(fname,'r') as f:
        for line in f:
            rline = line.rstrip()
            total+=len(rline)
            realtotal += len(eval(rline))#len(rline) - 2 - rline.count(r'\"') - rline.count(r'\\') - rline.count(r'\x')*3
    return total,realtotal,total-realtotal

def day8p2(fname='input8.txt'):
    total = 0
    realtotal = 0
    with open(fname,'r') as f:
        for line in f:
            rline = line.rstrip()
            total+=len(rline)
            realtotal += len(rline)+rline.count(r'"')+rline.count('\\')+ 2
    return total,realtotal,realtotal-total

print( day8p2() )
