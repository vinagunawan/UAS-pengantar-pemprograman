data = []
jumlahInputData = 0
while True:
    userInput = input("Masukan angka: ")
    if userInput == 'n':
        break
    jumlahInputData += 1
    data.append(userInput)

total = 0
for nilai in data:
    total += int(nilai)

total = total / jumlahInputData
print(total)
