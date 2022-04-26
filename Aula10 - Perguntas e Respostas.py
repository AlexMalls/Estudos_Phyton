Respostas_acertadas = 0
Perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual jogo o protagonista vira um deus da guerra? ',
        'respostas': {
            'a': 'Call of Duty',
            'b': 'God of War',
            'c': 'Rome',
            'd': 'Devil May Cry'
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta': 'Qual jogo o protagonista é azul e baseado em um ouriço? ',
        'respostas': {
            'a': 'Kirby',
            'b': 'Super Mario',
            'c': 'Pepsiman',
            'd': 'Sonic'
        },
        'resposta_certa': 'd'
    },
}
print()

for PC, PV in Perguntas.items():
    print()
    print(f'{PC}: {PV["pergunta"]}')

    for RC, RV in PV['respostas'].items():
        print(f'Alternativa [{RC}]: {RV}')

    print()
    Resposta_Usuario = input('Qual a resposta correta? ')
    if Resposta_Usuario == PV['resposta_certa']:
        print('Resposta Correta')
        Respostas_acertadas += 1
    else:
        print('Respota Errada')

print(f'Você acertou {Respostas_acertadas} pergunta(s) parabens') if Respostas_acertadas else print('Infelizmente você não acertou nenhuma resposta :(')
