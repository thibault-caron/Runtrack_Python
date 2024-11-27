# Job 1 - égalité de valeurs
def Job1():
    print("Comparaison de 2 valeurs")
    valeur1 = input("Entrez la première valeur: ")
    valeur2 = input("Entrez la deuxième valeur: ")

    #Vérifions l'égalité des valeurs
    if valeur1 == valeur2:
        print("Valeur 1 est égale à valeur 2.")
    else:
        print("Les deux valeurs ne sont pas égales.")

    return

# Job 2 - Age
def Job2():
    #Initialisation de la variable
    age = int(input("Entrez votre age: "))

    #Verificat si l'age est au moins 18 ans
    if age >= 18:
        print("Tu peux voter")
    else:
        print("Tu ne peux pas voter")    
    
    return


# Job 3
def Job3():
    print("affichons les nombres de 0 à 100 saans 26, 37 et 88:")
    #genere les nbrs de 0 à 100
    for i in range(101):  
        if i in [26, 37, 88]:
            continue
        print(i)

    return 


# Job 4
def Job4():
    print("pour les nombres de 1 à 100, affiche 'Fizz' pour les multiples de 3 et 'Buzz' pour les multiples de 5")
    for i in range (1, 101):
        ##verifier si multiple de 3 et 5
        if i % 3 == 0 and i % 5 == 0:
            print(i, "- FizzBuzz")
        #verifier si multiple de 3
        elif i % 3 == 0:    
            print(i, "- Fizz")
        #verifier si multiple de 5
        elif i % 5 == 0:
            print(i, "- Buzz")
        #sinon afficher le nombre
        else:
            print(i)

    return


# Job 5
def Job5():
    primary = 3
    lower = int(input("Entrez la valeure minimum de l'echelle de valeurs:"))
    upper = int(input("Entrez la valeure maximum de l'echelle de valeurs:"))

    print("Prime numbers between", lower, "and", upper, "are:")

    for primary in range(lower, upper + 1):
        for i in range (2, primary):
            if (primary % i) == 0:
                break
        else:
           print(primary)

    return


# Job 6
def Job6():


    return


# Job 7
def Job7():
    string="abcdefghijklmnopqrstuvwxyz" 

    i=1

    while i <= len(string):
        print(string[:i])
        i+=2

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


Job4()