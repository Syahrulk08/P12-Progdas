g = 10

def f1():
    print('Nilai variabel g di dalam f1(): %d' % g)

def f2():
    global g
    # mencoba untuk mengubah nilai g
    g = 20
    print('Nilai variabel g di dalam f2(): %d' % g)

def f3():
    print('Nilai variabel g di dalam f3(): %d' % g)

def main():

    # memanggil fungsi f1() dan f2()
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()
