def luar():
    x = 10
    def fdalam():
        nonlocal x
        x = 20
        print('Nilai x di dalam fdalam(): %d' %x)

    print('Nilai x di dalam fluar(): %d' %x)
    fdalam()

fluar()
nilai x di dalam fluar(): 10
nilai x di dalam fdalam(): 20