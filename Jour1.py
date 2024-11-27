# Job 3
# to execute file in cmd: 'python [fileName.py]

def Job3 ():
    10 + 3
    10 - 3
    10 * 3
    10 / 3
    10 // 3
    10 % 3
    return


# Job 4
def Job4():
    print("abcdefghijklmnopqrstuvwxyz")
    return


# job 5
def Job5():
    print(list(map(chr,range(97,123)[::-1])))
    # [::-1] inverse la string
    return


#job 6
def Job6():
    ma_string="je suis une string"
    print(ma_string)
    # shift+enter to run just the selected code
    return


# Job 7 & 8
def Job7_8():
    num1 = 40
    num2 = 2
    print(num1+num2)
    return


# Job 9
def Job9():
    nom="nom"
    prix_unitaire = 1.0
    quantite_stock = 1

    quantite_stock = quantite_stock+5
    print(quantite_stock)

    print(f'le nom du produit est: {nom}')
    print(f'le prix unitaire est: {prix_unitaire}')
    print(f'la quantité en stock est: {quantite_stock} produit(s)')

    # Demander à l'utilisateur combien de produits il souhaite acheter
    quantite_achetee = 0
    while True:
        quantite_achetee = int(input("Combien de produits souhaitez-vous acheter ? "))

        # Vérifier si la quantité demandée est disponible en stock
        if quantite_achetee <= quantite_stock:

            # Mettre à jour le stock
            quantite_stock -= quantite_achetee
            print(f"Achat effectué. Il reste {quantite_stock} produits en stock.")
        else:
            print(f"Désolé, il n'y a pas assez de produits en stock pour cette commande. Il reste {quantite_stock} produits disponibles.")

        break

    inflation = 0.1

    prix_unitaire += inflation

    print(f'le nom du produit est: {nom}')
    print(f'le prix unitaire est: {prix_unitaire}')
    print(f'la quantité en stock est: {quantite_stock} produit(s)')

    return


# Job 10
def Job10():
    investissement_initial = 1000.0
    rendement_annuel_relatif = 0.05

    rendement_annuel_absolu = investissement_initial * rendement_annuel_relatif

    print(f"gain annuel = {rendement_annuel_absolu}")

    return

# Plus loin
# Écrivez un script qui détermine si une chaîne contient ou non le caractère "e"
