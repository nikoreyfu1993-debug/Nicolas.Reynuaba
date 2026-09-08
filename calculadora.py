def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

print("Calculadora básica")
print("Suma:", sumar(10, 5))
print("Resta:", restar(10, 5))
print("Multiplicación:", multiplicar(10, 5))
print("División:", dividir(10, 5))
