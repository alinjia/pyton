A = input('name')
B = input('surname')
C = int(input('year_of_birth'))
print( A, B, C, sep="_")

A, B =B, A
print( A, B, int(C)+60, sep="_")