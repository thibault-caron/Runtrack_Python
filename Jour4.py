# Job 1
def Job1():


    return

# Job 2
def Job2():

    
    return


# Job 3
def Job3():


    return


# Job 4
def Job4():


    return


# Job 5
def Job5():


    return


# Job 6 - fonction nombre positif ou negatif
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

    # Appel de la fonction avec le nombre saisi
    # verif_nombre(nombre)

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


    return


# Job 9
def Job9():


    return

# Job 10
def Job10():


    return

Job7()