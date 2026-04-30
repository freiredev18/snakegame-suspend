#Bibliotecas
import time
import sys

#Criando a funcao que vai percorrer e cada letra e expor na tela de forma lente
def narracao(texto):
    for letra in texto:
        sys.stdout.write(letra) #Escreve o caractere e mantem o cursor exatamente onde parou
        sys.stdout.flush() #Comando de acao para que o identador nao junte todas as letras no buff e depois exponha
        time.sleep(0.03) #Tempo para expor cada caractere
    print()

#Funcao para o poder de fogo
def poder_fogo():
    narracao('O ar é pesado, carregado com o cheiro acre de enxofre e o estalo rítmico de brasas que nunca se apagam. Você abre os olhos, {} e a primeira coisa que sente não é o sol, mas o calor pulsante que emana do solo negro da Cratera de Ignis.'.format(nomeperson))
    narracao('Sua pele não queima; ela reconhece o berço. Mas, ao levar a mão ao peito, um vazio gélido te atinge. O Amuleto de Enxofre, o receptáculo da sua essência, sumiu.')
    narracao('À distância, em meio às cortinas de fumaça, uma silhueta se esgueira. Um saqueador das sombras corre com o seu brilho carmesim nas mãos. O sangue em suas veias ferve... é hora de agir')
    while True:
        narracao('Um saqueador tenta roubar seu amuleto, o que voce faz? (Queimar/Intimidar)')
        ladrao = input()
        ladrao = ladrao.upper()
        ladraoc = ['QUEIMAR', 'INTIMIDAR']
        if ladrao not in ladraoc:
            print('Digite uma opcao valida!')
        else:
            print('Voce escolheu {}'.format(ladrao))
        if ladrao == ('QUEIMAR'):
            narracao('Você estende a mão e o ar ao redor se incendeia instantaneamente. Um raio de fogo puro cruza o vale, reduzindo o ladrão a cinzas antes mesmo que ele pudesse gritar. Você caminha entre as chamas, recupera seu amuleto do chão chamuscado e sente o peso do silêncio. O mundo agora teme o seu rastro.')
        elif ladrao == ('INTIMIDAR'):
            narracao('Você solta um rugido que faz a própria cratera tremer. O calor que emana de você distorce a visão, criando uma aura de sol apocalíptico. O ladrão tropeça, paralisado pelo pavor de enfrentar um verdadeiro senhor das chamas. Ele larga o amuleto e foge aos prantos, sabendo que a misericórdia foi o único motivo de sua vida ter sido poupada, todos reconhecem seu respeito.')
            break

    if ladrao == ('QUEIMAR'):
        status_fogo = ('TEMIDO')
    else:
        status_fogo = ('RESPEITADO')
    
    while True:
        narracao('Após horas de caminhada sob o sol implacável, as imponentes muralhas de ferro de Aethelgard surgem no horizonte. O calor que emana de você faz o ar tremer ao redor do seu corpo, anunciando sua chegada muito antes de você alcançar o fosso.')
        if status_fogo == ('TEMIDO'):
            narracao("Lanças apontadas. 'Afastem-se, maldito!', grita o capitão. 'Não tragam cinzas para cá'.")
            narracao('Voce tem duas opcoes quais voce escolhe? (LUTAR/SUBORNAR)')
            temido_luta = input()
            temido_luta = temido_luta.upper()
            temido_options = ['LUTAR', 'SUBORNAR']
            if temido_luta not in temido_options:
                print('Digite uma opcao valida!')
            elif temido_luta == ('LUTAR'):
                narracao('Voce escolheu LUTAR!')
            elif temido_luta == ('SUBORNAR'):
                narracao('Voce escolheu SUBORNAR!')
                             
        if status_fogo == ('RESPEITADO'):
            narracao("Punhos no peito. 'Luz no caminho, Guardião!', saúda o capitão. 'Aethelgard precisa de você.")
            narracao('Voce tem duas opcoes quais voce escolhe? (INFORMACAO/DESCANSO)')
            respeitado_escolha = input()
            respeitado_escolha = respeitado_escolha.upper()
            respeitado_options = ['INFORMACAO', 'DESCANSO']
            if respeitado_escolha not in respeitado_options:
                print('Digite uma opcao valida!')
            elif respeitado_escolha == ('INFORMACAO'):
                narracao('Voce escolheu INFORMACAO!')
            elif temido_luta == ('DESCANSO'):
                narracao('Voce escolheu DESCANSO!')
                break

    while True:
        narracao('O setor leste arde. A Grande Biblioteca está sendo devorada. Milênios de história em risco')
        narracao('Voce possui duas opcoes, qual delas voce escolhe? (ABSORVER) o fogo (Cansa você) | (DEIXAR) queimar (Poupa energia)')
        bibliotecaop = ['ABSORVER', 'DEIXAR']
        bibliotecac = input()
        bibliotecac = bibliotecac.upper()
        if bibliotecac not in bibliotecaop:
            print('Digite uma opcao valida!')
        else:
            print('Voce escolheu {}!'.format(bibliotecac))
        if bibliotecac == ('ABSORVER'):
            print('Você usa um Selo Ancestral aprendido nos livros. O vilão é selado pela sabedoria')
        else:
            print('Resta apenas a Fúria Bruta. Você explode sua alma para vaporizar as sombras')
            break
        
