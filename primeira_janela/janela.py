import tkinter as tk #importacao da biblioteca

#Criando a converção de Celsius para Fahrenheit
def conversaoc():
    conteudo = questcelcius.get() #Capturando o que for escrito na entrada de dados
    conteudo = float(conteudo) #Convertendo o conteúdo inserido em strings para float
    conteudo = (conteudo * 1.8 + 32) #Exercendo a conversão
    result.config(text=conteudo)#Atribuindo a mudanca de texto na variavel usando o .config

def conversaof():
    conteudo2 = questf.get()
    conteudo2 = float(conteudo2)
    conteudo2 = (conteudo2 - 32) / 1.8
    result2.config(text=conteudo2)

#Definindo tamanho da janela e expondo texto de orientação
root = tk.Tk() #Root é a janela, e tk.Tk() é o comando para executar o tkinter
root.title('Conversor de tempetura') #Titulo da janela do programa
root.geometry('800x600') #Definindo o tamanho inicial da janela

#Definindo texto da primeira pergunta para conversão em Celcius
guide_text = tk.Label(root, text="Digite o valor da sua conversão (Celcius para Fahrenheit)") #Texto que fica acima do botão de ação
guide_text.grid(row=0, column=0, padx=10, pady=10) #Define a posição do texto de pergunta
questcelcius = tk.Entry(root, width = '10') #Parte onde é inserido o valor desejado
questcelcius.grid(row=1, column=1, padx=20, pady=20) #Posição da caixa de pergunta

#Botão para captar quando pode ser executada a conversão de dados
botao = tk.Button(root, text="Clique para conventer", command=conversaoc) #Botão que vai chamar a função de conversão
botao.grid(row=1, column=0) #Posição
result_text = tk.Label(root, text='O resultado da conversão é: ')#Criado mais um texto de orientacao
result_text.grid(row=2, column=0)#Definidos os espacos do texto
result = tk.Label(root, text='')#Criando um espaco de texto vazio para receber a conversao do conteudo presente na funcao
result.grid(row=2, column=1)#Definindo posicao do result

#Criando a segunda parte usando os mesmos metodos (Nao comentados)
guide_text2 = tk.Label(root, text="Digite o valor da sua conversão (Fahrenheit para celcius)")
guide_text2.grid(row=5, column=0, padx=10, pady=10)
questf = tk.Entry(root, width = '10')
questf.grid(row=6, column=1, padx=20, pady=20)

botao2 = tk.Button(root, text="Clique para conventer", command=conversaof)
botao2.grid(row=6, column=0)
result2_text = tk.Label(root, text='O resultado da conversão é: ')
result2_text.grid(row=7, column=0)
result2 = tk.Label(root, text='')
result2.grid(row=7, column=1)

#O comando que vai manter o root (Nesse caso seria a janela) em looping infinito (Ou até que o usuário feche a janela)
root.mainloop() #Loop que vai manter o programa rodando até que a janela se feche
