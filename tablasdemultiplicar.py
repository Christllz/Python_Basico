def run():
   opcion = (input("""Bienvenido al visualizador de tablas 
   a - tabla del 2
   b - tabla del 3
   c - tabla del 4
   d - tabla del 5
   e - tabla del 6
   f - tabla del 7
   g - tabla del 8
   h - tabla del 9
   elija una opcion: """))
   
   abc = "abcdefgh"
   contador= 0
   numero = 666
   for contador in range(8):
      if abc[contador] == opcion:
         numero = contador + 2
         print("esta es la tabla del " + str(a))
         for tabla in range(1,11):
            print(a*tabla)
      
   if numero == 666:
      print("ingrese una opcion valida")


if __name__ == "__main__":
   run()