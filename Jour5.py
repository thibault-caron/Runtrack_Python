# Job 1 - liste de fruits
def Job1():

    def get_fruits():
        fruits = ["pomme", "cerise", "orange"]
        return fruits

    #apppel de la fonction et affichage du résultat
    resultat = get_fruits()

    return print(resultat)

# Job 2 - afficher 2ème élément d'une liste
def Job2():

    def get_fruit():
        fruits = ["pomme", "cerise", "orange"]
        return print(f"Le deuxième fruit est: {fruits[1]}")
    
    return get_fruit() # print(f"Affichez le deuxième fruit est: {fruits[1]}")


# Job 3 - ajout en fin de liste
def Job3():
    def ajout_fruits():
        fruits = ["pomme", "cerise", "orange"]
        fruits.append("melon")
        print(fruits)

    return ajout_fruits() 


# Job 4 - ajout en 2ème position
def Job4():
    def ajout_mangue():
        fruits = ["pomme", "cerise", "orange", "melon"]
        fruits.insert(2,"mangue")
        print(fruits)

    return ajout_mangue()


# Job 5
def Job5():
    # Initialisation liste
    L = [5, 9, 8, 15, 38]
    print(f"La deuxième valeur de la liste est : {L[1]}")


    #   fonction qui remplace L[3] par la somme des cases voisines
    def replace_sum(L):
        L[3] = L[2] + L[4]
        print(f"Liste après modification: {L}")

    #afficher la dernière valeur du tableau
    print(f"Dernière valeur du tableau : {L[-1]}")

    return replace_sum(L)


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

# Job 11
def Job11():


    return


# Job 12
def Job12():


    return

# Job 13
def Job13():


    return

# Job 14
def Job14():


    return

# Job 15
def Job15():


    return

Job5()