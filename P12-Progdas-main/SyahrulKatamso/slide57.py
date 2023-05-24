def f(n):
    import time
    if n == 0:
        print('Go! Semangat Belajar Pemrograman Python nya ')
        return
    print(n, end=' ')
    time.sleep(1)
    f(n-1)

f(3)

def f(n):
    import time
    if n == 0:
        print('Go! selamat anda akan menjadi seorang progammer')
        return
    print(n, end=' ')
    time.sleep(1)
    f(n-1)

f(10)