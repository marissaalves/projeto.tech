print("Digite as notas das disciplinas (separadas por espaço):")
notas = list(map(float, input().split()))

media = sum(notas) / len(notas)

print(f"A média do aluno é: {media:.2f}")

if media >= 7:
    print("Aluno aprovado! 🎉")
elif 5 <= media < 7:
    print("Aluno em recuperação. 📚")
else:
    print("Aluno reprovado. 😢")

