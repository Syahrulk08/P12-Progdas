def varLenArg(*daftarNamaMhs):
    j = 0
    for i in daftarNamaMhs:
        j = j+1
        print("Nama ke -",j,"= ", i)
    return
    
varLenArg("Mirna", 'Ekky', 'Wahdatul', "Hanifah")