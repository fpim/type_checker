from tc import auto_dec

def add(a:int,b:int)->int:
    return a+b

def otherfunc(a:int,b:int)->int:
    return a+b

def otherotherfunc(a:int,b:int)->int:
    return a+b

auto_dec(__name__,locals())

if __name__ == '__main__' :
    print(add(1,2))
    print(otherfunc(1,2))
    print(otherotherfunc('nah','got string'))