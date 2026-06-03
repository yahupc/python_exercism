def _is_valid_triangle(sides):
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)


def equilateral(sides):
    a, b, c = sides
    return _is_valid_triangle(sides) and a == b == c


def isosceles(sides):
    a, b, c = sides
    if not _is_valid_triangle(sides):
        return False
    return a == b or b == c or a == c


def scalene(sides):
    a, b, c = sides
    if not _is_valid_triangle(sides):
        return False
    return a != b and b != c and a != c


# def equilateral(sides):
#     a, b, c = sides
#     if a == b == c and a > 0:
#         return True
#     else:
#         return False
#
#
# def isosceles(sides):
#     a, b, c = sides
#     # Validar las condiciones minimas  de un triangulo.
#     if (a + b <= c) or (a + c <= b) or (b + c <= a):
#         return False
#     # Validar si no tiene dos lados iguales
#     if a == b or b == c or a == c:
#         return True
#     else:
#         return False
#
#
# def scalene(sides):
#     a, b, c = sides
#     if (a + b <= c) or (a + c <= b) or (b + c <= a):
#         return False
#     if equilateral(sides) or isosceles(sides):
#         return False
#     else:
#         return True
#
