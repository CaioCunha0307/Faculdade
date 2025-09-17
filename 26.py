positivos = []

for i in range(6):
    num = float(input())

if num > 0:
    positivos.append(num)

print(f"{len(positivos)} valores positivos\n{sum(positivos)/len(positivos):.1f}")