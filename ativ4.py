def calcular_retangulo(base, altura):
    area = (base * altura)
    perimetro = 2* (base+altura)
    Diagonal_do_retângulo = (base**2 + altura**2)**0.5
    return area, perimetro, Diagonal_do_retângulo

base = float(input("Digite a base do retângulo:"))
altura = float(input("Digite a altura do rentângulo:"))

area, perimetro, Diagonal_do_retângulo = calcular_retangulo(base, altura)
print("Área do retângulo: {:.2f}".format(area))
print("Perímetro do retângulo: {:.2f}".format(perimetro))
print("Diagonal do retângulo: {:.2f}".format(Diagonal_do_retângulo))
