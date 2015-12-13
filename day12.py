import re
import json
def day12(inp):
    return sum(map(int,re.findall(r'-?\d+',inp)))
def day12p2(inp):
    return sum(
                map(
                    int,
                    re.findall(
                                r'-?\d+',
                                str(
                                    json.loads(
                                               inp,
                                               object_hook=lambda obj: {} if 'red' in obj.values() else obj
                                              )
                                    )
                              )
                    )
                )
def day12p2_reddit(inp):
    def _sum(j):
        if type(j) == int:
            return j
        if type(j) == list:
            return sum(_sum(e) for e in j)
        if type(j) != dict:
            return 0
        if 'red' in j.values():
            return 0
        return _sum(list(j.values()))
    return _sum(json.loads(inp))

with open('input12.txt') as f:
    data = f.read()

print(day12(data))
print(day12p2(data))
