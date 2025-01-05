def calcule():

    num1 = int(input("Digite um Valor: "))
    num2 = int(input("Digite um segundo Valor: "))

    soma = num1 + num2


    print(f"{num1} + {num2} = {soma}")


while True:
    calcule()
    Continue = input("Deseja continuar? (s/n):").strip()
    if Continue != 's':
        print("Encerrando o programa...")
        break