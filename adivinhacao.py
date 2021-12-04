import random
from datetime import datetime


# imports

# Definindo a saldação do dia
def retorna_hora():
    hora = datetime.now()
    hora_format = hora.strftime('%H:%M')
    return hora_format


hora_formatada = retorna_hora()


def retorna_saldacao():
    if hora_formatada < '12':
        return 'Bom Dia'
    elif hora_formatada < '18':
        return 'Boa Tarde'
    else:
        return 'Boa noite'


saldacao = retorna_saldacao()

# Pontuação do jogo
pontuacao = 1000


# Abertura/apresentação do jogo
def abertura_jogo():
    print('-' * 20)
    print('{} {}\nBem-vindo ao jogo'.format(saldacao, hora_formatada))
    print('-' * 20)


abertura_jogo()

# Número principal randomico entre 1 e 100
num = round(random.randrange(1, 100 + 1))


# Definindo o nível do jogo
def retorna_nivel():
    print('(1)Fácil (2)Médio (3)Difícil ')
    while True:
        nivel_usuario = int(input('Insira o nível: '))
        if nivel_usuario < 1 or nivel_usuario > 3:
            print('Por favor insira corretamente!')
        else:
            break
    return nivel_usuario


usuario_nivel = retorna_nivel()


# definindo o número de tentativas de acordo com o nível
def define_tentativas():
    facil, medio, dificil = usuario_nivel == 1, usuario_nivel == 2, usuario_nivel == 3
    if facil:
        tentativas = 15
    elif medio:
        tentativas = 10
    else:
        tentativas = 5
    return tentativas


tentativas_usuario = define_tentativas()


# exibe game over
def exibe_game_over():
    print('Game Over :(')
    print('O número é {}'.format(num))


# Definindo o chute do usuário e iniciando o jogo
while True:
    chute = int(input('Insira um número entre 1 e 100: '))
    if chute < 1 or chute > 100:
        print('Por favor, insira corretamente!')
    else:
        while chute != num:
            pontuacao -= chute
            tentativas_usuario -= 1
            break
        if pontuacao <= 0 or tentativas_usuario <= 0:
            exibe_game_over()
            break
        if chute == num:
            print('Tentativas: {} Pontuação {}'.format(
                tentativas_usuario, pontuacao))
            print('Você acertou!!')
            break
        elif chute < num:
            print('Tentativas: {} Pontuação {}'.format(
                tentativas_usuario, pontuacao))
            print('Mais pra cima')
            print('-' * 20)
            continue
        else:
            print('Tentativas: {} Pontuação {}'.format(
                tentativas_usuario, pontuacao))
            print('Mais pra baixo')
            print('-' * 20)
            continue
