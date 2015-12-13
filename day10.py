def day10(instr,count=40):
    print(instr)
    for _ in range(count):
        instr = "".join( str(len(group))+group[0] for group in split_groups(instr) )
    print(len(instr))

def split_groups(s):
    cut = 0
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            yield s[cut:i]
            cut = i
    yield s[cut:]

day10('3113322113',50)
