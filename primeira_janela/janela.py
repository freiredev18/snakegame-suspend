import tkinter as tk

#Criando a converção de Celsius para Fahrenheit
def conversaoc():
    conteudo = questcelcius.get() #Capturando o que for escrito na entrada de dados
    conteudo = float(conteudo) #Convertendo o conteúdo inserido em strings para float
    print(conteudo * 1.8 + 32) #Exercendo a conversão

#Definindo tamanho da janela e expondo texto de orientação
root = tk.Tk() #Root é a janela, e tk.Tk() é o comando para executar o tkinter
root.title('Conversor de tempetura') #Titulo da janela do programa
root.geometry('800x600') #Definindo o tamanho inicial da janela

#Definindo texto da primeira pergunta para conversão em Celcius
guide_text = tk.Label(root, text="Digite o valor da sua conversão") #Texto que fica acima do botão de ação
guide_text.grid(row=0, column=0, padx=10, pady=10) #Define a posição do texto de pergunta
questcelcius = tk.Entry(root, width = '30') #Parte onde é inserido o valor desejado
questcelcius.grid(row=1, column=1, padx=20, pady=20) #Posição da caixa de pergunta

#Botão para captar quando pode ser executada a conversão de dados
botao = tk.Button(root, text="Clique para conventer", command=conversaoc) #Botão que vai chamar a função de conversão
botao.grid(row=1, column=0) #Posição

#O comando que vai manter o root (Nesse caso seria a janela) em looping infinito (Ou até que o usuário feche a janela)
root.mainloop() #Loop que vai manter o programa rodando até que a janela se feche
