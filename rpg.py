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
    # Primeira escolha
    narracao('O ar é pesado, carregado com o cheiro acre de enxofre e o estalo rítmico de brasas que nunca se apagam. Você abre os olhos, {}, e a primeira coisa que sente não é o sol, mas o calor pulsante que emana do solo negro da Cratera de Ignis.'.format(nomeperson))
    narracao('Sua pele não queima; ela reconhece o berço. Mas, ao levar a mão ao peito, um vazio gélido te atinge. O Amuleto de Enxofre, o receptáculo da sua essência, sumiu.')
    narracao('À distância, em meio às cortinas de fumaça, uma silhueta se esgueira. Um saqueador das sombras corre com o seu brilho carmesim nas mãos. O sangue em suas veias ferve... é hora de agir.')
    narracao('Um saqueador tenta roubar seu amuleto, o que você faz? (Queimar/Intimidar)')
    
    ladrao = input()
    ladrao = ladrao.upper()
    ladraoc = ['QUEIMAR', 'INTIMIDAR']
    
    if ladrao not in ladraoc:
        print('Digite uma opção válida!')
    else:
        print('Você escolheu {}'.format(ladrao))
        
    if ladrao == ('QUEIMAR'):
        narracao('Você estende a mão e o ar ao redor se incendeia instantaneamente. Um raio de fogo puro cruza o vale, reduzindo o ladrão a cinzas antes mesmo que ele pudesse gritar. Você caminha entre as chamas, recupera seu amuleto do chão chamuscado e sente o peso do silêncio. O mundo agora teme o seu rastro.')
        status_fogo = ('TEMIDO')
    elif ladrao == ('INTIMIDAR'):
        narracao('Você solta um rugido que faz a própria cratera tremer. O calor que emana de você distorce a visão, criando uma aura de sol apocalíptico. O ladrão tropeça, paralisado pelo pavor de enfrentar um verdadeiro senhor das chamas. Ele larga o amuleto e foge aos prantos, sabendo que a misericórdia foi o único motivo de sua vida ter sido poupada. Todos reconhecem seu respeito.')
        status_fogo = ('RESPEITADO')

    # Segunda escolha
    narracao('Após horas de caminhada sob o sol implacável, as imponentes muralhas de ferro de Aethelgard surgem no horizonte. O calor que emana de você faz o ar tremer ao redor do seu corpo, anunciando sua chegada muito antes de você alcançar o fosso.')
    
    if status_fogo == ('TEMIDO'):
        narracao("Lanças apontadas. 'Afastem-se, maldito!', grita o capitão. 'Não tragam cinzas para cá'.")
        narracao('Você tem duas opções, quais você escolhe? (LUTAR/SUBORNAR)')
        temido_luta = input()
        temido_luta = temido_luta.upper()
        temido_options = ['LUTAR', 'SUBORNAR']
        
        if temido_luta not in temido_options:
            print('Digite uma opção válida!')
        elif temido_luta == ('LUTAR'):
            narracao('Você escolheu LUTAR!')
        elif temido_luta == ('SUBORNAR'):
            narracao('Você escolheu SUBORNAR!')
            
    # Ajuste de indentação para que o bloco RESPEITADO funcione corretamente
    if status_fogo == ('RESPEITADO'):
        narracao("Punhos no peito. 'Luz no caminho, Guardião!', saúda o capitão. 'Aethelgard precisa de você'.")
        narracao('Você tem duas opções, quais você escolhe? (INFORMACAO/DESCANSO)')
        respeitado_escolha = input()
        respeitado_escolha = respeitado_escolha.upper()
        respeitado_options = ['INFORMACAO', 'DESCANSO']
        
        if respeitado_escolha not in respeitado_options:
            print('Digite uma opção válida!')
        elif respeitado_escolha == ('INFORMACAO'):
            narracao('Você escolheu INFORMAÇÃO!')
        elif respeitado_escolha == ('DESCANSO'):
            narracao('Você escolheu DESCANSO!')
    
    # Terceira escolha
    narracao('O setor leste arde. A Grande Biblioteca está sendo devorada. Milênios de história em risco.')
    narracao('Você possui duas opções, qual delas você escolhe? (ABSORVER) o fogo (Cansa você) | (DEIXAR) queimar (Poupa energia)')
    
    bibliotecaop = ['ABSORVER', 'DEIXAR']
    bibliotecac = input()
    bibliotecac = bibliotecac.upper()
    
    if bibliotecac not in bibliotecaop:
        print('Digite uma opção válida!')
    else:
        print('Você escolheu {}!'.format(bibliotecac))
        
    if bibliotecac == ('ABSORVER'):
        narracao('Você usa um Selo Ancestral aprendido nos livros. O vilão é selado pela sabedoria.\n')
        print('=='*60 + '\n')
    else:
        narracao('Resta apenas a Fúria Bruta. Você explode sua alma para vaporizar as sombras.\n')
        print('=='*60 + '\n')

