nota1, nota2, nota3, nota4 = map(float, input().split(' '))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4))/(2 + 3 + 4 + 1)
print(f"Média: {media:.1f}")

if media >= 7:
    print("Aluno aprovado")

elif media <= 5:
    print("Aluno em exame")

    nota5 = float(input())
    print("Nota do exame: {:.1f}".format(nota5))
    media = (media + nota5)/2

    if media>= 5:
        print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")    

    print(f"Média Final: {media:.1f}")

else:
    print("Aluno reprovado")