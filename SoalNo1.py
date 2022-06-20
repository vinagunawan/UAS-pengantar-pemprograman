dataMahasiswa = [
    ["42130102", "VINA", "TI"],
    ["42130103", "ALICIA", "TI"],
    ["42130103", "ARY", "TI"]
]
 
x = 0
print (f"1. {dataMahasiswa[0][1]}")
print (f"2. {dataMahasiswa[1][1]}")
print (f"3. {dataMahasiswa[2][1]}")

inputUser = int(input("pilihlah nama mahasiswa diatas: "))

if inputUser == 1:
    print (dataMahasiswa[0])
elif inputUser == 2:
    print (dataMahasiswa[1])
elif inputUser == 3:
    print (dataMahasiswa[2])