#Esse projeto tem por objetivo simular o jogo da velha

palavra = "leao"

progresso = ["_"] * len(palavra)

repeticao = 0

condicao = True

while condicao:
    print("Bem-vindo(a) ao  jogo da velha")
    print("DICA: é um animal mamífero selvagem")
    letra = input("Digite uma letra \n").lower()

    #verificando se a letra está na palavra
    if letra in palavra:
        print("Parabéns você acertou")
        for i, caractere in enumerate(palavra):
            if caractere == letra:
                progresso[i] = letra 
    else:
        repeticao +=1
        print(f"Você errou! Tente novamente. Tentativsad restantes {10 - repeticao}")

    #verifica o progresso
    for letra in progresso:
        print(letra, end=" ")

 #verifica se já conluiu a palavra
    if "_" not in progresso:
        print(f"Parabéns! Você venceu a palavra certa é {palavra}")
        condicao = False

    if repeticao>=10:
       print("Fim de jogo! Você atingiu o número máximo de tentativas.")
       print(f"A palavra correta era: {palavra}")
       condicao = False
        
       