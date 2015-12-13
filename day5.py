def day5(st):
    if ("ab" in st) or ("cd" in st) or ("pq" in st) or ("xy" in st):
        return False
    if (st.count("a")+st.count("e")+st.count("i")+st.count("o")+st.count("u"))<3:
        return False
    for i in range(len(st)-1):
        if st[i+1]==st[i]:
            return True
    return False
def day5p2(st):
    def rule1(st):
        for i in range(len(st)-1):
            pair1 = (st[i],st[i+1])
            for j in range(len(st)-1):
                pair2 = (st[j],st[j+1])
                if (pair1 == pair2) and (i != j) and (i+1 != j) and (j+1 != i):
                    return True
        return False
    def rule2(st):
        for i in range(len(st)-2):
            if st[i]==st[i+2]:
                return True
        return False
    return (rule2(st) and rule1(st))
#st = " "
#while (st!=""):
#    st = input()
#    print(day5p2(st))
count = 0
with open("input5.txt") as f:
    for line in f:
        count += int(day5p2( line.strip() ))
print(count)
