def uint16(x):
    return x&0xFFFF

def find_bylabel(lst, label):
    for item in lst:
        if (item.label == label):
            return item
    return None

def find_bylroot(lst, label):
    for item in lst:
        if (item.left.label == label):
            return item
    return None

def findkbyv(dic, v):
    for ke,va in dic.items():
        if v == va:
            return ke
    return None

_and = lambda a,b: a&b
_or = lambda a,b: a|b
_lshift = lambda a,b: a<<b
_rshift = lambda a,b: a>>b
_not= lambda a,b: ~a
_none = lambda a,b: a

class Expr(object):
    funcs = {'AND':_and, 'OR':_or, 'LSHIFT':_lshift, 'RSHIFT':_rshift, 'NOT':_not , 'NOOP': _none}
    funcs.update({ v:k for k,v in funcs.items() }) #make symmetric
    def __init__(self, label, l=None, r=None, v=0, op=None):
        self.left = l
        self.right = r
        self.value = v
        self.op = op
        self.label = label
        self.evaluated = -1
    def evaluate(self,dynamic=True):
        if dynamic:
            if (self.evaluated == -1):
                if (self.left and self.right):
                    self.evaluated = uint16( self.op( self.left.evaluate(), self.right.evaluate() ) )
                    return self.evaluated
                if (self.left or self.right):
                    self.evaluated = uint16( self.op( (self.left or self.right).evaluate(), self.value ) )
                    return self.evaluated
                return self.value
            else:
                return self.evaluated
        else:
            if (self.left and self.right):
                return uint16( self.op( self.left.evaluate(dynamic=False), self.right.evaluate(dynamic=False) ) )
            if (self.left or self.right):
                return uint16( self.op( (self.left or self.right).evaluate(dynamic=False), self.value ) )
            return self.value
    def __repr__(self):
        if (self.left and self.right):
            return "({} {} {})".format(self.left, Expr.funcs[self.op], self.right)
            #print("(",self.left,Expr.funcs[self.op],self.right,")")
        if (self.left or self.right):
            if (self.value == 0):
                return "({} {})".format(self.left or self.right, Expr.funcs[self.op])
            else:
                return "({} {} {})".format(self.left or self.right, Expr.funcs[self.op], self.value)
            #print("(",self.left or self.right,Expr.funcs[self.op],self.value,")")
        return "{}".format(self.value)
        #print(self.value)
        #return ""

    def dep(self,level=0):
        if (self.evaluated == -1):
            if (self.left and self.right):
                print(" "*level,self.label,"=",self.left.label,Expr.funcs[self.op],self.right.label)
                self.left.dep(level=level+1)
                self.right.dep(level=level+1)
            elif (self.left or self.right):
                print (" "*level,self.label,"=",self.left.label,Expr.funcs[self.op],self.value)
                self.left.dep(level=level+1)
            else:
                print (" "*level,self.label,"=",self.value)
        else:
            print(" "*level,self.label,"=",self.evaluated)
        
        
def day7(fname='input7.txt',part2=False):
    exprs = []
    with open(fname,'r') as f:
        for line in f:
            data = line.strip().split()
            target = data[-1]
            this_expr = Expr(target) #new node with target label
            exprs.append(this_expr)
            if part2:
                if (target=='b'):
                    this_expr.value = 3176
                    continue
            for expr in exprs:
                if expr.left and expr.left.label == target:
                    expr.left = this_expr
                elif expr.right and expr.right.label == target:
                    expr.right = this_expr
            if (data[1]=='AND') or (data[1]=='OR'):
                this_expr.op = Expr.funcs[data[1]]
                left_dep = data[0]
                right_dep = data[2]

                if left_dep.isdigit():
                    this_expr.left = Expr("_anon_",v=int(left_dep))
                else:
                    this_expr.left = Expr(left_dep)
                if right_dep.isdigit():
                    this_expr.right = Expr("_anon_",v=int(right_dep))
                else:
                    this_expr.right = Expr(right_dep)
                
                find = find_bylabel(exprs, left_dep)
                if (find): this_expr.left = find
                find = find_bylabel(exprs, right_dep)
                if (find): this_expr.right = find
            elif (data[1]=='LSHIFT') or (data[1]=='RSHIFT'):
                this_expr.op = Expr.funcs[data[1]]
                left_dep = data[0]
                this_expr.left = Expr(left_dep)
                find = find_bylabel(exprs, left_dep)
                if (find): this_expr.left = find
                this_expr.value = int(data[2])
            elif (data[0]=='NOT'):
                this_expr.op = _not
                left_dep = data[1]
                this_expr.left = Expr(left_dep)
                find = find_bylabel(exprs, left_dep)
                if (find): this_expr.left = find
            else:
                if data[0].isdigit():
                    this_expr.value = int(data[0])
                else:
                    this_expr.op = _none
                    left_dep = data[0]
                    find = find_bylabel(exprs, left_dep)
                    this_expr.left = Expr(left_dep)
                    if (find): this_expr.left = find
    print('Tree created, size:',len(exprs))
    a_expr = find_bylabel(exprs, 'a')
    #print(a_expr.label, '=', a_expr)
    #a_expr.dep()
    print( a_expr.label,'=',uint16( a_expr.evaluate(dynamic=True) ) )

day7()
