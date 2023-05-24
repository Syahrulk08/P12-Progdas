def f(a, *args):
    print('Nilai a\t: %s' % repr(a))
    print('Tipe a\t %s' % type(a))
    print('Nilai *args\'t: %s' % repr(args))
    print('Tipe *args\t: %s' % type(args))

    f('test', 1, 2, 3)

# def f(*args,a):
#     print('Nilai a\t: %s' % repr(a))
#     print('Tipe a\t %s' % type(a))
#     print('Nilai *args\t: %s' % repr(a))
#     print('Tipe *args\t: %s' % repr(a))

#     # f(1, 2, 3, 'test')  # Salah


#     f(1, 2, 3, a= 'test')  # Benar