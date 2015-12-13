from itertools import permutations

def day9(fname='input9.txt'):
    locations = set()
    distances = {}
    with open(fname,'r') as f:
        for line in f:
            data = line.strip().split()
            _from, _to = data[0], data[2]
            locations.add(_from)
            locations.add(_to)
            distances[ _from+_to ] = int(data[4])
            distances[ _to+_from ] = int(data[4])
    mn = 999999
    mx = 0
    print(locations)
    for perm in permutations(locations):
        #print(perm)
        dist = sum(distances[perm[i]+perm[i+1]] for i in range(len(perm)-1))
        if dist>mx:
            mx = dist
        if dist<mn:
            mn = dist
    print(mn, mx)

day9()
