
#Sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
#def function(resp):
for p in perguntas:
    print('Pergunta:\n',p.get('Pergunta'))

    resposta = p.get('Opções')
    for i, r in enumerate(resposta):
        print(f'{i}) {r}\n')
    
    opcao = input('\nEscolha uma opção: \n')

   
    if opcao == p.get('Resposta'):
        print('Você ACERTOU!!!')
    else:
         print('Você ERROU!!!')
    
        
