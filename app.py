import random

# Iniciar com um numero aleatório entre 1 e 100
numero_alvo = random.randint(1, 100)
# Iniciar o chute do usuario antes do While
chute = 0

# Enquanto o chute do usuario for diferente do valor aleatório, continue no loop
while chute != numero_alvo:
    print(numero_alvo)

    try:
        chute = int(input('Chute um numero entre 1 e 100: '))
        # Para validar que a entrada não seja menor que 1 e nem maior que 100
        if 1 <= chute <= 100:
            # Condição caso o usuário acerte
            if chute == numero_alvo:
                print('Acertou!')
                continuar = input('Deseja continuar jogando? (s/n)? ')
                if continuar.lower() == 'n':
                    chute = numero_alvo
                else:
                    # Se caso quiser continuar jogando, a variavel chute volta a ser 0 para sair continuar no loop,
                    chute = 0
                    # E um novo número aleatório é gerado para um novo jogo
                    numero_alvo = random.randint(1, 100)
            # Condição caso o numero escolhido seja menor
            elif chute > numero_alvo:
                print('O número secreto é MENOR do que o escolhido por vc')
            # Condição caso o numero escolhido seja maior
            elif chute < numero_alvo:
                print('O número secreto é MAIOR do que o escolhido por vc')
        else:
            raise ValueError
    except ValueError:
        print('Por favor, digite apenas números de 1 a 100. Tente novamente...')
