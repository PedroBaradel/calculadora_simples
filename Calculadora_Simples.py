# Importando tkinter

from tkinter import * # Importa a biblioteca completa do tkinter
from tkinter import ttk # Importa uma sub biblioteca do tkinter

# Definindo cores

cor1 = "#b3b3b3"  # black/preta
cor2 = "#ffffff"  # white/branca
cor3 = "#38576b"  # Azul carregando
cor4 = "#ECEFF1"  # cinzenta
cor5 = "#FFAB40"  # Orange/Laranja

janela = Tk() # Cria o ambiente (janela) do tkinter

# Criando frames

janela.title("Calculadora") # Define o nome da janela
janela.geometry("235x310") # Define o tamanho da janela

frame_tela = Frame(janela, width=235, height=50, bg=cor3) # Cria um frame dentro da janela
frame_tela.grid(row=0, column=0) # Define a posição do frame dentro da janela

frame_corpo = Frame(janela, width=235, height=268) # Cria um frame dentro da janela
frame_corpo.grid(row=1, column=0) # Define a posição do frame dentro da janela

# variável todos valores

todos_valores = '' # Variável com valor em branco

# criando label
valor_texto = StringVar() # Define uma variável que recebe uma String Variável que pode ser modificada no decorrer do código

# criando funcao

def entrar_valores(event): # cria um função

    global todos_valores # Define a variável todos_valores acessível para todo o restante do código

    todos_valores = todos_valores + str(event) # variável que concatena a variável toos_valores + string de Event

    # passando valor para a tela
    valor_texto.set(todos_valores) # Exibe o valor da variável todos_valores na tela


# funcao para calcular
    
def calcular(): # cria a função calcular
    global todos_valores # Define a variável todos_valores acessível para todo o restante do código
    resultado = eval(todos_valores) # Avalia a expressão definida em todos_valores (realiza o cálculo)
    valor_texto.set(str(resultado))

# Criando rótulo e definindo posição
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, fg=cor2, bg=cor3, font=('Ivy 18'))
app_label.place(x=0, y=0)

# funcao para limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

# Criando os botões

b_1 = Button(frame_corpo, command = limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


janela.mainloop()