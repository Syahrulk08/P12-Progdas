def kali(a, b):
    return a * b

def echo(h, j):
    for i in range(j):
        print(h)

def main():
    # memanggil fungsi kali
    # mengalikan nilai 2 dan 3
    print("\nPemanggilan pertama fungsi kali():")
    print("2 x 3 = %d " % kali(2, 3))

    # mengalikan nilai 10 dan 20
    print("\nPemanggilan kedua fungsi kali():")
    print("10 x 10 = %d " % kali(10, 20))

    # memanggil fungsi echo
    # mencetak teks Python sebanyak 5 kali
    print("\n Pemanggilan pertama fungsi Echo():")
    echo("Python", 5)

    # mencetak teks Python sebanyak 2 kali
    print("\n Pemanggilan kedua fungsi Echo():")
    echo("Pemrograman Python", 2)

if __name__ == "__main__":
    main()