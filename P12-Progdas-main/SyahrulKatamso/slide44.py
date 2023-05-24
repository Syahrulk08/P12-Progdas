def f(**kwargs):
    print('Nilai **kwargs\t: %s' % repr(kwargs))
    print('tipe **kwargs\t: %s' % type(kwargs))

f(satu=1, dua=2)