from re import findall

def beolvas(fajlnev):
    return open(fajlnev).read()

def feladat1(s):
    return sum([int(p[0])*int(p[1]) for p in findall(r'mul\((\d{1,3}),(\d{1,3})\)', s)])

def main():
    print(feladat1(beolvas('input.txt')))
    