#Criando funcao da agua
def poder_agua():
    # Primeira escolha
    narracao('O silêncio é profundo, interrompido apenas pelo pulsar rítmico das correntes e o brilho azulado das águas abissais. Você abre os olhos, {}, e sente o peso de quilômetros de oceano sobre seus ombros, mas a água não te esmaga; ela te abraça nas Ruínas de Vidro.'.format(nomeperson))
    narracao('Você nota que o fluxo das marés ao seu redor está agitado. Uma Corrente Corrompida, negra como tinta, está sufocando os corais ancestrais que dão vida ao seu povo.')
    narracao('Um espírito marinho corrompido surge das sombras, bloqueando seu caminho com tentáculos de energia sombria. O que você faz? (Purificar/Esmagar)')
    
    espirito = input()
    espirito = espirito.upper()
    espiritoc = ['PURIFICAR', 'ESMAGAR']
    
    if espirito not in espiritoc:
        print('Digite uma opção válida!')
    else:
        print('Você escolheu {}'.format(espirito))
        
    if espirito == ('PURIFICAR'):
        narracao('Você estende as mãos e uma luz turquesa emana do seu peito. A água ao redor gira em um redemoinho de pureza, limpando a corrupção do espírito. Ele se dissolve em bolhas cristalinas, deixando para trás uma pérola de gratidão. As águas agora te veem como um Salvador.')
        status_agua = ('CALMO')
    elif espirito == ('ESMAGAR'):
        narracao('Você fecha o punho e a pressão da água ao redor do espírito aumenta violentamente. Em um estalo hidrostático, você implode a criatura, dispersando a escuridão à força. O oceano treme com sua demonstração de poder. As águas agora temem sua fúria.')
        status_agua = ('IMPLACÁVEL')

    # Segunda escolha
    narracao('Emergindo das profundezas, você alcança os portões traseiros de Aethelgard, onde os canais da cidade encontram o mar. A umidade que você carrega anuncia sua linhagem real antes mesmo de você tocar o ferro dos portões.')
    
    if status_agua == ('IMPLACÁVEL'):
        narracao("Sentinelas em alerta. 'Atrás da grade, monstro das marés!', grita o vigia. 'Sua corrente é perigosa demais para nossas ruas'.")
        narracao('Você tem duas opções, qual você escolhe? (INUNDAR/NEGOCIAR)')
        implacavel_escolha = input()
        implacavel_escolha = implacavel_escolha.upper()
        implacavel_options = ['INUNDAR', 'NEGOCIAR']
        
        if implacavel_escolha not in implacavel_options:
            print('Digite uma opção válida!')
        elif implacavel_escolha == ('INUNDAR'):
            narracao('Você escolheu INUNDAR!')
        elif implacavel_escolha == ('NEGOCIAR'):
            narracao('Você escolheu NEGOCIAR!')
            
    if status_agua == ('CALMO'):
        narracao("Portões se abrem. 'As marés trouxeram paz!', exclama o guarda. 'Entre, Guardião, a sede da cidade é grande'.")
        narracao('Você tem duas opções, qual você escolhe? (CURAR/GUIAR)')
        calmo_escolha = input()
        calmo_escolha = calmo_escolha.upper()
        calmo_options = ['CURAR', 'GUIAR']
        
        if calmo_escolha not in calmo_options:
            print('Digite uma opção válida!')
        elif calmo_escolha == ('CURAR'):
            narracao('Você escolheu CURAR!')
        elif calmo_escolha == ('GUIAR'):
            narracao('Você escolheu GUIAR!')

    # Terceira escolha
    narracao('O reservatório central de Aethelgard foi envenenado por um alquimista traidor. A população está morrendo de sede enquanto a água se torna lodo verde.')
    narracao('Você possui duas opções, qual delas você escolhe? (FILTRAR) a toxina (Exige foco) | (SACRIFICAR) uma parte do seu poder para renovar a fonte.')
    
    reservatorioop = ['FILTRAR', 'SACRIFICAR']
    reservatorioc = input()
    reservatorioc = reservatorioc.upper()
    
    if reservatorioc not in reservatorioop:
        print('Digite uma opção válida!')
    else:
        print('Você escolheu {}!'.format(reservatorioc))
        
    if reservatorioc == ('FILTRAR'):
        narracao('Você dança entre as moléculas de água, separando o veneno com precisão cirúrgica. A pureza retorna, e você é coroado como o mestre das águas.\n')
        print('=='*60 + '\n')
    else:
        narracao('Você mergulha no lodo e libera toda sua essência vital. A explosão de energia limpa o reservatório instantaneamente, mas você sente sua conexão com o mar enfraquecer para sempre.\n')
        print('=='*60 + '\n')

