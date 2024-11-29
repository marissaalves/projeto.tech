print("Digite as notas das disciplinas (separadas por espaço):")
try:
    notas = list(map(float, input().split()))
    
    if not notas:  
        print("Nenhuma nota foi inserida. Tente novamente.")
    else:
        media = sum(notas) / len(notas)

        print(f"\nA média do aluno é: {media:.2f}")

        if media >= 7:
            print("Situação: Aluno aprovado! 🎉")
        elif 5 <= media < 7:
            print("Situação: Aluno em recuperação. 📚")
        else:
            print("Situação: Aluno reprovado. 😢")
except ValueError:
    print("Entrada inválida. Certifique-se de digitar apenas números separados por espaço.")
