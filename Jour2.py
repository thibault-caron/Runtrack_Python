# Job 1
def Job1():
    i = 0
    for i in range(21):
        print(i)

    return

# Job 2
def Job2():
    i = 0
    for i in range(2, 21, 2):
        print(i)
    
    return


# Job 3
def Job3():


    return


# Job 4 - tables de multiplications
def Job4():

    N = int(input("Veuillez entrer un entier N supérieur à zéro: "))

    if N > 0:
        for i in range(1, N+1):
            print(f"La table de multiplication de {i}:")
            for j in range(1, 11):
                print(f"{i} X {j} = {i * j}")
    else:
        print("Veuillez entrer un nombre supérieur à zéro")

    return


# Job 5 - Boucle "while"
def Job5():

    N = 1
    print("Valeurs de N dans (1, 13) grâce à une boucle 'while': ")
    while N < 14 and N > 0:
        print(N)
        N += 1

    return

def Job5b():

    N = int(input("Entrez un nombre entier supérieur à zéro: "))
    if N > 0:
        i = 1
        while i <= N:
            print(f"Table de multiplication de {i}: ")
            for j in range(1, 11):
                print(f"{i} X {j} = {i * j}")

            i += 1
    else:
        print("Veuillez entrer un nombre supérieur à zéro.")

        return


# Job 6 - premiers résultats de la multiplications par N * 7
def Job6():

    N = int(input(f"Entrez un entier N supérieur à zéro :"))
    i = 1

    while i <= 10:
        print(f"{N} X {i} X 7 = {N * i * 7}")
        i += 1

    return


# Job 7 - Boucle de 12 tours (affiche {tour - 2})
def Job7():

    for tour in range(1, 13):
        resultat = 3 * tour - 2
        print(f"Tour {tour} : {resultat}")

    return


# Job 8 - Boucle de 12 tours avec numéro précédent +2
def Job8():

    resultat = 0

    for tour in range(1, 13):
        resultat += 2
        print(f"Tour {tour} : {resultat}")

    return


# Job 9
def Job9():


    return

# Job 10
def Job10():


    return

Job5()