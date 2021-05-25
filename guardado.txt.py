def run():
    LIMITE = 1034537273737

    num = 0
    potencia_2 = 2**num
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(num) + " es igual a: " + str(potencia_2) )
        num = num + 1
        potencia_2 = 2**num 

if __name__ == "__main__" :
    run()