
def peso_planetas(n_planeta, gravedad):
    peso = input("Cuanto pesas en el planeta tierra?: ")
    peso = float(peso)
    g_tierra = 9.807
    peso_f = peso * (
        d/g_tierra)
    peso_f = round(peso_f, 2)
    peso_f = str(peso_f)
    print("Tu peso en " + n_planeta  + " es: " + peso_f + " kg ")


menu = """Bienvenido a la calculadora de pesos planetarios

1 - Mercurio
2 - Venus
3 - Marte
4 - Jupiter
5 - Saturno
6 - Urano 
7 - Neptuno
8 - Pluton
9 - Haumea
10 - Makemake
11 - Eris
12 - Sol

Elige un planeta: """

planeta = int(input(menu))   

if planeta == 1:
    peso_planetas("Mercurio", 3.7)
elif planeta == 2:
    peso_planetas("Venus", 8.87)
elif planeta == 3:
    peso_planetas("Marte", 3.721)
elif planeta == 4:
    peso_planetas("Jupiter", 24.79)
elif planeta == 5:
    peso_planetas("Saturno", 10.44)
elif planeta == 6:
    peso_planetas("Urano", 8.87)
elif planeta == 7:
    peso_planetas("Neptuno", 11.15)
elif planeta == 8:
    peso_planetas("Pluton", 0.62)
elif planeta == 9:
    peso_planetas("Haumea", 0.401)
elif planeta == 10:
    peso_planetas("Makemake", 0.5)
elif planeta == 11:
    peso_planetas("Eris", 0.82)
elif planeta == 12:
    peso_planetas("Sol", 274)
else:
    print("Ese planeta no existe, deja las drogas")