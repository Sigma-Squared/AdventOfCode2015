import re
def map_all(mat, f, start, end):
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            mat[i][j] = f(mat[i][j])
def day6(*func_list, size=1000):
    mat = [ [0]*size for _ in range(size) ]
    with open("input6.txt","r") as f:
        for line in f:
            data = line.strip().split()
            if ( data[0] == 'turn' ):
                start = tuple(map(int, data[2].split(',')))
                end = tuple(map(int, data[4].split(',')))
                if ( data[1] == 'on' ):
                    map_all(mat, func_list[0], start, end)
                else:
                    map_all(mat, func_list[1], start, end)
            else:
                start = tuple(map(int, data[1].split(',')))
                end = tuple(map(int, data[3].split(',')))
                map_all(mat, func_list[2], start, end)

    print(sum(map(sum, mat)))


if __name__ == '__main__':
    #part1 day6(lambda v: 1, lambda v: 0, lambda v: int(not v))
    #part 2
    day6(lambda v: v+1, lambda v: max(0, v-1), lambda v: v+2)
