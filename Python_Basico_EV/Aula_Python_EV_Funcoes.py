def lernotas():
    n=float(input("Digite uma nota para o aluno(a): "))
    return n


def resultado(n1,n2):
    media = (n1+n2)/2
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Média: {media}")
    if media >= 7:
        print("Resultado: Aprovado")
    else:
        print("Resultado: Reprovado")


a = lernotas()
b = lernotas()
resultado = resultado(a,b)