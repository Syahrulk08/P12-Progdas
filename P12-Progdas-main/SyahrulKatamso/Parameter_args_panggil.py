def f(*args):
    print('Nilai *args\t: %s' % repr(args))
    print('Tipe *args\t: %s' % type(args))

f(1)

f(1, 2)

f(1, 2, 3)