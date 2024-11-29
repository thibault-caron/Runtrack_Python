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
    print(f"la liste: {L}")
    print(f"La deuxième valeur de la liste est : {L[1]}")


    #   fonction qui remplace L[3] par la somme des cases voisines
    def replace_sum(L):
        print("On effectue l'opération L[3] = L[2] + L[4]...")
        L[3] = L[2] + L[4]
        print(f"Liste après modification: {L}")

    #afficher la dernière valeur du tableau
    print(f"Dernière valeur du tableau : {L[-1]}")

    return replace_sum(L)


# Job 6 - échange les valeurs de la première et de la dernière case d’une liste quelconque non vide.
def Job6():
    def change_place(L):
        if len(L) > 0:
            #inversion 1er et derniere position    
            L[0], L[-1] = L[-1], L[0]
        return L

    #Cree une liste de cinq entiers
    L = [1, 2, 3, 4, 5]
    print(f"La liste dans l'ordre est : {L}") 

    #appel de la fonction
    L = change_place(L)

    resultat = print("Liste après échange :", L ) 

    return resultat


# Job 7 - Compte les multiples de 3 dans la liste
def Job7():
    L =[8,24,48,2,16]

    def multiples_trois(L):
        i = 0
        for num in L:
            if num % 3 == 0:
                i += 1
        return i

    return print(f"Nombre de multiple de trois dans la liste : {multiples_trois(L)}")


# Job 8 - Calcul la somme des valeurs paires de la liste
def Job8():
    L = [8, 24,27,48,2,16,9,7,84,91]

    # Somme du tableau
    def somme_valeurs_paires(L):
        somme = 0
        for num in L:
            if num % 2 == 0:
                somme += num
        return somme
    
    return print(f"La somme de toutes les valeurs paires du tableau est : {somme_valeurs_paires(L)}")


# Job 9 - Récupère valeurs min et max
def Job9():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    max_value = max(L)
    min_value = min(L)
    print(f"La valeur max est: {max_value}")
    print(f"La valeur min est: {min_value}")

    return

# Job 10 - calcule le produit de toutes les valeurs de la liste comprises dans l’intervalle [25, 90]
def Job10():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    product = 1; 
    for x in L: 
        if 25 <= x <= 90: product *= x
    
    print(f"le produit de toutes les valeurs de la liste comprises dans l'intervalle [25, 90] est: {product}")

    return product

# Job 11 - augmenter de 1 la valeur de chaque élément d'une liste
def Job11():
    L = [7, 11, 42, 39, 2]
    print(f"liste initiale: {L}")

    L = [x+1 for x in L]

    print(f"liste finale: {L}")

    return L


# Job 12 - trie une liste dans l’ordre croissant (L = sorted(L))
def Job12():
    L = [7, 11, 42, 39, 2]
    print(f"liste initiale: {L}")

    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    
    print(f"liste finale: {L}")

    return L

# Job 13 - supprime les doublons (L = list(set(L)))
def Job13():
    L = [10, 20,30, 20, 10, 50, 60, 40, 80, 50, 40]
    print(f"liste initiale: {L}")

    L = [x for i, x in enumerate(L) if x not in L[:i]]
    print(f"liste finale: {L}")

    return L

# Job 14 - fonction qui retourne les mots plus longs que le chiffre passé en paramètre
def Job14():

    def my_long_word(n, s):
        return [word for word in s.split() if len(word) > n]

    my_long_word(5, "grandiose")

    return

# Job 15
def Job15():


    return

Job14()