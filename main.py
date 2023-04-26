from ast import match_case
from bib.module import *

num_exercicio = 1

while num_exercicio >= 1 and num_exercicio <= 7:
    num_exercicio = int(input('Qual exercicío você deseja visualizar? (1...7 - Somente inteiros) '))
    match num_exercicio:
        case 1:
            exercicio_1()
        case 2:
            exercicio_2()
        case 3: 
            exercicio_3()
        case 4:
            exercicio_4()
        case 5:
            exercicio_5()
        case 6:
            exercicio_6()
        case 7:
            exercicio_7()
        case _:
            print("Obrigado por utilizar meu algoritmo!")


