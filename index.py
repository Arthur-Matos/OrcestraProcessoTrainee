#coding utf-8

#Compra Burguers

import os
from time import sleep

def limpar():
    sleep(2)
    os.system("clear")

choose = [1, 2, 3, 4]
Valor = 0
burguer = 16
salada = 14
tudo = 22
suco = 4
refri = 5
drink = 9

while True:
    print("""
    ------Menu------
        
    Olá, escolha o seu serviço.
    
    [ 1 ] Escolha seu lanche
    [ 2 ] Escolha Bebida
    [ 3 ] Valor Atual
    [ 4 ] Terminar operação

    """)
    op = int(input("\tOpção:"))
    if op in choose:
        if op == 1:
            limpar()
            print("""
            Opções de Hamburguers:

            [ 1 ]X-burger R$ 16,00
            [ 2 ]X-Salada R$ 14,00
            [ 3 ]X-Tudo R$ 22,00
            [ 4 ]Retornar

        """)
            op_1 = int(input("Opção:"))
            if op_1 in choose:
                if op_1 == 1:
                    Valor += burguer
                    limpar()
                elif op_1 == 2:
                    Valor += salada
                    limpar()
                elif op_1 == 3:
                    Valor += tudo
                    limpar()
                elif op_1 == 4:
                    print("RETORNANDO...")
                    limpar()
            elif op_1 not in choose:
                print("\n\t Opção inexistente.")
                limpar()
        elif op == 2:
            limpar()
            print("""
            Opções de Bebidas
            
            [ 1 ]Refrigerante R$ 5,00
            [ 2 ]Suco R$ 4,00
            [ 3 ]Drink R$ 9,00
            [ 4 ]Retornar
            """)
            op_2 = int(input("\nOpção:"))
            if op_2 in choose:
                if op_2 == 1:
                    Valor += refri
                    limpar()
                elif op_2 == 2:
                    Valor += suco
                    limpar()
                elif op_2 == 3:
                    Valor += drink
                    limpar()
                elif op_2 == 4:
                    print("RETORNANDO...")
                    limpar()
            elif op_2 not in choose:
                print("\nOpção inexistente.")
                limpar()
        elif op == 3:
            limpar()
            print("Essa é sua conta atual R${},00.".format(Valor))
            op_3 = input("Insira algo para retornar:")
            if op_3 == '1':
                print("RETORNANDO...")
                limpar()
            else:
                print("RETORNANDO...")
                limpar()
        elif op == 4:
            limpar()
            print("ENCERRANDO...")
            quit()
    elif op not in choose:
        print("\nOpção inexistente")
        limpar()