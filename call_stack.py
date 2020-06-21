def c():
    print('c')

def a():
    print('a')
    b()

def b():
    print('b')
    c()

a()
