x = 789
y = 3.1415
print('%5d' % x)    # siapin 5 spasi, tulis angka rata kanan
print('%9.5f' % y)  # siapin 10 spasi termasuk utk koma, tulis angka rata kanan, belakang koma ada 5

s = input('input ints x y: ')
L = s.split()
x, y = map(int, L)  # [int(L[0]), int(L[1]), ...]
print(f'{x} + {y} = {x+y}')

# LAB 00
# there's n animals (not including host) and each animals eats m worth of food
budget = input()
x, y = map(int, budget.split())
print((x+1)*y)
