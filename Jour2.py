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
            print(f"La table de multiplication de {i} :")
            for j in range(1, 11):
                print(f"{i} X {j} = {i * j}")
    else:
        print("Veuillez entrer un nombre supérieur à zéro")

    return


# Job 5 - Boucle "while"
def Job5():

    N = int(input("Entrez un entier N supérieur à zéro : "))
    if N > 0:
        i = 0
        while i <= N:
            print(f"Table de multiplication de {i} :")
            for j in range(1, 11):
                print(f"{i} X {j} = {i * j}")

            i += 1
    else:
        print("Veuillez entrer un nombre supérieur à zéro.")

        return


# Job 6
def Job6():


    return


# Job 7
def Job7():


    return


# Job 8
def Job8():


    return


# Job 9
def Job9():


    return

# Job 10
def Job10():


    return