#Criando funcao do poder terra
def poder_terra():
    # Primeira escolha
    narracao('O ar é denso, saturado com o cheiro de terra úmida e o som surdo de placas tectônicas se movendo nas profundezas. Você abre os olhos, {}, e sente uma conexão inabalável com o solo vibrante das Cavernas de Obsidiana.'.format(nomeperson))
    narracao('Seus músculos são como rocha; você é parte da montanha. Mas, ao tocar o solo, uma vibração errada percorre seus pés. O Cristal Terreno, o núcleo da sua força, foi arrancado do altar sagrado.')
    narracao('Um escavador das sombras foge apressado por uma fenda, arrastando sua relíquia preciosa. A terra sob seus pés clama por justiça... é hora de agir.')
    narracao('Um escavador roubou seu cristal, o que você faz? (ESMAGAR/IMOBILIZAR)')
    
    escavador = input()
    escavador = escavador.upper()
    escavadorc = ['ESMAGAR', 'IMOBILIZAR']
    
    if escavador not in escavadorc:
        print('Digite uma opção válida!')
    else:
        print('Você escolheu {}'.format(escavador))
        
    if escavador == ('ESMAGAR'):
        narracao('Você golpeia o chão e uma estalactite massiva se desprende do teto, esmagando o ladrão sob toneladas de rocha pura. Você recupera o cristal das mãos sem vida e o chão silencia. Agora, a terra conhece a sua fúria impiedosa.')
        status_terra = ('TEMIDO')
    elif escavador == ('IMOBILIZAR'):
        narracao('Você faz o chão se erguer como mãos de pedra, prendendo o ladrão em um casulo inquebrável. Ele implora por misericórdia enquanto você retoma o cristal sem derramar sangue. Você provou que a força da terra pode ser justa. Todos reconhecem sua autoridade.')
        status_terra = ('RESPEITADO')

    # Segunda escolha
    narracao('Após cruzar vales rochosos e desfiladeiros, as colossais muralhas de ferro de Aethelgard surgem no horizonte. Cada passo seu faz o solo tremer levemente, anunciando a chegada de um lorde telúrico muito antes de você alcançar o fosso.')
    
    if status_terra == ('TEMIDO'):
        narracao("Arqueiros se preparam. 'Pare aí, abalador de mundos!', grita o capitão. 'Não queremos seus terremotos e destruição aqui'.")
        narracao('Você tem duas opções, quais você escolhe? (DERRUBAR/SUBORNAR)')
        temido_terra = input()
        temido_terra = temido_terra.upper()
        temido_options = ['DERRUBAR', 'SUBORNAR']
        
        if temido_terra not in temido_options:
            print('Digite uma opção válida!')
        elif temido_terra == ('DERRUBAR'):
            narracao('Você escolheu DERRUBAR!')
        elif temido_terra == ('SUBORNAR'):
            narracao('Você escolheu SUBORNAR!')
            
    if status_terra == ('RESPEITADO'):
        narracao("Sentinelas batem os escudos no chão. 'A montanha caminha conosco!', saúda o capitão. 'Aethelgard precisa da sua resiliência'.")
        narracao('Você tem duas opções, quais você escolhe? (REFORÇAR/ESTRATÉGIA)')
        respeitado_terra = input()
        respeitado_terra = respeitado_terra.upper()
        respeitado_options = ['REFORÇAR', 'ESTRATÉGIA']
        
        if respeitado_terra not in respeitado_options:
            print('Digite uma opção válida!')
        elif respeitado_terra == ('REFORÇAR'):
            narracao('Você escolheu REFORÇAR!')
        elif respeitado_terra == ('ESTRATÉGIA'):
            narracao('Você escolheu ESTRATÉGIA!')

    # Terceira escolha
    narracao('O Distrito das Minas de Aethelgard está desmoronando após um ataque. Centenas de trabalhadores estão presos nos níveis inferiores enquanto o teto cede.')
    narracao('Você possui duas opções, qual delas você escolhe? (SUSTENTAR) o peso da montanha (Exige esforço físico letal) | (SOTERRAR) a entrada para impedir o avanço das sombras (Sacrifica os mineradores).')
    
    minasop = ['SUSTENTAR', 'SOTERRAR']
    minasc = input()
    minasc = minasc.upper()
    
    if minasc not in minasop:
        print('Digite uma opção válida!')
    else:
        print('Você escolheu {}!'.format(minasc))
        
    if minasc == ('SUSTENTAR'):
        narracao('Você se torna um pilar vivo, segurando milhões de toneladas enquanto os inocentes fogem. Seus ossos rangem, mas sua lenda é gravada na pedra eterna.\n')
        print('=='*60 + '\n')
    else:
        narracao('Com um movimento seco, você lacra as minas para sempre. O mal é contido, mas os gritos dos esquecidos ecoarão em sua consciência sob a terra fria.\n')
        print('=='*60 + '\n')