#Apresentacao do jogo
print('=='*60 + '\n')
narracao('Olá jogador, seja bem vindo ao nosso jogo de RPG: Éter - O Último Guardião ')
narracao('Nesta jornada, o seu maior poder não é o elemento que você carrega, mas as decisões que você toma.')
narracao('1. Escolha seu Destino: Logo no início, você deve se vincular a um dos quatro elementos ancestrais. Isso mudará sua história, seus diálogos e seu final.')
narracao('2. Comandos: O jogo apresentará opções entre parênteses, como (falar/lutar) ou (norte/sul). Digite a palavra escolhida e aperte Enter para avançar.')
narracao('3. Consequências: Como este é um conto curto, cada decisão tem um peso enorme. Não há caminhos neutros; você será levado rapidamente ao seu destino... ou à sua ruína.\n')
narracao('Escolha com sabedoria, o equilibrio de Aethelgard esta em suas maos...\n')
print('=='*60 + '\n')

#Escolhendo o caminho do jogador
narracao('Vamos para a melhor parte da sua jornada, mostrarei a seguir as bencaos que seu personagem pode obter: \n')
narracao('1. O fogo não pede permissão; ele consome para transformar. Escolher as brasas é abraçar a força bruta e a coragem impetuosa. Em Aethelgard, você será a luz que afasta as sombras... ou o incêndio que as devora.')
narracao('2. A água molda a rocha não pela força, mas pela persistência. Como um Tecelão das Marés, você entende que a verdadeira força reside na adaptação. Seja calmo como um lago ou implacável como um tsunami')
narracao('3. Enquanto impérios caem, as montanhas permanecem. Vincular-se à terra é tornar-se o escudo de Aethelgard. Você será a base inabalável, o guardião que protege os fracos com a força da pedra milenar')
narracao('4. Onde outros veem barreiras, você vê caminhos. Invisível, rápido e livre de amarras. O vento não pode ser capturado, e seus inimigos descobrirão que você está em todos os lugares, mas em lugar nenhum \n')
print('=='*60 + '\n')

#Pergunta do nome do personagem]
while True:
    narracao('Digite o nome do seu personagem: ')
    nomeperson = input()
    if nomeperson.isalpha():
        print('Seu nome e {}'.format(nomeperson))
        break
    else:
        print('Digite um nome valido! (Somente letras)')
        

#Criando pergunta que vai definir o poder e caminho escolhido pelo jogador, logo apos vai executar as funcoes de cada poder
while True:
    bencaos = ['FOGO', 'AGUA', 'TERRA', 'AR']
    narracao('Digite qual bencao seu pernosagem possuira: (Fogo/Agua/Terra/Ar) ')
    bencaojg = input()
    bencaojg = bencaojg.upper()
    if bencaojg not in bencaos:
        print('Digite uma bencao valida!')
    else:
        print('Voce escolheu a bencao: ' + bencaojg)
        break

while True:
   if bencaojg == ('fogo'):
        poder_fogo()
#    elif bencaojg == ('AGUA'):
#        poder_agua()
#    elif bencaojg == ('TERRA'):
#        poder_terra()
#    elif bencaojg == ('AR'):
#        poder_ar()
        break    
