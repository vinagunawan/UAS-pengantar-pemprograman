batas = 5 
spasi = 2*batas-2

for i in range (0, batas):
    for j in range (0, spasi):
        print (' ', end='')
    spasi -= 2
    for j in range (0, i + 1):
        print ('* ', end='')
    print('')