#Criando o poder AR

def poder_ar():
    # Primeira escolha
    narracao('O ar é rarefeito, gélido e assobia entre os picos flutuantes das Ilhas de Zephyrus. Você abre os olhos, {}, e a primeira coisa que sente não é o chão firme, mas a leveza absoluta de quem nasceu para dominar os céus.'.format(nomeperson))
    narracao('Seu corpo parece feito de brisa, mas seu coração bate forte. Ao olhar para o altar de cristal, você percebe que a Essência de Éter, o sopro que mantém as ilhas flutuando, foi roubado.')
    narracao('Um renegado alado mergulha entre as nuvens carregando sua luz prateada. Se você não agir agora, o céu irá desabar... é hora de agir.')
    narracao('Um renegado roubou sua essência, o que você faz? (TORNADO/CORTE)')
    
    renegado = input()
    renegado = renegado.upper()
    renegadoc = ['TORNADO', 'CORTE']
    
    if renegado not in renegadoc:
        print('Digite uma opção válida!')
    else:
        print('Você escolheu {}'.format(renegado))
        
    if renegado == ('TORNADO'):
        narracao('Você gira as mãos e cria um vórtice furioso que engole o renegado. O impacto o arremessa contra as rochas, recuperando a essência enquanto o inimigo desaparece no abismo. O céu ruge com sua fúria. Agora, todos temem a tempestade que você carrega.')
        status_ar = ('DESTRUTOR')
    elif renegado == ('CORTE'):
        narracao('Você move os dedos como lâminas invisíveis, criando vácuos que desequilibram o voo do ladrão. Ele cai suavemente em uma rede de vento que você teceu, entregando a essência por puro medo da sua precisão. Você provou que o ar é sutileza. Todos reconhecem seu domínio.')
        status_ar = ('LIVRE')

    # Segunda escolha
    narracao('Planando sobre as correntes térmicas, as torres prateadas de Aethelgard surgem entre as nuvens. O vento que te precede faz as bandeiras da cidade estalarem violentamente, anunciando a chegada de um senhor dos ventos.')
    
    if status_ar == ('DESTRUTOR'):
        narracao("Bestas apontadas para o céu. 'Pouse imediatamente, portador do caos!', ordena o capitão. 'Não permitiremos furacões dentro de nossos muros'.")
        narracao('Você tem duas opções, qual você escolhe? (DISPERSAR/DESPISTAR)')
        destrutor_ar = input()
        destrutor_ar = destrutor_ar.upper()
        destrutor_options = ['DISPERSAR', 'DESPISTAR']
        
        if destrutor_ar not in destrutor_options:
            print('Digite uma opção válida!')
        elif destrutor_ar == ('DISPERSAR'):
            narracao('Você escolheu DISPERSAR!')
        elif destrutor_ar == ('DESPISTAR'):
            narracao('Você escolheu DESPISTAR!')
            
    if status_ar == ('LIVRE'):
        narracao("Saudações dos observadores. 'O sopro da esperança chegou!', grita o capitão. 'Aethelgard precisa de olhos no céu'.")
        narracao('Você tem duas opções, qual você escolhe? (VIGILÂNCIA/TRANSPORTE)')
        livre_ar = input()
        livre_ar = livre_ar.upper()
        livre_options = ['VIGILÂNCIA', 'TRANSPORTE']
        
        if livre_ar not in livre_options:
            print('Digite uma opção válida!')
        elif livre_ar == ('VIGILÂNCIA'):
            narracao('Você escolheu VIGILÂNCIA!')
        elif livre_ar == ('TRANSPORTE'):
            narracao('Você escolheu TRANSPORTE!')

    # Terceira escolha
    narracao('Um miasma tóxico e pesado, criado por experimentos sombrios, estagnou sobre a praça principal de Aethelgard. Os pulmões do povo estão falhando.')
    narracao('Você possui duas opções, qual delas você escolhe? (PURIFICAR) o ar (Exige um esforço imenso) | (SOPRAR) para longe (Limpa a cidade, mas contamina as vilas vizinhas).')
    
    miasmaop = ['PURIFICAR', 'SOPRAR']
    miasmac = input()
    miasmac = miasmac.upper()
    
    if miasmac not in miasmaop:
        print('Digite uma opção válida!')
    else:
        print('Você escolheu {}!'.format(miasmac))
        
    if miasmac == ('PURIFICAR'):
        narracao('Você respira o veneno para dentro de si, usando seu corpo como filtro elemental. A cidade respira aliviada enquanto você se torna o herói que sacrificou a própria paz pelo povo.\n')
        print('=='*60 + '\n')
    else:
        narracao('Com uma rajada poderosa, você varre a névoa para fora dos muros. A cidade está salva, mas ao longe, você vê as fumaças negras atingindo os inocentes no horizonte. O preço da liberdade é amargo.\n')
        print('=='*60 + '\n')

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
# Pergunta o nome do personagem
while True:
    narracao('Digite o nome do seu personagem: ')
    nomeperson = input()
    if nomeperson.isalpha():
        print('Seu nome é {}'.format(nomeperson))
        break
    else:
        print('Digite um nome válido! (Somente letras)')

