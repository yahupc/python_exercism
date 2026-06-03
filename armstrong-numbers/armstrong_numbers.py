def is_armstrong_number(number):
    digitos = [int(d) for d in str(number)]
    exponenete = len(digitos)
    return sum([d**exponenete for d in digitos]) == number
