from f1 import beolvas, osszegez

def balra_fent(m, i, j):
    return m[i-2][j-2]

def balra_lent(m, i, j):
    return m[i][j-2]

def jobbra_fent(m, i, j):
    return m[i-2][j]

def jobbra_lent(m, i, j):
    return m[i][j]

def kozepen(m, i, j):
    return m[i-1][j-1] 

def MAS_balrol(m,i,j):
    return (balra_fent(m,i,j) == balra_lent(m,i,j) == 'M') and kozepen(m,i,j) == 'A' and (jobbra_fent(m,i,j) == jobbra_lent(m,i,j) == 'S')

def MAS_lentrol(m,i,j):
    return (balra_lent(m,i,j) == jobbra_lent(m,i,j) == 'M') and kozepen(m,i,j) == 'A' and (balra_fent(m,i,j) == jobbra_fent(m,i,j) == 'S')

def MAS_jobbrol(m,i,j):
    return (jobbra_lent(m,i,j) == jobbra_fent(m,i,j) == 'M') and kozepen(m,i,j) == 'A' and (balra_fent(m,i,j) == balra_lent(m,i,j) == 'S')

def MAS_fentrol(m,i,j):
    return (balra_fent(m,i,j) == jobbra_fent(m,i,j) == 'M') and kozepen(m,i,j) == 'A' and (balra_lent(m,i,j) == jobbra_lent(m,i,j) == 'S')

def feladat2(m):
    return osszegez(m, 2, 2, MAS_balrol) + osszegez(m, 2, 2, MAS_lentrol) + osszegez(m, 2, 2, MAS_jobbrol) + osszegez(m, 2, 2, MAS_fentrol)

print(feladat2(beolvas('test.txt')))
print(feladat2(beolvas('input.txt')))