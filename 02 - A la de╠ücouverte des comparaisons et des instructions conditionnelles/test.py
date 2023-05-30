n=None
try:
    n = int(input("Entrez un nombre :  "))
except ValueError:
    print("\x1b[31m\x1b[46mJe t'avais dit d'entrer un nombre >:(\x1b[37m\x1b[0m")

if n != None :
    if (n % 2) == 0:
        print( str(n)+" est pair")
    else :
        print( str(n)+" est impair")