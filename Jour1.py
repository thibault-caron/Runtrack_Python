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
    print(num1 + num2)

    return


# Job 9 - gestion d'un inventaire
def Job9():

    nom = "objet"
    prix_unitaire = 1.5
    quantite_stock = 2500

    # Affichage du produit en console
    print("INVENTAIRE")
    print(f"Nom du produit :  {nom}")
    print(f"Prix Unitaire (€) : {prix_unitaire:.2f} € ")
    print(f"Quantite total du stock : {quantite_stock} {nom}s")

    # ajout de stocks
    quantite_stock += 300
    print(quantite_stock)

    # quantite d'objets que veut l'utilisateur
    while True:
        quantite = input("Quelle quantité de ", nom, "voulez-vous? : ")
        if quantite.isdigit():
            # Conversion de l'entrée en entier si c'est bien un chiffre
            quantite = int(quantite)
            if quantite > quantite_stock:
                print(f"Desolé, il ne reste que: {quantite_stock} {nom}s")
                continue
            else:
                quantite_stock -= quantite  
                print(f"Vous avez acheté {quantite} {nom}s.") 
                print(f"Quantité stock restant: {quantite_stock} {nom}s")

            break
        else:
            print("Entrée invalide. Veuillez entrer un chiffre.")


    #augmentation du prix de 10%
    augmentation = 0.1
    prix_unitaire_augm = prix_unitaire * (1 + augmentation)
    print(f"Prix unitaire après inflation : {prix_unitaire_augm:.2f} €")

    #Affichage du produit en console après augmentation
    print("INVENTAIRE APRES INFLATION DE 10%")
    print(f"Nom du produit :  {nom}")
    print(f"Prix Unitaire (€) : {prix_unitaire_augm:.2f} € ")
    print(f"Quantite total du stock : {quantite_stock} stylos")

    return


# Job 10 - Simulation financiere
def Job10():
    
    # variable pour % investissement et taux rendement
    investissement = 1300
    taux_an = 5

    # affiche gain annuel en fct du taux de rendement
    gain_annuel = investissement * (taux_an / 100)
    print(f"Le gain annuel est : {gain_annuel:.2f} €")

    # augmentation du capital et du % de rendement
    investissement += 5000
    taux_an += 2
    gain_annuel = investissement * (taux_an / 100)
    print(f"Le gain annuel après augmentation est : {gain_annuel:.2f} €")

    # diminution du capital et du rendement
    investissement *= 0.9
    taux_an -= 1
    gain_annuel = investissement* (taux_an / 100)
    print(f"Gain après retrait de 10% et diminution du taux de 1% : {gain_annuel} €")

    return

# Job+
# Écrivez un script qui détermine si une chaîne contient ou non le caractère "e"

def Job_plus():

    # Chaine qui détermine si e est présent
    chaine = input("Entrez une chaine de caractère: ")

    #vérifier si le e est présent
    if "e" in chaine:
        print("La lettre e est dans la chaine de caractères.")
    else:
        print("La lettre e n'est pas présente dans la chaine de caractères.")

    return

Job_plus()
