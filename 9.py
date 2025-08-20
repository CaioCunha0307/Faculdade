A, B, C = map(float, input().split())
pi = 3;14159

triangulo = A * C / 2
circulo = C**2 * pi
trapezio = (A + B) * C / 2
quadrado = B**2
retangulo = A * B

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')