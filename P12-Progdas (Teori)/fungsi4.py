def kali():
    return 10*20

def echo():
    for i in range(3):
        print("Python")

def main():
    # memanggil fungsi kali
    print("Memanggil fungsi kali():")
    print("10 x 20 = %d " % kali())

    # memanggil fungsi echo
    print("\n Memanggil fungsi Echo():")
    echo()

if __name__ == "__main__":
    main()