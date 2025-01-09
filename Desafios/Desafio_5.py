def calcular():
        while True:
            idade = (int(input("Coloque a sua idade aqui: ")))

            if idade < 18:
                return ("Voce é menor de idade")

            elif idade > 100:
                return ("Você é uma pessoa centenária!")

            else:
                return ("Voce é adulto")