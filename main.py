
"""supression de l'import car non-utilisation de sqrt"""
#### Fonction secondaire


def isprime(p):
    """
    Vérifie si un nombre entier est un nombre premier.
     >>> est_premier(5)
    True
    >>> est_premier(10)
    False
    """
    if p <= 1 :
        return False
    for i in range(2, int( p**0.5 ) + 1):
        if p % i == 0 :
            return False
            break
    else :
        return True

    pass

#### Fonction principale


def main():
    """
    test de la fonction isprime()
    """
    isprime(1)
    isprime(11)
    isprime(19)
    isprime(21)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