# Criando a pergunta que definirá o poder e o caminho escolhido pelo jogador; logo após, executará as funções de cada poder
while True:
    bencaos = ['FOGO', 'AGUA', 'TERRA', 'AR']
    narracao('Digite qual bênção seu personagem possuirá: (Fogo/Agua/Terra/Ar) ')
    bencaojg = input()
    bencaojg = bencaojg.upper()
    if bencaojg not in bencaos:
        print('Digite uma bênção válida!')
    else:
        print('Você escolheu a bênção: ' + bencaojg)
        break

#Criando a execução de cada poder escolhido
if bencaojg == ('FOGO'):
    poder_fogo()
elif bencaojg == ('AGUA'):
    poder_agua()
elif bencaojg == ('TERRA'):
    poder_terra()
elif bencaojg == ('AR'):
    poder_ar()

narracao('A poeira baixa sobre Aethelgard, e o eco das suas escolhas ressoa pelas eras. O destino que você moldou com suas mãos — seja através das chamas, das marés, das rochas ou dos ventos — agora faz parte da tapeçaria eterna deste mundo.\n')
narracao('Obrigado por trilhar este caminho conosco!\n')
narracao('Este foi um projeto simples, nascido do código e da imaginação, mas cada decisão sua deu vida a esses parágrafos. Esperamos que você tenha sentido o peso do seu poder e que tenha gostado da jornada.\n')
narracao('Quem sabe o que o futuro reserva? Outros elementos ainda aguardam por um portador...\n')
narracao('Até a próxima convergência!')
print('=='*60 + '\n')