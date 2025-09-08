# throwable variable, _ can be used to refer to previous variable
# type python3 in terminal first
# '12 34 56'.split()
# map(int, _)
# list(_)

print(1,2,3)
print(1, end='')
print(2)
print(1,2,3,sep='-')

print()

x=23
print('there are %d frogs' % x)
print('there are %04d frogs' % x)
print('there are %4d frogs' % x)
print('there are %-4d frogs' % x)

print()

x=2.3
print('there are %f frogs' % x)
print('there are %.2f frogs' % x)
print('there are %.3f frogs' % x)
print('there are %5.1f frogs' % x)

print()

x='two'
print('there are %s frogs' % x)
print('there are %4s frogs' % x)
print('there are %-4s frogs' % x)
print('there are %.2s frogs' % x)

print()

print(7/3)
print(7//3)
print(7%3)
print(7**3)
print(7**0.5)

print()

print(12, 0x12, 0o12) # ngubah ke desimal dari hex dan octal
print('%d %x %o' % (12, 0x12, 0o12)) # ngubah ke hex dan octal dari desimal

print()

print(bin(12)) # ngubah ke binary dari desimal
print(int('1100',2)) # ngubah ke desimal dari binary

print()

print(3.0 / 2.0)
print(3 / 2)
print(3.0 // 2.0) # hasil ada .
print(3 // 2) # hasil angka bulat

print()

x = 'Python'
print(len(x))
print(x[0])
print(x[5])
print(x[-1])
print(x[1:3])
print(x[:3])
print(x[3:])
print(x[:])
print(x[1:5:2]) # start, stop, step
print(x[::-1]) # reverse
print(x[3:-1]) # start, stop

print()

print('a'+'b'+'c')
print(20*'-')
print('-'*20)
print('abc'*2)

print()

# list
L = [1,2,3]
print(L[0])
L[1] = 'halo'
print(L)
L.append(4)
print(L)
L + [5,6] # tidak mengubah L, hanya membuat list baru
L * 3 # tidak mengubah L, hanya membuat list baru
print(L + [5,6])
print(L * 3)

print()

#tuple
T = (1,2,3)
print(T[0])
# T[1] = 'halo' # error, tidak bisa diubah
# T.append(4) # error, tidak bisa diubah
# mirip string yang ga bisa diubah
print(T + (4,5)) # membuat tuple baru
print(T * 3) # membuat tuple baru

print()

#dictionary
D = {'satu':1, 'dua':2, 'tiga':3}
print(D['satu'])
D['dua'] = 'two'
print(D)
D['empat'] = 4
print(D)
# D[1] = 'satu' # bisa, key bisa apa aja
print(D.keys())
print(D.values())
print(D.items())
print('satu' in D)
print(1 in D)

print()

# set
A = {1,2,3}
B = {3,4,5}
C = {1,2,2,3,3,3} # duplicate diabaikan
print(A)
print(C)
print(A & B) # intersection                             (A dan B)
print(A | B) # union                                    (A atau B)
print(A - B) # difference / set subtraction             (A tanpa B)
print(A ^ B) # symmetric difference / exclusive union   (XOR)

print()

print(1 + \
      1) # \ buat lanjutin ke baris berikutnya

print()

# LOOPS

# for loop
L = [1,2,3]
total = 0
for x in L:
    total += x # this is called a suite, must be indented
print(total) # print(sum(L)) built-in function
# for loop has one suite

# while loop
name = 'ABC'
guess = input('masukkan nama: ')
while (guess != name): # while loop has one suite
    print('salah')
    guess = input('masukkan nama: ') # pencet ctrl+c to stop
print('benar')

print()

# if else statement
L = [1,2,3,4,5,-1,-2,-3]
negatif, positif, nol = 0,0,0
for x in L:
    if x < 0:
        negatif += 1
    elif x > 0:
        positif += 1
    else:
        nol += 1
print('>0: %d, <0: %d, ==0: %d' % (negatif, positif, nol))

print()

# match
bulan = int(input('masukkan bulan: '))
match bulan: # butuh python 3.10
    case 1:
        print('januari')
    case 2:
        print('februari')
    case 3:
        print('maret')
    case 4:
        print('april')
    case 5:
        print('mei')
    case 6:
        print('juni')
    case 7:
        print('juli')
    case 8:
        print('agustus')
    case 9:
        print('september')
    case 10:
        print('oktober')
    case 11:
        print('november')
    case 12:
        print('desember')
    case _: # mirip default atau else
        print('bulan tidak valid')
