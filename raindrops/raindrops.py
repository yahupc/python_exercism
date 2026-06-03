def convert(number):
    resultado = ""
    lista = [3, 5, 7]
    for i in lista:
        if not number % i:
            if i == 3:
                resultado += "Pling"
            elif i == 5:
                resultado += "Plang"
            elif i == 7:
                resultado += "Plong"
    return resultado if resultado else str(number)


print(convert(35))
