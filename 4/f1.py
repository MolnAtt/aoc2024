def beolvas(fajlnev):
    return open(fajlnev).read().strip().split('\n')

def jo1(s):
    return s == 'XMAS' or s == 'SAMX'

def horizontal(m,i,j):
    return jo1(m[i][j-3:j + 1])

def vertical(m,i,j):
    return jo1(m[i-3][j] + m[i-2][j] + m[i-1][j] + m[i][j])

def diagonal(m,i,j):
    return jo1(m[i-3][j-3] + m[i-2][j-2] + m[i-1][j-1] + m[i][j])

def antidiagonal(m,i,j):
    return jo1(m[i-3][j] + m[i-2][j-1] + m[i-1][j-2] + m[i][j-3])

def osszegez(m,i_start, j_start, fv):
    return sum(sum(1 if fv(m,i,j) else 0 for j in range(j_start, len(m[0]))) for i in range(i_start,len(m)))

def feladat1(m):
    return osszegez(m, 3, 0, horizontal) + osszegez(m, 0, 3, vertical) + osszegez(m, 3, 3, diagonal) + osszegez(m, 3, 3, antidiagonal)

print(feladat1(beolvas('test.txt')))
print(feladat1(beolvas('input.txt')))
