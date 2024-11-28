# Job 1 - Fonction qui affiche 'Hello World'
def Job1():
    # La fonction
    def My_Print_Hello():
        print("Hello World")

    #Appel de la fonction
    My_Print_Hello()

    return

# Job 2
def Job2():
    def My_Print_name(name):
        print(name)


    My_Print_name("Thibault")
    My_Print_name("Vanessa")
    My_Print_name("Florence")
    
    return 


# Job 3
def Job3():
    def Add(a, b):
        print(a + b)

    Add(10, 5)
    Add(2, 4)
    Add(7, 3)   

    return


# Job 4
def Job4():
    def GetHello():
        print("Hello la Plateforme")

    return GetHello()


# Job 5
def Job5():
    # Demande des valeurs à l'utilisateur
    num1 = int(input("Entrez la valeur 1: "))
    operator = input("Entrez l'opérateur (+, -, *, /, %): ")
    num2 = int(input("Entrez la valeur 2 : "))

    # Fonction calcule
    def calcule(num1, operator, num2):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Erreur: division par zéro"
        elif operator == "%":
            if num2 != 0:
                return num1 % num2
            else:
                return "Erreur: division par zéro"
        else:
            return "Opérateur invalide"

    # Appel de la fonction avec les arguments fournis
    resultat = calcule(num1, operator, num2)
    print("Résultat = ", resultat)

    return resultat


# Job 6 - fonction verifie si nombre positif ou negatif
def Job6():
    # Entrez un nombre
    nombre = int(input("Entrez un nombre: "))

    # Fonction qui vérifie le signe du nombre
    def verif_nombre(nombre):
        if nombre > 0:
            print("Ce nombre est positif.")
        elif nombre < 0:
            print("Ce nombre est négatif.") 
        else: 
            print("Ce nombre est nul.")    

    return verif_nombre(nombre)


# Job 7
def Job7():
    langage = input("Entre le language que tu utilise: ")

#fonction paramètre langage
    def verif_langage(langage):

        if langage == "JavaScript" or langage == "javascript" or langage == "Javascript":
            print("Tu es un developpeur Web.")
        elif langage == "Python" or langage == "python":  
            print("Tu es un developeeur IA.")
        elif langage == "Java" or langage == "java":
            print("Tu es un développeur logiciel")
        elif langage == "ReactJs" or langage == "Reactjs" or langage == "reactjs":
            print("Tu es un développeur mobile.")
        else:
            print("Un jour, je serai le meilleur développeur, je me batterais sans repis!")
            print("Je ferais tout pour être vainqueur, et gagner les défis!")  

    #appel fonction
    return verif_langage(langage)


# Job 8
def Job8():
    # Demande à l'utilisateur d'entrer les valeurs
    saison = input("Entrez une saison: 'été' ou 'hiver': ")
    type_aliment = input("Entrez 'fruits' ou 'légumes': ")

    # Définition de la fonction
    def aliments(type_aliment, saison):
        if (type_aliment == "fruits" or type_aliment == "f") and (saison == "hiver" or saison == "h"):
            print("orange, mandarine, kiwi")
        elif (type_aliment == "fruits" or type_aliment == "f") and (saison == "été" or saison == "e"):
            print("Poire, fraise, cassis")
        elif (type_aliment == "légumes" or type_aliment == "l") and (saison == "hiver" or saison == "h"):
            print("carotte, topinambour, endive")
        elif (type_aliment == "légumes" or type_aliment == "l") and (saison == "été" or saison == "e"):
            print("artichaut, aubergine, navet")  
        else:
            print("Données introuvables.")   

    # Appel de la fonction en passant les paramètres saisis par l'utilisateur
    # aliments(type_aliment, saison)

    return aliments(type_aliment, saison)


# Job 9 - Moyenne de 3 notes
def Job9():

    def moyenne(note1, note2, note3):
        return (note1 + note2 + note3) / 3

    #demande à l'utilisateur de rentrer les notes
    note1 = float(input("Entrez la première note: "))
    note2 = float(input("Entrez la deuxième note: "))
    note3 = float(input("Entrez la troisième note: "))

    #Calculer la moyenne en appelant la fct
    moyenne_etudiant = moyenne(note1, note2, note3)
    moyenne_etudiant = float(format(moyenne_etudiant, '.2f'))

    #Afficher message en fct de la moyenne
    if 15 <= moyenne_etudiant <= 20:
        print(moyenne_etudiant, " - Très bon élève.")
    elif 11 <= moyenne_etudiant <=14:
        print(moyenne_etudiant, " - Bon élève.")   
    elif 8 <= moyenne_etudiant <= 10:
        print(moyenne_etudiant, " - Elève moyen.")
    elif 0 <= moyenne_etudiant <= 7:
        print(moyenne_etudiant, " - Elève devant faire des efforts.")  
    else:
        print("Note invalide.")    

    return

# Job 10 - fonction nombre pair ou impair
def Job10():

    def parity (nombre):
        if isinstance(nombre, int)and nombre >= 0:
            if nombre % 2 == 0:
                print("Ce nombre est pair !!")
            else :
                print("ce nombre est impair.")   
        else:
            print("Saisie invalide, veuillez entrer un nombre entier positif") 

    nombre = int(input("entrez un nombre entier positif: "))

    #Appel de la fonction
    # parity(4)   # Nombre pair
    # parity(7)   # Nombre impair
    # parity(10)  # Nombre pair
    # parity(-3)  # Entrée invalide (négatif)
    # parity(3.5) # Entrée invalide (non entier)

    return parity(nombre)


# Job 11 - transforme un entier en une chaine qui présente l'heure correspondante
def Job11():
    def time_to_text(minutes):
        heures = minutes // 60
        minutes_reste = minutes % 60
        print(f"{heures} heures et {minutes_reste} minutes")


    # Faire entrer à l'utilisateur un nombre entier de minutes
    minutes = int(input("Entrez un nombre de minutes: "))
    
    return time_to_text(minutes)

# Job_plus - fonction qui inverse une string

def Job_plus():
    #reverse une string
    def reverse_chaine(chaine):
        chaine = input("Entrez une suite de charactères: ")
        return chaine [::-1]

    #appel de la fonction
    resultat = print(reverse_chaine("test"))
    # print(resultat)

    return resultat


Job_plus()