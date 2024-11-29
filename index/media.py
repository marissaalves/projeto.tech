print("Digite as notas das disciplinas (separadas por espaço):")
try:
    notas = list(map(float, input().split()))

    if not notas:
        print("Nenhuma nota foi inserida. Por favor, insira ao menos uma nota.")
    else:

        media = sum(notas) / len(notas)

        
        print("\n===== Resultado =====")
        print(f"Notas informadas: {', '.join(f'{n:.2f}' for n in notas)}")
        print(f"Média calculada: {media:.2f}")

        
        if media >= 7:
            print("Situação: Aluno aprovado! 🎉")
        elif 5 <= media < 7:
            print("Situação: Aluno em recuperação. 📚")
        else:
            print("Situação: Aluno reprovado. 😢")
        print("=====================")
except ValueError:
    
    print("\nErro: Entrada inválida.")
    print("Certifique-se de digitar apenas números separados por espaço (exemplo: 8.5 7 6.3).")
